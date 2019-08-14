FROM  bde/spark-app

MAINTAINER Mengjie Guo <xxxx@xxx.com>



RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev
#    && \
#    pip3 install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple/ && \
#    pip3 install psycopg2 -i https://mirrors.aliyun.com/pypi/simple/

# Set spark-submit's task file path
# PYSPARK_PYTHON=python3 /spark/bin/spark-submit \
#            --master ${SPARK_MASTER_URL} \
#            ${SPARK_SUBMIT_ARGS} \
#            ${SPARK_APPLICATION_PYTHON_LOCATION} ${SPARK_APPLICATION_ARGS}
#ENV SPARK_APPLICATION_PYTHON_LOCATION /app/entrypoint.py
#ENV SPARK_APPLICATION_ARGS "foo bar baz"
