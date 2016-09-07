# celeryconfig
import urllib.parse

# BROKER_URL = 'sqs://{0}:{1}@'.format(
#     urllib.parse.quote_plus(AWS_ACCESS_KEY_ID),
#     urllib.parse.quote_plus(AWS_SECRET_ACCESS_KEY)
# )

AMQP_USER = 'tester'
AMQP_PASS = 'testing'

CELERY_USER = AMQP_USER
CELERY_PASS = AMQP_PASS

BROKER_URL = 'amqp://{0}:{1}@localhost/test'.format(
    urllib.parse.quote_plus(CELERY_USER),
    urllib.parse.quote_plus(CELERY_PASS)
)
BROKER_TRANSPORT_OPTIONS = {
    # 'region': AWS_REGION,
    'polling_interval': 3,
    'visibility_timeout': 3600,
    'queue_name_prefix': 'celery-'
}

# CELERY_RESULT_BACKEND = 'db+mysql://pftest:pftest1008@test.codmhuzpr5fy.ap-northeast-1.rds.amazonaws.com/peoplefund'
CELERY_RESULT_BACKEND = BROKER_URL

print('this is config...')


