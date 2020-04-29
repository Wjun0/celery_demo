import logging
import os


class My_log(object):
    logg = logging.getLogger(__name__)
    logg.setLevel(logging.INFO)
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    from logging.handlers import RotatingFileHandler
    fh = RotatingFileHandler(filename=path + '/test.log',
                             mode='a',
                             maxBytes=100 * 1024 * 1024,  #每个日志文件100
                             backupCount=5,
                             encoding='utf8')
    # fh = logging.FileHandler(path + '/my_log/test.log', mode='a')
    fh.setLevel(logging.INFO)

    log_format = logging.Formatter('%(asctime)s %(filename)s %(lineno)s %(levelname)s %(message)s')
    fh.setFormatter(log_format)

    logg.addHandler(fh)



if __name__ == '__main__':
    log = My_log()
    log.logg.error('这是一个错误信息')