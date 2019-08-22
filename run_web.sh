#!/bin/bash

# 在一个容器中运行多条命令时，需要在命令后面加上 "&" 表示放在后台运行，然后可以继续执行下一条命令

#[watcher:integrity_assessment]
#cmd = gunicorn --workers=8 --threads=8 --bind 0.0.0.0:8000 --max-requests 2000 --timeout 30 --access-logfile web_access.log integrity_assessment.wsgi
#working_dir = /code
#copy_env = True
#send_hup = True

gunicorn --bind 0.0.0.0:8000 --max-requests 2000 --timeout 30 --access-logfile web_access.log DjangoTaskForSpark.wsgi