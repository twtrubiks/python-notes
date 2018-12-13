def my_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "1":
                print('level {} logging - {} is running'.format(level, func.__name__))
            elif level == "2":
                print('level {} logging - {} is running'.format(level, func.__name__))

            func(*args, **kwargs)

        return wrapper

    return decorator


@my_logging(level="1")
def f1(*args, **kwargs):
    print("f1")

    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
