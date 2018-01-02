# Settings for live deployed environments: vagrant, staging, production, etc
from .base import *  # noqa
import dj_database_url

os.environ.setdefault('CACHE_HOST', '127.0.0.1:11211')
os.environ.setdefault('BROKER_HOST', '127.0.0.1:5672')

ENVIRONMENT = os.environ['ENVIRONMENT']

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)  # noqa: F405

WEBSERVER_ROOT = '/var/www/school_navigator/'

PUBLIC_ROOT = os.path.join(PROJECT_ROOT, 'public')

STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': '%(CACHE_HOST)s' % os.environ,
#     }
# }

if 'EMAIL_HOST_PASSWORD' in os.environ:
    EMAIL_HOST = "email-smtp.us-east-1.amazonaws.com"
    EMAIL_HOST_USER = "AKIAJ7B33FCWH5FMSOBA"
    EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

EMAIL_SUBJECT_PREFIX = '[School_Navigator %s] ' % ENVIRONMENT.title()
DEFAULT_FROM_EMAIL = 'noreply@%(DOMAIN)s' % os.environ
SERVER_EMAIL = DEFAULT_FROM_EMAIL

COMPRESS_ENABLED = True

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = ['*']

# Uncomment if using celery worker configuration
CELERY_SEND_TASK_ERROR_EMAILS = True
BROKER_URL = os.environ.get('REDIS_URL', '')

# Environment overrides
# These should be kept to an absolute minimum
if ENVIRONMENT.upper() == 'LOCAL':
    # Don't send emails from the Vagrant boxes
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMINS = (
    ('Code for Durham', 'school-inspector@googlegroups.com'),
)
MANAGERS = ADMINS
