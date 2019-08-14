#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 6:54 PM
# @Author  : screwman
# @Site    : 
# @File    : python_call_shell.py
# @Software: PyCharm
import subprocess

command = 'bash run_spark_app.sh'
subprocess.call(command, shell=True)