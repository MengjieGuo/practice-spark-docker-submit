#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 7:29 PM
# @Author  : screwman
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoTaskForSpark.settings")
import django

django.setup()

import os
from django.contrib.auth.models import User

person = User.objects.filter(first_name='1', first_name__contains='a')
print(person)
print(person.username)

