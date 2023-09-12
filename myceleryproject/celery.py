import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myceleryproject.settings')

app = Celery('myceleryproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

#To monitor worker
# celery -A myceleryproject worker -l info 

#To monitor celery beat
#celery -A myceleryproject beat -l info