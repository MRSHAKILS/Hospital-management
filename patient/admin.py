from django.contrib import admin
from patient import models

<<<<<<< HEAD

=======
>>>>>>> e387db8dff2078def121911fddcba075f9b6b62d
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'email', 'mobile', 'gender', 'dob']


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['patient', 'appointment', 'type', 'seen', 'date']


admin.site.register(models.Patient, PatientAdmin)
<<<<<<< HEAD
admin.site.register(models.Notification, NotificationAdmin)
=======
admin.site.register(models.Notification, NotificationAdmin)
>>>>>>> e387db8dff2078def121911fddcba075f9b6b62d
