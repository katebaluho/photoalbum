from django.db.models.signals import post_save
from django.dispatch import receiver

from media_app.models import Media
from media_app.utils import save_thumbnail_image, save_webp_image


@receiver(post_save, sender=Media)
def create_thumbnail_image(sender, instance=None, **kwargs):
    if instance:
        save_thumbnail_image(instance.file)
        save_webp_image(instance.file)