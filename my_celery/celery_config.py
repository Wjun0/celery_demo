from kombu import Queue
# 指定rabbitmq作为celery的队列
# broker_url= 'amqp://guest:guest@127.0.0.1:5672'
broker_url = 'redis://192.168.59.129:6379/1'  #中间人选择，可以是rabbitmq，也可以是redis
result_backend = 'redis://192.168.59.129:6379/2'  # 执行结果的存储，如果需要将执行结果返回就必须配置

task_queues = (
    Queue(name='t1_queue',routing_key='t1_router'), #celery -A my_celery.main worker -l info -Q t1_queue -P eventlet
    Queue(name='t2_queue',routing_key='t2_router')  #可以使用多个队列启动，-P 是使用evenlet 启动，防止windows下运行出错
)

task_routes = ([    #celery4.4 配置方式使用元组嵌套列表的方式。
    ('my_celery.celery1.tasks.*',{      #*号可以将该路由下的所有任务都使用同一个队列处理。
        "queue":'t1_queue',
        'routing_key':'t1_router'
    }),
    ('my_celery.celery2.tasks.t2',{
        "queue":"t2_queue",
        "routing_key":'t2_router'
    })
],)