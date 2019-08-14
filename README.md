# practice-spark-docker-submit


## 启动spark集群

下面的命令将启动一个master，一个worker

docker-compose -f docker-compose-spark.yml up -d spark-master spark-worker-1

## 如何提交spark任务

需要在entrypoint.py中提供要执行的spark任务

然后运行 bash run_spark_app.sh
