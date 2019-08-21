#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 9:11 AM
# @Author  : screwman
# @Site    : 
# @File    : spark_submit_file.py
# @Software: PyCharm
from datetime import datetime


def keep_task_run_time(start_time):
    pass


def task_entry(spark_sql):
    """
    机动车业务办理数据统计

    按照时间（年、月）、大队、业务类型统计记录数量
    :param which_sql:
    :return:
    """
    st = datetime.now()

    # from pyspark import SparkConf
    from pyspark import SparkContext
    from pyspark import SQLContext
    st_1 = datetime.now()

    print("Got sql: {sql}".format(sql=spark_sql))

    # conf = SparkConf().setAppName("testing").setMaster("local[2]")
    sc = SparkContext().getOrCreate()
    sql_context = SQLContext(sc)
    st_3 = datetime.now()

    # For use sql, must create a table or view

    # Load
    # File path must be given
    df_veh_flow = sql_context.read.load('/srv/BigData/dbdata_service/ffk/veh_flow_to_190805_allf')
    st_4 = datetime.now()

    df_veh_flow.createOrReplaceTempView('veh_flow_temp_view_002')  # Create a view
    st_5 = datetime.now()

    # execute sql
    from pyspark.shell import spark
    df_veh_flow_key1 = spark.sql(spark_sql)
    st_6 = datetime.now()

    df_veh_flow_key1.show()
    st_7 = datetime.now()
    print('运行时间统计：'
          '\nGet sqlcontext: {1}'
          '\nLoad data: {2}'
          '\nCreate table or view: {3}'
          '\nExecute sql: {4}'
          '\nShow result: {5}'.format(st_3 - st_1, st_4 - st_3, st_5 - st_4, st_6 - st_5, st_7 - st_6))
    keep_task_run_time(start_time=st)
