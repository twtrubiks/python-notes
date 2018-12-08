# decorator

[Youtube Tutorial - What is python decorator - part1](XXX)

[Youtube Tutorial - What is python decorator - part2](XXX)

這篇文章主要會介紹 decorator，一直沒有來好好的來介紹一下:sweat_smile:

在開始介紹 decorator 前，要先有一個觀念，就是在 python 中，

我們可以將 function 如同參數一樣傳遞，

[demo1.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo1.py)

```python
def f1():
    print("f1")


def register(func):
    func()


register(f1)
```

裝飾器就是站在這個基礎上去延伸出來的。

接著來說說什麼時候要用裝飾器，裝飾器主要的目的是在不破壞 function 或 class 的情況下，

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

[demo2.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo2.py)

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

[demo3.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo3.py)

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

接下來要來談談 `@` 這個符號，你可以把他想成是一種語法的符號，透過這個符號，可以將 [demo3.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo3.py) 簡略，

[demo4.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo4.py)

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

當然，我們也可以同時使用多個裝飾器，[demo4_1.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo4_1.py)

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

其實上面這段 code 也相當於 [demo4_2.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo4_2.py)

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

我們在 `f1()` 完全不修改的情況下 ( 只需要加上裝飾器 )，就可以擴充這個函數的功能，

未來如果有同樣的需求，也只需要加上裝飾器即可。

這樣一來，大大提高了程式的重複使用性，也增加了維護以及可讀性。

[Youtube Tutorial - What is python decorator - part2](XXX)

剛剛的 `f1()` 是沒有帶入參數的，今天假如我希望帶入參數呢:question:

[demo5.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo5.py)

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

關於 `**kwargs` 和 `*arg` 著範例，可參考 [**kwargs , *arg tutorial](https://github.com/twtrubiks/python-notes/blob/master/kwargs.py)。

裝飾器還有更大的彈性，像是今天如果我希望將裝飾器帶入參數，

[demo6.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo6.py)

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

( 這邊是 closures 閉包的概念 )

接下來要來談談 `functools.wraps` 的功用，雖然使用裝飾器可以大大的減少重複的 code，

但是他有一個缺點，就是你會發現 `f1` function 中的 name 和 doc 結果會怪怪的，

以下的例子，

[demo7.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo7.py)

```python
def my_logging(func):
    def wrapper(*args, **kwargs):
        """my wrapper"""
        print('logging - {} is running'.format(func.__name__))
        func(*args, **kwargs)

    return wrapper


@my_logging
def f1(*args, **kwargs):
    """write logging"""
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

[demo7_1.py](https://github.com/twtrubiks/python-notes/blob/master/decorator_tutorial/demo7_1.py)

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
    """write logging"""
    print("f1")

    for thing in args:
        print('hello {}'.format(thing))

    for name, value in kwargs.items():
        print('{0} = {1}'.format(name, value))


f1('twtrubiks', apple='fruit', cabbage='vegetable')
print('f1.__name__', f1.__name__)  # output -> 'f1'
print('f1.__doc__', f1.__doc__)  # output -> 'write logging'
```

這樣子就可以正確的顯示 `f1` 的資訊了。

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
