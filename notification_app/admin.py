from django.contrib import admin

from notification_app.models import Notification


@admin.register(Notification)
class MediaAdmin(admin.ModelAdmin):
    model = Notification
