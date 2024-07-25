import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('newspaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_notifications_every_30_seconds': {
        'task': 'news.tasks.send_notifications',
        'schedule': 30,
    },
    'send_week_notification_every_week': {
        'task': 'news.tasks.send_week_notification',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    }
}