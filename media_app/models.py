from django.contrib.auth.models import User
from django.core import validators
from django.db import models

from app import settings
from media_app.validators import MaxSizeValidator


class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='photos')
    file = models.FileField(null=False,
                            blank=False,
                            validators=[validators.FileExtensionValidator(settings.ALLOWED_UPLOAD_FILES,
                                                                          message='File of this format cannot be load'),
                                        MaxSizeValidator(settings.ALLOWED_UPLOAD_FILES_SIZE_MB)]
                            )
    title = models.CharField(null=False, blank=False, max_length=250)
    create_date = models.DateTimeField(auto_now=True)
    counter_views = models.IntegerField(default=0)

    def increase_counter_views(self):
        self.counter_views += 1
        self.save()



