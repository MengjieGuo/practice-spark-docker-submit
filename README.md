[TOC]

# practice-spark-docker-submit

# 启动项目

- 依赖于rabbitmq redis flower，这些服务可以部署于其他服务器
- 采用宿主机启动方式，启动以下服务
    - celery beat
    - celery worker
    - gunicorn

# 如何提交任务

- 通过http端口提交spark任务文件

可以参考以下代码

> python send_file.py my_spark_task.py -- 运行代码, 其中 my_spark_task.py 为 spark 任务文件
>
> cat send_file.py -- 查看代码
  
```python

#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys

import requests

file_name = sys.argv[1]

url = 'http://127.0.0.1:8000/FusionInsight/SubmitTask/'
files = {'file': open('./{0}'.format(file_name), 'rb')}
data = {'k1': 1, 'k2': 2} # 其他参数，可以忽略

response = requests.post(url, files=files, data=data)
print(response)


```

# spark任务文件内容

- 设置全局默认编码为utf-8
- 获取spark session
- 获取spark context
- 加载数据并转换成DataFrame
- 从DataFrame创建View
- 提供SparkSQL语句并执行
- 获得分析结果，并将结果给接受方
- 接受方可以是数据库、HTTP接口、等

# 其他

- 当前spark 版本 2.1

# 通过 pip 安装依赖

    pip download tensorflow
    pip dowload -d /path/to/dir -r requirements.txt
    
    pip install --no-index --find-links=file:/offline_package_dir tensorflow
    pip install --no-index --find-links=/path/to/dir -r requirements.txt
    
    
    pip download -d ./pip_packages/ -r requirements.txt
   
# 练习


## 启动spark集群

下面的命令将启动一个master，一个worker

    docker-compose -f docker-compose-spark.yml up -d spark-master spark-worker-1

## 如何提交spark任务

需要在entrypoint.py中提供要执行的spark任务

然后运行 bash run_spark_app.sh

