# freezegun (https://github.com/spulec/freezegun)
# pip3 install freezegun

from freezegun import freeze_time
import datetime
import time

# Decorator
@freeze_time("2021-10-10")
def example_1():
    assert datetime.datetime.now() == datetime.datetime(2021, 10, 10)

# Context manager
def example_2():
    assert datetime.datetime.now() != datetime.datetime(2021, 10, 10)
    with freeze_time("2021-10-10"):
        assert datetime.datetime.now() == datetime.datetime(2021, 10, 10)
    assert datetime.datetime.now() != datetime.datetime(2021, 10, 10)

# Raw use
def example_3():
    freezer = freeze_time("2021-10-10 10:00:00")
    freezer.start()
    assert datetime.datetime.now() == datetime.datetime(2021, 10, 10, 10, 0, 0)
    freezer.stop()
    assert datetime.datetime.now() != datetime.datetime(2021, 10, 10, 10, 0, 0)

# tick argument
@freeze_time("2021-10-10", tick=True)
def example_4():
    print(datetime.datetime.now()) # 2021-10-10 00:00:00
    time.sleep(5)
    assert datetime.datetime.now() > datetime.datetime(2021, 10, 10)
    print(datetime.datetime.now()) # 2021-10-10 00:00:05

# auto_tick_seconds
@freeze_time("2021-10-10", auto_tick_seconds=15)
def example_5():
    print(datetime.datetime.now()) # 2021-10-10 00:00:00
    print(datetime.datetime.now()) # 2021-10-10 00:00:15

if __name__ == '__main__':
    example_1()
    # example_2()
    # example_3()
    # example_4()
    # example_5()




