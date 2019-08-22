#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 9:05 AM
# @Author  : screwman
# @Site    : 
# @File    : SparkTaskProcessor.py
# @Software: PyCharm
from django.http import JsonResponse
from django.views import View

from taskmanager.tasks import spark_submit_processor


class SparkTaskProcessor(View):

    def post(self, request):
        resp = {'ok': False, 'message': ''}
        # get spark sql from request
        # 接受文件
        spark_sql = request.FILES.get('file', None)
        # spark_sql = request.POST.get('file', None)

        if spark_sql:
            # 元编程生成 spark-submit 需要提交的任务
            # todo 将文件写到任务管理文件夹
            # meta = self.request.files['file'][0]
            # print(meta)
            # file_path = ''

            # Second Keep file to local dir
            file_path = 'spark_tasks/{0}'.format(spark_sql.name)
            print('Get file path in web: {0}'.format(file_path))
            with open(file_path, 'wb+') as destination:
                for chunk in spark_sql.chunks():
                    destination.write(chunk)

            # Submit the spark task file
            spark_submit_processor.delay(file_path)
        else:
            resp['message'] = 'The parameter sparkSQL must be given.'
        return JsonResponse(resp)
