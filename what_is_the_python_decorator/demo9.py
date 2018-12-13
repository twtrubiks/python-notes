registry = dict()


def route(rule):
    def decorator(f):
        registry[rule] = f
        return f

    return decorator


@route('/')
def index():
    print('hello')
    return 'hello'


index()
print('registry:', registry)
