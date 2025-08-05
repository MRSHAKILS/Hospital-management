from django.contrib import admin
from doctor import models


<<<<<<< HEAD
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'specialization',
                    'qualifications', 'years_of_experience']
=======

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'specialization', 'qualifications', 'years_of_experience']
>>>>>>> e387db8dff2078def121911fddcba075f9b6b62d


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'appointment', 'type', 'seen', 'date']


<<<<<<< HEAD
=======

>>>>>>> e387db8dff2078def121911fddcba075f9b6b62d
admin.site.register(models.Doctor, DoctorAdmin)
admin.site.register(models.Notification, NotificationAdmin)
