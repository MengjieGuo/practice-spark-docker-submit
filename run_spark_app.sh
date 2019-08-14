#!/bin/bash

#docker run --name my-spark-app \
#    --rm \
#    -e SPARK_MASTER_NAME=192.168.1.175 \
#    -e SPARK_MASTER_PORT=7077 \
#    -e ENABLE_INIT_DAEMON=false \
#    -v /Users/screwman/Docker/DjangoTaskForSpark/entrypoint.py:/app/entrypoint.py bde/spark-app

#     --link spark-master:spark-master \

docker-compose -f docker-compose-spark.yml stop spark-app-1
docker rm -f spark-app-1
docker-compose -f docker-compose-spark.yml up spark-app-1