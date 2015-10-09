# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

from . import load_env

load_env.load_env()

from .celery import app as celery_app  # noqa
