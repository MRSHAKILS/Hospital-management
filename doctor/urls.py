from django.urls import path
from doctor import views

app_name = "doctor"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("appointments/", views.appointments, name="appointments"),
    path("appointments/<appointment_id>/", views.appointment_detail, name="appointment_detail"),
    
    path("cancel_appointment/<appointment_id>/", views.cancel_appointment, name="cancel_appointment"),
    path("activate_appointment/<appointment_id>/", views.activate_appointment, name="activate_appointment"),
    path("complete_appointment/<appointment_id>/", views.complete_appointment, name="complete_appointment"),

    path("add_medical_report/<appointment_id>/", views.add_medical_report, name="add_medical_report"),
    path("edit_medical_report/<appointment_id>/<medical_report_id>/", views.edit_medical_report, name="edit_medical_report"),

    path("add_lab_test/<appointment_id>/", views.add_lab_test, name="add_lab_test"),
    path("edit_lab_test/<appointment_id>/<lab_test_id>/", views.edit_lab_test, name="edit_lab_test"),

    path("add_prescription/<appointment_id>/", views.add_prescription, name="add_prescription"),
    path("edit_prescription/<appointment_id>/<prescription_id>/", views.edit_prescription, name="edit_prescription"),

    path("payments/", views.payments, name="payments"),

    path("notifications/", views.notifications, name="notifications"),
    path("mark_noti_seen/<id>/", views.mark_noti_seen, name="mark_noti_seen"),
    path("profile/", views.profile, name="profile"),
    
    # Availability Management
    path("availability/", views.manage_availability, name="manage_availability"),
    
    # Slot Management
    path("slots/", views.manage_slots, name="manage_slots"),
    path("slots/add/", views.add_slot, name="add_slot"),
    path("slots/edit/<int:slot_id>/", views.edit_slot, name="edit_slot"),
    path("slots/delete/<int:slot_id>/", views.delete_slot, name="delete_slot"),
    path("slots/toggle/<int:slot_id>/", views.toggle_slot, name="toggle_slot"),
    
    # Days Off Management
    path("days-off/", views.manage_days_off, name="manage_days_off"),
    path("days-off/add/", views.add_day_off, name="add_day_off"),
    path("days-off/delete/<int:dayoff_id>/", views.delete_day_off, name="delete_day_off"),
    
    # API Endpoints
    path("api/slots/<int:doctor_id>/<str:date_str>/", views.get_available_slots, name="get_available_slots"),
]