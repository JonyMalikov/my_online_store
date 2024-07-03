import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop_settings')
app = Celery('myshop')
app.config_from_object('django.conf:settigs', namespace='CELERY')
app.autodiscover_tasks()