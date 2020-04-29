from my_celery.main import app
import time
@app.task
def t1(a,b):
    # print(args)
    time.sleep(5)
    print("++++++++++",a * b)
    print("t1 end")
    return a*b

import celery
class MyTask(celery.Task):
    def on_failure(self, exc, task_id, args, kwargs, einfo):
        print("{0!r} failed: {1!r}'.format(task_id, exc)")



@app.task(base=MyTask)
def add(x,y):
    raise KeyError()

@app.task()
def add1(x,y):
    print('x + y = ')
    return x + y
