#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 10:14 AM
# @Author  : screwman
# @Site    : 
# @File    : celery.py.py
# @Software: PyCharm

from __future__ import absolute_import, unicode_literals
import os
import subprocess

from celery import Celery, shared_task

# set the default Django settings module for the 'celery' program.
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoTaskForSpark.settings')

app = Celery('app-DjangoTaskForSpark')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks() # packages=lambda: settings.INSTALLED_APPS


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
