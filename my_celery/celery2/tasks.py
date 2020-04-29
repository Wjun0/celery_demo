from my_celery.main import app
import time

@app.task(bind=True)
def t2(self,a,b):
    # print(args)
    print("++++++++++",a + b)
    time.sleep(5)
    print("t2 end")
    print(self.request.id)
    return a+b