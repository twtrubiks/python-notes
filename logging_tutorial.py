import logging

'''
ref. https://docs.python.org/3/library/logging.html
Level DEBUG < INFO < WARNING < ERROR < CRITICAL
'''


def ex1():
    # logging.basicConfig(level=logging.DEBUG)
    # will print 'warning message' , 'error message', because the default level is WARNING
    logging.warning('warning message')
    logging.error('error message')
    logging.debug('I told you so - debug')
    logging.info('I told you so - info')


def ex2():
    logging.error('test')
    log1 = logging.getLogger('my_app')
    log2 = logging.getLogger(__name__)
    log1.warning('I told you')
    log2.warning('warning message')


def ex3():
    # will print all message , because the level is DEBUG
    format_log = '%(asctime)s %(levelname)s:%(message)s'
    logging.basicConfig(filename='example.log', format=format_log, level=logging.DEBUG)
    # logging.basicConfig(format=format_log, level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')


def ex4():
    # multiple-handlers-and-formatter
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    log_file = 'my_test_logger.log'
    f_log = logging.FileHandler(log_file, mode='w')
    f_log.setLevel(logging.ERROR)

    # 設定 console 並且定義為 DEBUG
    c_log = logging.StreamHandler()
    c_log.setLevel(logging.DEBUG)

    format_log = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_log.setFormatter(format_log)
    c_log.setFormatter(format_log)

    logger.addHandler(f_log)
    logger.addHandler(c_log)

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == "__main__":
    # ex1()
    # ex2()
    # ex3()
    ex4()
