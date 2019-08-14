#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 10:21 AM
# @Author  : screwman
# @Site    : 
# @File    : tasks.py
# @Software: PyCharm
import subprocess

from celery import shared_task, task



# @task()
@shared_task()
# @shared_task(name='task1')
def spark_task_1():
    """
    Spark 任务1注册
    :return:
    """
    command = 'pwd'
    result = subprocess.call(command, shell=True)
    # write result to some where


@shared_task()
# @shared_task(name='task2')
def spark_task_2():
    """
    Spark 任务2注册
    :return:
    """
    command = 'pwd'
    result = subprocess.call(command, shell=True)
    # write result to some where
