from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from base import models as base_models
from doctor import models as doctor_models
from patient import models as patient_models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
import json


def send_appointment_confirmation_email(billing):
    """
    Helper function to send appointment confirmation email
    """
    try:
        appointment = billing.appointment
        patient = appointment.patient
        
        # Prepare email context
        email_context = {
            'appointment': appointment,
            'billing': billing,
            'patient': patient,
        }
        
        # Render email templates
        html_content = render_to_string('emails/appointment_confirmation.html', email_context)
        text_content = render_to_string('emails/appointment_confirmation.txt', email_context)
        
        # Create email
        subject = f"Appointment Confirmation - #{appointment.appointment_id} | HMS"
        from_email = 'HMS Healthcare <noreply@hms.com>'
        to_email = [patient.email]
        
        # Create multipart email
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=from_email,
            to=to_email
        )
        
        # Attach HTML version
        email.attach_alternative(html_content, "text/html")
        
        # Send email
        email.send()
        
        print(f"Confirmation email sent successfully to {patient.email}")
        return True
        
    except Exception as e:
        print(f"Failed to send confirmation email: {str(e)}")
        return False


def index(request):
    services = base_models.Service.objects.all()
    context = {
        "services": services
    }
    return render(request, "base/index.html", context)


def service_detail(request, service_id):
    service = base_models.Service.objects.get(id=service_id)
    context = {
        "service": service
    }
    return render(request, "base/service_detail.html", context)


@login_required
def book_appointment(request, service_id, doctor_id):
    service = base_models.Service.objects.get(id=service_id)
    doctor = doctor_models.Doctor.objects.get(id=doctor_id)
    patient = patient_models.Patient.objects.get(user=request.user)

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        dob = request.POST.get("dob")
        issues = request.POST.get("issues")
        symptoms = request.POST.get("symptoms")

        # Update patient bio data
        patient.full_name = full_name
        patient.email = email
        patient.mobile = mobile
        patient.gender = gender
        patient.address = address
        patient.dob = dob
        patient.save()

        # Create appointment object
        appointment = base_models.Appointment.objects.create(
            service=service,
            doctor=doctor,
            patient=patient,
            appointment_date=doctor.next_available_appointment_date,
            issues=issues,
            symptoms=symptoms,
        )

        # Create a billing objects
        billing = base_models.Billing()
        billing.patient = patient
        billing.appointment = appointment
        billing.sub_total = appointment.service.cost
        billing.tax = appointment.service.cost * 5 / 100
        billing.total = billing.sub_total + billing.tax
        billing.status = "Unpaid"
        billing.save()

        return redirect("base:checkout", billing.billing_id)

    context = {
        "service": service,
        "doctor": doctor,
        "patient": patient,
    }
    return render(request, "base/book_appointment.html", context)


@login_required
def checkout(request, billing_id):
    billing = base_models.Billing.objects.get(billing_id=billing_id)

    context = {
        "billing": billing,
        # "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        # "paypal_client_id": settings.PAYPAL_CLIENT_ID,
    }
    return render(request, "base/checkout.html", context)


# New Pay Now view - bypasses actual payment processing
@csrf_exempt
def pay_now(request, billing_id):
    """
    Simple payment processing that bypasses actual payment gateways
    """
    if request.method == 'POST':
        try:
            billing = base_models.Billing.objects.get(billing_id=billing_id)

            # Check if billing is already paid
            if billing.status == "Paid":
                return JsonResponse({
                    "success": False,
                    "message": "Payment already processed",
                    "billing_id": billing_id
                })

            # Simulate payment processing (you can add validation logic here)
            # For now, we'll assume payment is always successful

            # Update billing status
            billing.status = "Paid"
            billing.save()

            # Update appointment status
            billing.appointment.status = "Completed"
            billing.appointment.save()

            # Create notifications
            doctor_models.Notification.objects.create(
                doctor=billing.appointment.doctor,
                appointment=billing.appointment,
                type="New Appointment"
            )

            patient_models.Notification.objects.create(
                patient=billing.appointment.patient,
                appointment=billing.appointment,
                type="Appointment Scheduled"
            )

            # Send confirmation email to patient
            send_appointment_confirmation_email(billing)

            return JsonResponse({
                "success": True,
                "message": "Payment processed successfully",
                "billing_id": billing_id
            })

        except base_models.Billing.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Billing record not found",
                "billing_id": billing_id
            })
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": f"Payment processing failed: {str(e)}",
                "billing_id": billing_id
            })

    return JsonResponse({"success": False, "message": "Invalid request method"})


@login_required
def payment_status(request, billing_id):
    billing = base_models.Billing.objects.get(billing_id=billing_id)
    payment_status = request.GET.get("payment_status")
    
    # Send confirmation email if payment is successful and email hasn't been sent yet
    if payment_status == "success" and billing.status == "Paid":
        send_appointment_confirmation_email(billing)
    
    context = {
        "billing": billing,
        "payment_status": payment_status,
    }
    return render(request, "base/payment_status.html", context)
