
from celery import Celery
app = Celery('wj')

# 加载配置
app.config_from_object('my_celery.celery_config')

# 加载可用的任务
app.autodiscover_tasks([
    'my_celery.celery1',
    'my_celery.celery2',
    'my_celery.celery3'
])