from my_celery.main import app


from my_celery.log_config import My_log
wj_log = My_log()



@app.task(bind=True)
def t3(self,a,b):
    # print(args)

    wj_log.logg.error('wj_log')
    return a+b