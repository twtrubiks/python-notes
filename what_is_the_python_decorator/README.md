# What is the python decorator

[Youtube Tutorial - What is the python decorator - part1](https://youtu.be/WtNh_-okV04)

[Youtube Tutorial - What is the python decorator - part2](https://youtu.be/JNxtI-thX_w)

[Youtube Tutorial - What is the python decorator - part3](https://youtu.be/f4BG_MBXF2Q)

[Youtube Tutorial - What is the python decorator - part4](https://youtu.be/79QK-LI-P10)

這篇文章主要會介紹 decorator，一直沒有好好的介紹一下:sweat_smile:

在開始介紹 decorator 前，要先有一個觀念，就是在 python 中，

我們可以將 function 如同參數一樣傳遞，

[demo1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo1.py)

```python
def f1():
    print("f1")


def register(func):
    func()


register(f1)
```

裝飾器就是站在這個基礎上去延伸出來的。

接著來說說什麼時候要用裝飾器，裝飾器最主要的目的是在不破壞 function 或 class 的情況下，

去擴充目標 function 或 class 的功能。

例如，logging、計算 function or class 執行的時間、權限等等。

如果大家有興趣，可以再去查查 AOP ( Aspect Oriented Programming )，中文翻成 面向切面。

有了這個裝飾器，我們就可以將大量的程式碼抽出來( 與函數本身無關的部分 )，將這些 code

寫到裝飾器中 ( 可以重複使用 )，程式碼也不會變得很亂。

說穿了，就是在現在的功能上，可以加上額外的功能 ( 重點是不破壞原有的 code )。

舉個例子，今天我想要紀錄 `f1()` 的 logging，我們可能這樣寫，

( 正常來說，應該要使用 `logging` 這個 module，但這邊簡單用 print 代替就好 :smile:)

```python
def f1():
    print("f1")
    print("logging - f1 is running")

f1()
```

這樣寫看似沒有問題，但如果你今天 `f2()` `f3()` `f4()` 都需要紀錄呢 :question:

這樣要每一個都寫一樣的 code :question:

我們能不能把它抽出來 :question: 而這個東西，就是專門處理 logging 的，

答案當然是可以的:smile:

[demo2.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo2.py)

```python
def my_logging(func):
    print('logging - {} is running'.format(func.__name__))
    func()


def f1():
    print("f1")


my_logging(f1)
```

功能實現了，看似很美好，如果有其他的需要加上 logging，使用 `my_logging(f2)` 即可。

但這方法其實有一些問題，問題點在每次都要呼叫 my_logging，而且也要將 f1 當成參數傳遞，

比較好的方法應該是維持 f1 為主要業務邏輯，而不是像現在變成 my_logging 為主要業務邏輯，

也就是說，現在的狀況破壞了原有代碼的結構。

所以更好的方法，就是使用裝飾器 ( 我們終於談到主角了:smile:)

來看一個簡單的裝飾器，

[demo3.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo3.py)

```python
def my_logging(func):
    def wrapper():
        print('logging - {} is running'.format(func.__name__))
        func()  # run func()  Equivalent run f1()

    return wrapper


def f1():
    print("f1")


f1 = my_logging(f1)  # Equivalent -> f1 = wrapper
f1()  # Equivalent -> f1() = wrapper()
```

my_logging 就是一個裝飾器，把真正的業務邏輯 func 包在裡面，看起來就像是 func 被 my_logging

裝飾了一樣，所以顧名思義，稱為裝飾器。

在這個範例中，函數的進入和退出時，都可以加上東西，這種方式也稱為 AOP ( Aspect Oriented Programming )。

接下來要來談談 `@` 這個符號，你可以把他想成是一種語法的符號，透過這個符號，可以將 [demo3.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo3.py) 簡略，

[demo4.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo4.py)

```python
def my_logging(func):
    def wrapper():
        print('logging - {} is running'.format(func.__name__))
        func()  # run func()  Equivalent run f1()

    return wrapper


@my_logging
def f1():
    print("f1")


f1()
```

當有了 `@` 這個語法的幫忙，就可以將 `f1 = my_logging(f1)` 省略，直接使用 `f1()` 即可。

[Youtube Tutorial - What is python decorator - part2](https://youtu.be/JNxtI-thX_w)

當然，我們也可以同時使用多個裝飾器，[demo4_1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo4_1.py)

```python
def my_logging(func):
    def wrapper():
        print('logging - {} is running'.format(func.__name__))
        func()  # run func()  Equivalent run f1()

    return wrapper


def bold(func):
    def wrapper():
        print("<b>")
        func()
        print("</b>")

    return wrapper


def italic(func):
    def wrapper():
        print("<i>")
        func()
        print("</i>")

    return wrapper


@my_logging
@bold
@italic
def f1():
    print("f1")


f1()
```

其實上面這段 code 也相當於 [demo4_2.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo4_2.py)

```python
def my_logging(func):
    def wrapper():
        print('logging - {} is running'.format(func.__name__))
        func()  # run func()  Equivalent run f1()

    return wrapper


def bold(func):
    def wrapper():
        print("<b>")
        func()
        print("</b>")

    return wrapper


def italic(func):
    def wrapper():
        print("<i>")
        func()
        print("</i>")

    return wrapper


def f1():
    print("f1")


f1 = my_logging(bold(italic(f1)))
f1()

```

這邊只需要稍微注意一下執行的順序:smile:

剛剛的 `f1()` 是沒有帶入參數的，今天假如我希望帶入參數呢:question:

[demo5.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo5.py)

```python
def my_logging(func):
    def wrapper(*args, **kwargs):
        print('logging - {} is running'.format(func.__name__))
        func(*args, **kwargs)

    return wrapper


@my_logging
def f1(*args, **kwargs):
    print("f1")

    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
```

這樣寫的話，不管 `f1()` 帶入什麼參數都不用擔心:smile:

關於 `**kwargs` 和 `*arg` 的範例，可參考 [What is the **kwargs *args](https://youtu.be/UwhbFxLADmE)。

裝飾器還有更大的彈性，像是今天如果我希望將裝飾器帶入參數，

[demo6.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo6.py)

```python
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
```

這邊簡單說明，就是為了要將裝飾器帶入參數，我們必須再包一層。

( 這邊可以把它想成是 closures 閉包的概念，可參考 [What is the closures in python](https://github.com/twtrubiks/fluent-python-notes/tree/master/what_is_the_closures) )

[Youtube Tutorial - What is the python decorator - part3](https://youtu.be/f4BG_MBXF2Q)

接下來要來談談 `functools.wraps` 的功用，雖然使用裝飾器可以大大的減少重複的 code，

但是他有一個缺點，就是你會發現 `f1` function 中的 name 和 doc 結果會怪怪的，

以下的例子，

[demo7.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo7.py)

```python
def my_logging(func):
    def wrapper(*args, **kwargs):
        """my wrapper"""
        print('logging - {} is running'.format(func.__name__))
        func(*args, **kwargs)

    return wrapper


@my_logging
def f1(*args, **kwargs):
    """f1 function"""
    print("f1")

    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
print('f1.__name__', f1.__name__)  # output -> 'wrapper'
print('f1.__doc__', f1.__doc__)  # output -> 'my wrapper'
```

將 `f1.__name__` 以及 `f1.__doc__` 印出來，竟然出現了 `wrapper` 的東西，

( 也就是說，`f1` 被 `wrapper` 取代了，所以才顯示 `wrapper` 的資訊 )

所以為了解決這個問題，可以使用 `functools.wraps` 這個裝飾器，將原本函數裡面

的資訊複製到 `func` 之中，這樣就會讓 `func` 也有原函數 `f1` 的資訊。

方法如下，

[demo7_1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo7_1.py)

```python
from functools import wraps


def my_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """my wrapper"""
        print('logging - {} is running'.format(func.__name__))
        func(*args, **kwargs)

    return wrapper


@my_logging
def f1(*args, **kwargs):
    """f1 function"""
    print("f1")

    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
print('f1.__name__', f1.__name__)  # output -> 'f1'
print('f1.__doc__', f1.__doc__)  # output -> 'f1 function'
```

這樣子就可以正確的顯示 `f1` 的資訊了。

裝飾器除了 function 之外, 也可以是 class，

class decorator 主要是依賴 `__call__` 的方法，可參考 [What is the `__call__` in python](https://youtu.be/YIstPYG15IA)。

[demo8.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo8.py)

這個範例是**裝飾器沒有帶參數**的，

```python
class MyDecorator:
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        print('do something before calling function {}'.format(self.__func.__name__))
        self.__func(*args, **kwargs)
        print('do something after calling function {}'.format(self.__func.__name__))


@MyDecorator
def f1(*args, **kwargs):
    print('f1')
    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')

# @MyDecorator Equivalent
# f1 = MyDecorator(f1)
# f1('twtrubiks', apple='fruit', cabbage='vegetable')
```

[demo8_1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo8_1.py)

這個範例是**裝飾器有帶參數**的，

```python
class MyDecorator:
    def __init__(self, param):
        self.__param = param

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('do something before calling function {}'.format(func.__name__))
            print('self.__param', self.__param)
            func(*args, **kwargs)
            print('do something after calling function {}'.format(func.__name__))

        return wrapper


@MyDecorator('level')
def f1(*args, **kwargs):
    print('f1')
    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
```

看起來稍微比較複雜，但其實就是 closures 閉包的概念。

[Youtube Tutorial - What is the python decorator - part4](https://youtu.be/79QK-LI-P10)

裝飾器還有一個神奇的功能，就是用裝飾器來註冊函數，

先來看一個 flask 框架中常常用來註冊 url 的方法，

相信如果寫過 flask 的人，一定對下面這段 code 不陌生，

```python
@app.route("/")
def index():
    pass
```

但是你有想過，他是怎麼辦到的嗎:question:

其實就是利用了我剛剛說的另外一個特性，用裝飾器來註冊函數。

不太懂意思，沒關係，來看一個例子，

[demo9.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_python_decorator/demo9.py)

以下的 code 是我從 flask 中的 source code 精簡來的，如果大家有興趣，可以自行到 [flask app.py](https://github.com/pallets/flask/blob/master/flask/app.py) 查看，

主要看 `route` 以及 `add_url_rule` 這兩個方法，

```python
registry = dict()

def route(rule):
    def decorator(f):
        registry[rule] = f # <1>
        return f

    return decorator


@route('/')
def index():
    print('hello')
    return 'hello'

index()
print('registry:', registry) # <2>
```

重點在 <1> 的部分，我們只是將 rule 以及 f 註冊到 registry，然後

再 return 原本的 function ( 沒經過任何加工，只單純註冊 url )，

如果你觀察 <2> 的輸出，你也會發現 registry 裡面有 url 的 mapping。

所以裝飾器除了裝飾 ( 擴充 ) 原本的功能之外，還有註冊函數的功用。

## 結論

介紹到這邊差不多該告一段落了:relaxed:未來會再補充幾個常用的裝飾器，

* property - [What is the property in python](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_property)

* classmethod and staticmethod - [What is the classmethod and staticmethod in python](https://github.com/twtrubiks/python-notes/tree/master/what_is_classmethod_and_staticmethod)

以及在 `functools` module 中，比較實用的裝飾器，

* functools.wraps - 本篇文章已經介紹過了

* functools.lru_cache - [What is the functools.lru_cache in python](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_functools.lru_cache)

* functools.singeldispatch - [what_is_the_singledispatch](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_singledispatch)

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
