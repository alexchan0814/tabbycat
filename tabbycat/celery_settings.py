# Note the filename here can't be just 'celery'; creates import errrors
from __future__ import absolute_import, unicode_literals

from celery import Celery


# NOTE: Not working — can't import/resolve the app modules
# Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tabbycat.settings')

# NOTE: this is the config we would have imported if importing worked
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# NOTE: This is a workaround to the settings import not working
CELERY_IMPORTS = ['adjallocation.tasks']

app = Celery('tabbycat_celery',
             broker=CELERY_BROKER_URL,
             backend=CELERY_RESULT_BACKEND,
             accept_content=CELERY_ACCEPT_CONTENT,
             task_serializer=CELERY_TASK_SERIALIZER,
             result_serializer=CELERY_RESULT_SERIALIZER,
             imports=CELERY_IMPORTS)

# NOTE: below sections depend on settings import; using CELERY_IMPORTS instead

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
