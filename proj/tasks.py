from __future__ import absolute_import, unicode_literals

from proj.celery import app

print('this is tasks...')


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
