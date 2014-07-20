from school_inspector.settings.staging import *

# There should be only minor differences from staging

DATABASES['default']['NAME'] = 'school_inspector_production'
DATABASES['default']['USER'] = 'school_inspector_production'

EMAIL_SUBJECT_PREFIX = '[School_Inspector Prod] '

# Uncomment if using celery worker configuration
# BROKER_URL = 'amqp://school_inspector_production:%(BROKER_PASSWORD)s@%(BROKER_HOST)s/school_inspector_production' % os.environ