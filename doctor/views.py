from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta, time
from doctor import models as doctor_models
from base import models as base_models
from patient import models as patient_models
import json

@login_required
def dashboard(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointments = base_models.Appointment.objects.filter(doctor=doctor)
    notifications = doctor_models.Notification.objects.filter(doctor=doctor)

    context = {
        "appointment": appointments,
        "notifications": notifications,
    }

    return render(request, "doctor/dashboard.html", context)


@login_required
def appointments(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointments = base_models.Appointment.objects.filter(doctor=doctor)

    context = {
        "appointments": appointments,
    }

    return render(request, "doctor/appointments.html", context)

@login_required
def appointment_detail(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    medical_records = base_models.MedicalRecord.objects.filter(appointment=appointment)
    lab_tests = base_models.LabTest.objects.filter(appointment=appointment)
    prescriptions = base_models.Prescription.objects.filter(appointment=appointment)

    context = {
        "appointment": appointment,
        "medical_records": medical_records,
        "lab_tests": lab_tests,
        "prescriptions": prescriptions,
    }

    return render(request, "doctor/appointment_detail.html", context)


@login_required
def cancel_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

  
    appointment.status = "Cancelled"
    appointment.save()

    messages.success(request, "Appointment cancelled successfully.")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def activate_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    appointment.status = "Scheduled"
    appointment.save()

    messages.success(request, "Appointment Re-Scheduled successfully.")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def complete_appointment(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    appointment.status = "Completed"
    appointment.save()

    messages.success(request, "Appointment completed successfully.")
    return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def add_medical_report(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    if request.method == "POST":
        diagnosis = request.POST.get("diagnosis")
        treatment = request.POST.get("treatment")
        prescription = request.POST.get("prescription")
        base_models.MedicalRecord.objects.create(appointment=appointment,diagnosis=diagnosis,treatment=treatment)

        messages.success(request, "Medical report added successfully.")
        return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def edit_medical_report(request, appointment_id, medical_report_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)
    medical_report = base_models.MedicalRecord.objects.get(id=medical_report_id, appointment=appointment)

    if request.method == "POST":
        diagnosis = request.POST.get("diagnosis")
        treatment = request.POST.get("treatment")

        medical_report.diagnosis = diagnosis
        medical_report.treatment = treatment
        medical_report.save()

        messages.success(request, "Medical report updated successfully.")
        return redirect("doctor:appointment_detail", appointment.appointment_id)  
    

@login_required
def add_lab_test(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    if request.method == "POST":
        test_name = request.POST.get("test_name")
        description = request.POST.get("description")
        result = request.POST.get("result")
        base_models.LabTest.objects.create(appointment=appointment, test_name=test_name, description=description, result=result)

        messages.success(request, "Lab report added successfully.")
        return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def edit_lab_test(request, appointment_id, lab_test_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)
    lab_test = base_models.LabTest.objects.get(id=lab_test_id, appointment=appointment)

    if request.method == "POST":
        test_name = request.POST.get("test_name")
        description = request.POST.get("description")
        result = request.POST.get("result")
        
        lab_test.test_name = test_name
        lab_test.description = description
        lab_test.result = result
        lab_test.save()

        messages.success(request, "Lab report updated successfully.")
        return redirect("doctor:appointment_detail", appointment.appointment_id)
    

@login_required
def add_prescription(request, appointment_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)

    if request.method == "POST":
        medications = request.POST.get("medications")
        base_models.Prescription.objects.create(appointment=appointment, medications=medications)

        messages.success(request, "Prescription added successfully.")
        return redirect("doctor:appointment_detail", appointment.appointment_id)
    

@login_required
def edit_prescription(request, appointment_id, prescription_id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    appointment = base_models.Appointment.objects.get(appointment_id=appointment_id, doctor=doctor)
    prescription = base_models.Prescription.objects.get(id=prescription_id, appointment=appointment)

    if request.method == "POST":
        medications = request.POST.get("medications")
        prescription.medications = medications
        prescription.save()

        messages.success(request, "Prescription updated successfully.")
        return redirect("doctor:appointment_detail", appointment.appointment_id)


@login_required
def payments(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    payments = base_models.Billing.objects.filter(appointment__doctor=doctor, status="Paid")

    context = {
        "payments": payments
    }

    return render(request, "doctor/payments.html", context)


@login_required
def notifications(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    notifications = doctor_models.Notification.objects.filter(doctor=doctor, seen=False)

    context = {
        "notifications": notifications
    }

    return render(request, "doctor/notifications.html", context)



@login_required
def mark_noti_seen(request, id):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    notification = doctor_models.Notification.objects.get(doctor=doctor, id=id)
    notification.seen = True
    notification.save()

    messages.success(request, "Notification marked as seen.")
    return redirect("doctor:notifications")
 

@login_required
def profile(request):
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    formatted_next_available_appointment_date = doctor.next_available_appointment_date.strftime('%Y-%m-%d')

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        image = request.FILES.get("image")
        mobile = request.POST.get("mobile")
        country = request.POST.get("country")
        bio = request.POST.get("bio")
        specialization = request.POST.get("specialization")
        qualifications = request.POST.get("qualifications")
        years_of_experience = request.POST.get("years_of_experience")
        next_available_appointment_date = request.POST.get("next_available_appointment_date")

        doctor.full_name = full_name
        doctor.mobile = mobile
        doctor.country = country
        doctor.bio = bio
        doctor.specialization = specialization
        doctor.qualifications = qualifications
        doctor.years_of_experience = years_of_experience
        

        if image!= None:
            doctor.image = image

        doctor.save()

        messages.success(request, "Profile updated successfully.")
        return redirect("doctor:profile")
    
    context = {
        "doctor": doctor,
        "formatted_next_available_appointment_date": formatted_next_available_appointment_date,
    }

    return render(request, "doctor/profile.html", context)


# ==========================
# Availability Management
# ==========================

@login_required
def manage_availability(request):
    """
    View for doctors to manage their weekly availability
    """
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    
    # Get or create availability for all days
    availabilities = []
    for day_num, day_name in doctor_models.WEEKDAY_CHOICES:
        availability, created = doctor_models.DoctorAvailability.objects.get_or_create(
            doctor=doctor,
            day_of_week=day_num,
            defaults={'is_available': False}
        )
        availabilities.append(availability)
    
    if request.method == "POST":
        # Update availability for each day
        for day_num, day_name in doctor_models.WEEKDAY_CHOICES:
            is_available = request.POST.get(f"day_{day_num}") == "on"
            doctor_models.DoctorAvailability.objects.update_or_create(
                doctor=doctor,
                day_of_week=day_num,
                defaults={'is_available': is_available}
            )
        
        messages.success(request, "Availability updated successfully.")
        return redirect("doctor:manage_availability")
    
    context = {
        "doctor": doctor,
        "availabilities": availabilities,
    }
    return render(request, "doctor/manage_availability.html", context)


@login_required
def manage_slots(request):
    """
    View for doctors to manage their appointment time slots
    """
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    slots = doctor_models.AppointmentSlot.objects.filter(doctor=doctor)
    
    context = {
        "doctor": doctor,
        "slots": slots,
    }
    return render(request, "doctor/manage_slots.html", context)


@login_required
def add_slot(request):
    """
    Add a new appointment slot
    """
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    
    if request.method == "POST":
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        max_patients = request.POST.get("max_patients", 1)
        
        # Create the slot
        doctor_models.AppointmentSlot.objects.create(
            doctor=doctor,
            start_time=start_time,
            end_time=end_time,
            max_patients=max_patients,
            is_active=True
        )
        
        messages.success(request, "Appointment slot added successfully.")
        return redirect("doctor:manage_slots")
    
    return redirect("doctor:manage_slots")


@login_required
def edit_slot(request, slot_id):
    """
    Edit an existing appointment slot
    """
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    slot = doctor_models.AppointmentSlot.objects.get(id=slot_id, doctor=doctor)
    
    if request.method == "POST":
        slot.start_time = request.POST.get("start_time")
        slot.end_time = request.POST.get("end_time")
        slot.max_patients = request.POST.get("max_patients", 1)
        slot.is_active = request.POST.get("is_active") == "on"
        slot.save()
        
        messages.success(request, "Appointment slot updated successfully.")
        return redirect("doctor:manage_slots")
    
    return redirect("doctor:manage_slots")


@login_required
def delete_slot(request, slot_id):
    """
    Delete an appointment slot
    """
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    slot = doctor_models.AppointmentSlot.objects.get(id=slot_id, doctor=doctor)
    slot.delete()
    
    messages.success(request, "Appointment slot deleted successfully.")
    return redirect("doctor:manage_slots")


@login_required
def toggle_slot(request, slot_id):
    """
    Toggle slot active/inactive status
    """
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    slot = doctor_models.AppointmentSlot.objects.get(id=slot_id, doctor=doctor)
    slot.is_active = not slot.is_active
    slot.save()
    
    status = "activated" if slot.is_active else "deactivated"
    messages.success(request, f"Appointment slot {status} successfully.")
    return redirect("doctor:manage_slots")


@login_required
def manage_days_off(request):
    """
    View for doctors to manage their days off
    """
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    
    # Get upcoming days off
    from django.utils import timezone
    days_off = doctor_models.DayOff.objects.filter(
        doctor=doctor,
        date__gte=timezone.now().date()
    ).order_by('date')
    
    context = {
        "doctor": doctor,
        "days_off": days_off,
    }
    return render(request, "doctor/manage_days_off.html", context)


@login_required
def add_day_off(request):
    """
    Add a day off
    """
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    
    if request.method == "POST":
        date_str = request.POST.get("date")
        reason = request.POST.get("reason", "")
        cancel_appointments = request.POST.get("cancel_appointments") == "on"
        
        # Convert date string to date object
        from datetime import datetime
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Create day off
        doctor_models.DayOff.objects.create(
            doctor=doctor,
            date=date_obj,
            reason=reason,
            cancel_existing_appointments=cancel_appointments
        )
        
        messages.success(request, "Day off added successfully.")
        if cancel_appointments:
            messages.info(request, "All appointments for this day have been cancelled.")
        
        return redirect("doctor:manage_days_off")
    
    return redirect("doctor:manage_days_off")


@login_required
def delete_day_off(request, dayoff_id):
    """
    Delete a day off
    """
    doctor = doctor_models.Doctor.objects.get(user=request.user)
    day_off = doctor_models.DayOff.objects.get(id=dayoff_id, doctor=doctor)
    day_off.delete()
    
    messages.success(request, "Day off removed successfully.")
    return redirect("doctor:manage_days_off")


# ==========================
# AJAX API Endpoints
# ==========================

@csrf_exempt
def get_available_slots(request, doctor_id, date_str):
    """
    API endpoint to get available slots for a doctor on a specific date
    """
    try:
        doctor = doctor_models.Doctor.objects.get(id=doctor_id)
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        
        # Check if the date is a day off
        is_day_off = doctor_models.DayOff.objects.filter(
            doctor=doctor,
            date=date_obj
        ).exists()
        
        if is_day_off:
            return JsonResponse({
                'success': False,
                'message': 'Doctor is not available on this date.'
            })
        
        # Check if the day of week is available
        day_of_week = date_obj.weekday()
        is_available = doctor_models.DoctorAvailability.objects.filter(
            doctor=doctor,
            day_of_week=day_of_week,
            is_available=True
        ).exists()
        
        if not is_available:
            return JsonResponse({
                'success': False,
                'message': 'Doctor is not available on this day of the week.'
            })
        
        # Get all active slots for this doctor
        slots = doctor_models.AppointmentSlot.objects.filter(
            doctor=doctor,
            is_active=True
        ).order_by('start_time')
        
        # Build list of available slots
        available_slots = []
        for slot in slots:
            if slot.is_slot_available(date_obj):
                available_slots.append({
                    'id': slot.id,
                    'start_time': slot.start_time.strftime('%H:%M'),
                    'end_time': slot.end_time.strftime('%H:%M'),
                    'display': f"{slot.start_time.strftime('%I:%M %p')} - {slot.end_time.strftime('%I:%M %p')}"
                })
        
        return JsonResponse({
            'success': True,
            'slots': available_slots
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        })