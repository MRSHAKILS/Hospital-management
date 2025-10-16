from django.db import models
from django.utils import timezone
from datetime import time

from userauths import models as userauths_models

NOTIFICATION_TYPE = (
    ("New Appointment", "New Appointment"),
    ("Appointment Cancelled", "Appointment Cancelled"),
)

WEEKDAY_CHOICES = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class Doctor(models.Model):
    user = models.OneToOneField(userauths_models.User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to="images", null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    qualifications = models.CharField(max_length=100, null=True, blank=True)
    years_of_experience = models.CharField(max_length=100, null=True, blank=True)
    next_available_appointment_date = models.DateTimeField(default=timezone.now, null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.full_name}"


class DoctorAvailability(models.Model):
    """
    Defines which days a doctor is available to see patients
    """
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='availabilities')
    day_of_week = models.IntegerField(choices=WEEKDAY_CHOICES)
    is_available = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Doctor Availabilities"
        unique_together = ('doctor', 'day_of_week')
        ordering = ['day_of_week']
    
    def __str__(self):
        return f"Dr. {self.doctor.full_name} - {self.get_day_of_week_display()}"


class AppointmentSlot(models.Model):
    """
    Defines specific time slots when a doctor is available for appointments
    """
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointment_slots')
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)
    max_patients = models.IntegerField(default=1, help_text="Maximum number of patients for this slot")
    
    class Meta:
        verbose_name_plural = "Appointment Slots"
        ordering = ['start_time']
    
    def __str__(self):
        return f"Dr. {self.doctor.full_name} - {self.start_time.strftime('%I:%M %p')} to {self.end_time.strftime('%I:%M %p')}"
    
    def is_slot_available(self, date):
        """
        Check if this slot is available on a specific date
        """
        from base.models import Appointment
        
        # Check if the day is in doctor's availability
        day_of_week = date.weekday()
        availability = DoctorAvailability.objects.filter(
            doctor=self.doctor,
            day_of_week=day_of_week,
            is_available=True
        ).exists()
        
        if not availability:
            return False
        
        # Check if slot is active
        if not self.is_active:
            return False
        
        # Count booked appointments for this slot on this date
        from datetime import datetime, timedelta
        start_datetime = datetime.combine(date, self.start_time)
        end_datetime = datetime.combine(date, self.end_time)
        
        booked_count = Appointment.objects.filter(
            doctor=self.doctor,
            appointment_date__gte=start_datetime,
            appointment_date__lt=end_datetime,
            status__in=['Scheduled', 'Pending']
        ).count()
        
        return booked_count < self.max_patients


class DayOff(models.Model):
    """
    Allows doctors to mark specific dates as unavailable
    """
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='days_off')
    date = models.DateField()
    reason = models.CharField(max_length=255, blank=True, null=True)
    cancel_existing_appointments = models.BooleanField(
        default=False,
        help_text="Cancel all appointments scheduled for this day"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Days Off"
        unique_together = ('doctor', 'date')
        ordering = ['date']
    
    def __str__(self):
        return f"Dr. {self.doctor.full_name} - Day Off on {self.date}"
    
    def save(self, *args, **kwargs):
        """
        Override save to cancel appointments if requested
        """
        from base.models import Appointment
        from patient.models import Notification as PatientNotification
        
        super().save(*args, **kwargs)
        
        if self.cancel_existing_appointments:
            # Get all scheduled appointments for this doctor on this date
            from datetime import datetime, timedelta
            start_of_day = datetime.combine(self.date, time.min)
            end_of_day = datetime.combine(self.date, time.max)
            
            appointments = Appointment.objects.filter(
                doctor=self.doctor,
                appointment_date__gte=start_of_day,
                appointment_date__lte=end_of_day,
                status__in=['Scheduled', 'Pending']
            )
            
            # Cancel each appointment and notify patient
            for appointment in appointments:
                appointment.status = 'Cancelled'
                appointment.save()
                
                # Create notification for patient
                PatientNotification.objects.create(
                    patient=appointment.patient,
                    appointment=appointment,
                    type="Appointment Cancelled"
                )


class Notification(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey("base.Appointment", on_delete=models.CASCADE, null=True, blank=True, related_name="doctor_appointment_notification")
    type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Notification"

    def __str__(self):
        return f"Dr {self.doctor.full_name} Notification"
