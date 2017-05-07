import datetime
import time
from calendar import monthrange

if __name__ == "__main__":
    start_date = datetime.date(2017, 3, 1)
    end_date = datetime.date(2017, 3, 2)
    print(type(start_date))
    print('start_date: {}'.format(start_date))
    # total_seconds()
    total_time = (end_date - start_date).total_seconds()
    print('total_time: {}'.format(total_time))

    # datetime.timedelta
    print('datetime.timedelta : {}'.format(datetime.timedelta(hours=28)))

    now = datetime.datetime.now()
    print('now: {}'.format(now))
    yestoday = now - datetime.timedelta(days=1)
    print('yestoday: {}'.format(yestoday))

    # datetime.datetime.combine
    combine_time = datetime.datetime.combine(datetime.date(2017, 3, 1), datetime.time(18, 23, 50))
    print('combine_time: {}'.format(combine_time))

    # strftime ref. http://strftime.org/
    DATETIME_FORMAT = '%m/%d/%Y %I:%M %p'
    format_time = combine_time.strftime(DATETIME_FORMAT)
    print('type: {}'.format(type(format_time)))
    print('method 1 :format_time: {}'.format(format_time))
    print('method 2 :format_time: {:%m/%d/%Y %I:%M %p}'.format(combine_time))
    print('method 3 :format_time: {:{}}'.format(combine_time, DATETIME_FORMAT))

    # monthrange(year, month)
    # Returns weekday of first day of the month and number of days in month, for the specified year and month.
    first_day, num_days = monthrange(2017, 4)
    # 0-6 ~ Mon-Sun
    print('first_day: {}'.format(first_day))
    # number of days in month
    print('num_days: {}'.format(num_days))

    # datetime -> timestamp
    # time.mktime(t)
    # Its argument is the struct_time or full 9-tuple and it returns a floating point number,
    # for compatibility with time().
    timestamp = time.mktime(now.timetuple())
    print('timestamp : {}'.format(timestamp))

    # timestamp -> datetime
    datetime_date = datetime.datetime.fromtimestamp(timestamp)
    print('datetime : {}'.format(datetime_date))
