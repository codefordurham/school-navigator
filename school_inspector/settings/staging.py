from school_inspector.settings.base import *

os.environ.setdefault('CACHE_HOST', '127.0.0.1:11211')
os.environ.setdefault('BROKER_HOST', '127.0.0.1:5672')

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES['default']['NAME'] = 'school_inspector_staging'
DATABASES['default']['USER'] = 'school_inspector_staging'
DATABASES['default']['HOST'] = os.environ.get('DB_HOST', '')
DATABASES['default']['PORT'] = os.environ.get('DB_PORT', '')
DATABASES['default']['PASSWORD'] = os.environ['DB_PASSWORD']

PUBLIC_ROOT = '/var/www/school_inspector/public/'

STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '%(CACHE_HOST)s' % os.environ,
    }
}

EMAIL_SUBJECT_PREFIX = '[School_Inspector Staging] '
DEFAULT_FROM_EMAIL = 'noreply@foobar.com'
ADMINS = (
    ('Colin Copeland', 'ccopeland@codeforamerica.org'),
)
MANAGERS = ADMINS

COMPRESS_ENABLED = True

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(';')

# Uncomment if using celery worker configuration
BROKER_URL = 'amqp://school_inspector_staging:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/school_inspector_staging' % os.environ

LOGGING['handlers']['file']['filename'] = '/var/www/school_inspector/log/schools.log'
