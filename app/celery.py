from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.apps import apps

from app.settings import CELERY_BROKER, CELERY_BACKEND

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery(
    'app',
    broker=CELERY_BROKER,
    backend=CELERY_BACKEND
)
app.config_from_object(settings)
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
     'add-every-day': {
         'task': 'notification_app.tasks.email_task',
         'schedule': crontab(hour=12, minute=6),
     },
}
app.conf.timezone = 'UTC'