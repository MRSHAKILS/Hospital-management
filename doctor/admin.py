from django.contrib import admin
from doctor import models


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'specialization',
                    'qualifications', 'years_of_experience']


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'appointment', 'type', 'seen', 'date']


class DoctorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'day_of_week', 'is_available']
    list_filter = ['day_of_week', 'is_available']
    search_fields = ['doctor__full_name']


class AppointmentSlotAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'start_time', 'end_time', 'is_active', 'max_patients']
    list_filter = ['is_active', 'doctor']
    search_fields = ['doctor__full_name']


class DayOffAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'date', 'reason', 'cancel_existing_appointments']
    list_filter = ['date', 'cancel_existing_appointments']
    search_fields = ['doctor__full_name', 'reason']
    date_hierarchy = 'date'


admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Notification, NotificationAdmin)
admin.site.register(models.DoctorAvailability, DoctorAvailabilityAdmin)
admin.site.register(models.AppointmentSlot, AppointmentSlotAdmin)
admin.site.register(models.DayOff, DayOffAdmin)
