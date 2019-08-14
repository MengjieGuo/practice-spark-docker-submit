#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 3:41 PM
# @Author  : screwman
# @Site    : 
# @File    : entrypoint.py.py
# @Software: PyCharm

# Spark task template of python version
from datetime import datetime

from pyspark.sql import SparkSession


def read_from_postgres_with_spark():
    """
    In coming
    Use Spark read data from postgres

    :return:
    """
    result = ''
    return result


def read_from_postgres_to_df():
    """
    Read data from postgres, And turn data to DF
    :return:
    """
    print('test funcion one')

    # dict_lst = {'A': ['1', '2', '3', '3'], 'B': '2'}
    st = datetime.now()
    spark = SparkSession.builder.appName('abc').enableHiveSupport().getOrCreate()
    sc = spark.sparkContext

    dict_lst = [
        {"A": 1, "type_activity_name": "xxx"},
        {"A": 2, "type_activity_name": "yyy"},
        {"A": 3, "type_activity_name": "zzz"}
    ]

    rdd = sc.parallelize(dict_lst)
    print(type(rdd))
    df = spark.read.json(rdd)

    df.groupBy().agg()
    df.createOrReplaceTempView('test')
    step_1 = datetime.now()
    print('Load data: {0}'.format(step_1-st))
    df.show()
    from pyspark import shell
    sql = """
        select A, count(*)
        from test
        group  by A
    """
    df = shell.sql(sql)
    df.show()
    step_2 = datetime.now()
    print('Spark sql execute: {0}'.format(step_2-step_1))
    result = ''

    # json()
    # result_name : value

    return result


def write_to_postgres_with_spark():
    """
    In coming
    Use spark write data to postgres
    :return:
    """
    result = ''
    return result


def write_to_postgres_from_df():
    """
    DF to python DataStructure, And write data to postgres
    :return:
    """
    result = ''
    return result


def execute(func, *args, **kwargs):
    """
    Func entry
    :param func:
    :param args:
    :param kwargs:
    :return:
    """
    st = datetime.now()
    result = func(*args, **kwargs)
    print('Execute time: {0}'.format(datetime.now()-st))
    return result


if __name__ == '__main__':
    func = read_from_postgres_to_df
    execute(func=func)
