# celery.py
"""
Using SQS queue & MySQL result
pip install https://github.com/celery/vine/zipball/master#egg=vine
pip install https://github.com/celery/kombu/zipball/master#egg=kombu
pip install https://github.com/celery/py-amqp/zipball/master#egg=amqp
pip install https://github.com/celery/billiard/zipball/master#egg=billiard
pip install https://github.com/celery/celery/zipball/master#egg=celery
celery --app tasks worker --loglevel=debug
celery -A proj worker --loglevel=debug
celery multi start -A proj --loglevel=debug --pidfile=/Users/admin/Documents/tests/python-tester/python-tester/%n.pid --logfile=/Users/admin/Documents/tests/python-tester/python-tester/%n%I.log

Using RabbitMQ queue & result
rabbitmq-server -detached
celery -A proj worker -l info
celery multi start w1 -A proj -l info
celery multi stopwait w1 -A proj -l info
rabbitmqctl stop
"""
from __future__ import absolute_import, unicode_literals

from celery import Celery

from proj import celeryconfig

print('starting...')

app = Celery('proj',
             include=['proj.tasks'])
app.config_from_object(celeryconfig)

if __name__ == '__main__':
# def __main__():
    app.start()
