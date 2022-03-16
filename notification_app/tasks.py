from celery import shared_task
from django.core.mail import send_mail

from app import settings
from celery.utils.log import get_task_logger

from notification_app.utils import get_email_top_photo, get_last_message_info

logger = get_task_logger(__name__)


@shared_task
def email_task():
    notice = get_last_message_info()
    send_mail(notice['title'], notice['message'],
              settings.DEFAULT_FROM_EMAIL,get_email_top_photo())







