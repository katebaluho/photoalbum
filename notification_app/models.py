from django.db import models
from rest_framework.authtoken.admin import User


class Notification(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    message = models.CharField(max_length=250, null=False, blank=False)

    def __repr__(self):
        return f'Notification{self.title}'