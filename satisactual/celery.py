import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'satisactual.settings')

# Create Celery app
app = Celery('satisactual')

# Load Celery config from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto discover tasks
app.autodiscover_tasks()