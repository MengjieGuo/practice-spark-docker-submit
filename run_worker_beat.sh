#!/bin/bash

# 在一个容器中运行多条命令时，需要在命令后面加上 "&" 表示放在后台运行，然后可以继续执行下一条命令

#celery -A lightGateway beat -f /code/worker.log &
#celery worker -A lightGateway --loglevel=info -c 8 -f /code/worker.log &

#celery -A DjangoTaskForSpark beat --scheduler django_celery_beat.schedulers:DatabaseScheduler  &
#celery -A DjangoTaskForSpark beat --scheduler djcelery.schedulers.DatabaseScheduler  &
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# 给worker一个名称，不然在flower里面会有很多历史名称的worker
# --autoreload 自动发现任务 -- old version
# user watchdog to reload
celery worker -A DjangoTaskForSpark --loglevel=info -n worker01 -c 8   &
tail -f /dev/null