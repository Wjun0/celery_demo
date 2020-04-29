#pip install flower   启动可以在浏览器查看哪些任务成功了，哪些失败了
#启动任务前可以使用celery -A my_celery.main flower，查看哪些失败了，哪些成功了


def run():
    # 调用celery任务
    # from my_celery.celery1.tasks import t1
    # t1.delay(2, 2)     #apply_async的快捷调用

    from my_celery.celery1.tasks import add1
    r1 = add1.delay(6,6)
    print(r1.get())

    from my_celery.celery2.tasks import t2
    rr = t2.apply_async((3,3),link=t2.s(3))  # link 的作用，先将3和3进行运算，然后再将结果与4进行运算
    print(rr.get())

    from my_celery.celery1.tasks import t1
    # t1.apply_async((2,2),link=[t1.s(3),t2.s(100)])   #将apply_async的结果分别与link的结果进行运算


    from celery import chain
    ret = chain(t1.s(2,3),t1.s(4),t1.s(5))()   #将t1的结果运用链式返回，注意第二个参数调用少一个值  结果：2*3*4*5
    print(ret.get())

    from celery import group
    r1 = group(t1.s(i,i) for i in range(3))()  #返回的是一个列表，每个t1运行的结果
    print(r1.get())

    job = group([t1.s(2,3),t2.s(2,3),t1.s(4,5)])   #group的其他使用方法
    ret = job.apply_async()
    print(ret.ready())              #判断是否准备完成
    print(ret.successful())         #判断是否成功
    print(ret.completed_count())    #返回成功的子任务数量
    print(ret.get())                #返回的结果

    # from celery import chord
    # r2 = chord((t2.s(i,i) for i in range(4)),xsum.s())()
    # print(r2.get())
    # from my_celery.celery3.tasks import t3
    # t3.delay(6,6)



if __name__ == '__main__':
    import time
    start = time.time()
    run()
    print(time.time() - start)

