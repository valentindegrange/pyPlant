from django.contrib import admin

from pyPlants.models import Plant, NotificationCenter, Notification


class NotificationCenterAdmin(admin.ModelAdmin):
    list_display = ('user', 'enable_email_notifications',
                    'enable_sms_notifications', 'preferred_notification_hour',
                    'last_notification_sent')
    search_fields = ['user']
    list_filter = ['enable_email_notifications', 'enable_sms_notifications',
                   'preferred_notification_hour']


class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'sun_exposure', 'water_frequency_summer',
                    'water_frequency_winter', 'last_watered', 'leaf_mist',
                    'fertilizer', 'fertilizer_season', 'last_fertilized',
                    'repotting', 'repotting_season', 'last_repotted')
    search_fields = ['name', 'user']
    list_filter = ['last_watered', 'last_fertilized', 'last_repotted']


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'message', 'date', 'viewed')
    search_fields = ['user', 'message']
    list_filter = ['date', 'viewed']


admin.site.register(Plant, PlantAdmin)
admin.site.register(NotificationCenter, NotificationCenterAdmin)
admin.site.register(Notification, NotificationAdmin)
