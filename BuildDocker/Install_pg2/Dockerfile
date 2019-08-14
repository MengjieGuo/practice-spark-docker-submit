FROM  bde/spark-app-2

MAINTAINER Mengjie Guo <xxxx@xxx.com>



RUN apk add  python3-dev && \
    pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/ && \
    pip3 install psycopg2-binary -i https://mirrors.aliyun.com/pypi/simple/

# Set spark-submit's task file path
# PYSPARK_PYTHON=python3 /spark/bin/spark-submit \
#            --master ${SPARK_MASTER_URL} \
#            ${SPARK_SUBMIT_ARGS} \
#            ${SPARK_APPLICATION_PYTHON_LOCATION} ${SPARK_APPLICATION_ARGS}
#ENV SPARK_APPLICATION_PYTHON_LOCATION /app/entrypoint.py
#ENV SPARK_APPLICATION_ARGS "foo bar baz"
