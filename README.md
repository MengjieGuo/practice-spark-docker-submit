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

