#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 3:25 PM
# @Author  : screwman
# @Site    : 
# @File    : send_file.py
# @Software: PyCharm
import sys

import requests

file_name = sys.argv[1]

url = 'http://127.0.0.1:8000/FusionInsight/SubmitTask/'
files = {'file': open('./{0}'.format(file_name), 'rb')}
data = {'k1': 1, 'k2': 2}

response = requests.post(url, files=files, data=data)
print(response)
