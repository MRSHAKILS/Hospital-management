from django.db import models
from django.utils import timezone

<<<<<<< HEAD
=======

>>>>>>> e387db8dff2078def121911fddcba075f9b6b62d
from userauths import models as userauths_models

NOTIFICATION_TYPE = (
    ("New Appointment", "New Appointment"),
    ("Appointment Cancelled", "Appointment Cancelled"),
)

<<<<<<< HEAD

class Doctor(models.Model):
    user = models.OneToOneField(
        userauths_models.User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(upload_to="images", null=True, blank=True)
=======
class Doctor(models.Model):
    user = models.OneToOneField(userauths_models.User, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images", null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
>>>>>>> e387db8dff2078def121911fddcba075f9b6b62d
    mobile = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    specialization = models.CharField(max_length=100, null=True, blank=True)
    qualifications = models.CharField(max_length=100, null=True, blank=True)
<<<<<<< HEAD
    years_of_experience = models.CharField(
        max_length=100, null=True, blank=True)
    next_available_appointment_date = models.DateTimeField(
        default=timezone.now, null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.full_name}"


class Notification(models.Model):
    doctor = models.ForeignKey(
        Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey("base.Appointment", on_delete=models.CASCADE,
                                    null=True, blank=True, related_name="doctor_appointment_notification")
=======
    years_of_experience = models.CharField(max_length=100, null=True, blank=True)
    next_available_appointment = models.DateTimeField(default=timezone.now, null=True, blank=True)
   

    def __str__(self):
        return f"Dr. {self.full_name}"
    
class Notification(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True)
    appointment = models.ForeignKey("base.Appointment", on_delete=models.CASCADE, null=True, blank=True, related_name="doctor_appointment_notification")
>>>>>>> e387db8dff2078def121911fddcba075f9b6b62d
    type = models.CharField(max_length=100, choices=NOTIFICATION_TYPE)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Notification"

    def __str__(self):
<<<<<<< HEAD
        return f"Dr {self.doctor.full_name} Notification"
=======
        return f"Dr {self.doctor.ull_name} Notification"

>>>>>>> e387db8dff2078def121911fddcba075f9b6b62d
