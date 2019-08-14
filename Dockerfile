FROM bde2020/spark-submit:2.4.1-hadoop2.7

MAINTAINER Mengjie Guo <xxxx@xxx.com>


# Copy the requirements.txt first, for separate dependency resolving and downloading
COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
    #&& \
    #pip install psycopg2-binary  -i https://mirrors.aliyun.com/pypi/simple/
# Copy the source code
#COPY . /app

#COPY template.sh /
#CMD ["/bin/bash", "/template.sh"]

#（默认值：spark-master）
#ENV SPARK_MASTER_NAME spark-master
# （默认值：7077）
#ENV SPARK_MASTER_PORT 7077
# （默认：/app/app.py）

# Set spark-submit's task file path
# PYSPARK_PYTHON=python3 /spark/bin/spark-submit \
#            --master ${SPARK_MASTER_URL} \
#            ${SPARK_SUBMIT_ARGS} \
#            ${SPARK_APPLICATION_PYTHON_LOCATION} ${SPARK_APPLICATION_ARGS}
ENV SPARK_APPLICATION_PYTHON_LOCATION /app/entrypoint.py
#ENV SPARK_APPLICATION_ARGS "foo bar baz"

