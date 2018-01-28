import logging

'''
ref. https://docs.python.org/3.6/howto/logging.html
Level , DEBUG < INFO < WARNING < ERROR < CRITICAL
'''


def ex1():
    # ex1
    # will print 'warning message' , 'error message', because the default level is WARNING
    logging.warning('warning message')
    logging.error('error message')
    logging.debug('I told you so - debug')
    logging.info('I told you so - info')


def ex2():
    # ex 2
    # will print all message , because the level is DEBUG
    format_log = '%(asctime)s %(levelname)s:%(message)s'
    logging.basicConfig(filename='example.log', format=format_log, level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')


if __name__ == "__main__":
    ex1()
    # ex2()
