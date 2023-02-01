from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime

if __name__ == "__main__":
    '''
    ref. http://dateutil.readthedocs.io/en/stable/parser.html
    '''
    print(parse('2017/4  /4 4:00:00 PM '))
    print(parse('2017/4  -4 16:00:00  '))

    '''
    ref. https://dateutil.readthedocs.io/en/stable/relativedelta.html
    '''
    now = datetime.now()
    now_plus_1_month = now + relativedelta(months=+1)
    now_minus_1_month = now + relativedelta(months=-1)
    print('now', now)
    print('now_plus_1_month', now_plus_1_month)
    print('now_minus_1_month', now_minus_1_month)
