#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 10:21 AM
# @Author  : screwman
# @Site    : 
# @File    : tasks.py
# @Software: PyCharm
# import subprocess

from celery import shared_task
# from celery import task

# # @task()
# @shared_task()
# # @shared_task(name='task1')
# def spark_task_1():
#     """
#     Spark 任务1注册
#     :return:
#     """
#     command = 'pwd'
#     result = subprocess.call(command, shell=True)
#     # write result to some where
#
#
# @shared_task()
# # @shared_task(name='task2')
# def spark_task_2():
#     """
#     Spark 任务2注册
#     :return:
#     """
#     command = 'pwd'
#     result = subprocess.call(command, shell=True)
#     # write result to some where


@shared_task()
def spark_submit_processor(file_path):
    """
    调用 spark submit 命令提交任务

    spark version 2.1
    :注意: 提交

    :return:
    """
    # python 调用shell命令 完成spark-submit文件提交
    import subprocess
    command = 'su - TestUser001 -c  "/opt/hadoopclient/Spark2x/spark/bin/spark-submit' \
              ' /home/var/project/SparkProjectTest/{spark_task_file}"' \
        .format(spark_task_file=file_path)
    print(command)
    # result = subprocess.call(command, shell=True)
    # print(result)
