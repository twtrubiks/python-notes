# What is the singledispatch in python

[Youtube Tutorial - What is the singledispatch in python](https://youtu.be/09X0OhsAllQ)

這篇文章主要會介紹 `functools` module 中的 singledispatch ，

在介紹之前，建議大家對 decorator 有一些基本的認識，

如果不了解，可參考 [What is the python decorator](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_python_decorator)。

簡單解釋 singledispatch，就是可以將大量的 `if` `elif` `else` 抽出來，

方便之後的維護，可讀性也比較高。

先來看一段很醜的 code，閱讀性差，維護很麻煩 :weary:

[demo1.py](demo1.py)

```python
def fun(arg):
    if not arg:
        print("Nothing.")
        return
    if isinstance(arg, int) or isinstance(arg, float):
        print('hello int or float,', type(arg))
    elif isinstance(arg, list):
        print('hello list')
        for i, elem in enumerate(arg):
            print(i, elem)
    else:
        print('my type:', type(arg))


if __name__ == '__main__':
    fun("Hello, world.")
    fun(123)
    fun(123.3)
    fun([1, 2, 3])
    fun({'a': 2})
    fun(None)
```

程式的部分很簡單，就只是依照不同的 type 輸出不同的結果，

相信你一定會覺得很長，尤其是要判斷的 type 更多時，又要

寫上更多的 `if` `elif` `else`。

所以這時候就可以使用 `functools.singledispatch`，它可以將

大量的 `if` `elif` `else` 抽離出來，來看下面的例子，

[demo2.py](demo2.py)

```python
from functools import singledispatch


@singledispatch # <1>
def fun(arg):
    print('my type:', type(arg))


@fun.register(int) # <3>
@fun.register(float)
def _(arg):
    print('hello int or float,', type(arg))


@fun.register(list) # <2>
def _(arg):
    print('hello list')
    for i, elem in enumerate(arg):
        print(i, elem)


@fun.register(type(None)) # <4>
def nothing(_):
    print("Nothing.")


if __name__ == '__main__':
    fun("Hello, world.")
    # fun(123)
    # fun(123.3)
    # fun([1, 2, 3])
    # fun({'a': 2}) # <5>
    # fun(None)
```

<1> 的部分，先定義一個主要的 function。

<2> 的部分，依照不同的 type 處理對應的事情，這邊注意兩個地方，

第一，有沒有發現 `def _(arg):` 這裡，使用了 `_` ( 可稱它為 dummy )，

因為不需要再定義 function 的名稱，而原來的 `def fun(arg)` function 中

有帶入 arg 參數，記得也要補上去 ( 否則會噴錯 )。

第二，除了這樣寫，也可以這樣表示，如下，

```python
@fun.register # <2>
def _(arg: int):
    print('hello list')
    for i, elem in enumerate(arg):
        print(i, elem)
```

就只是寫法不同而已，可參考 [functools.singledispatch](https://docs.python.org/3/library/functools.html#functools.singledispatch)。

<3> 的部分，也就是可以同時註冊多個 type，像這邊代表如果是 `int` 或 `float` 都會成立。

<4> 的部分，也就是當傳入 `None` 的情形，像是 `fun(None)`，注意 `def nothing(_):`

這裡，我寫了 `_`，也可以寫 `arg`，雖然沒有用到參數，但還是要填，不然會噴錯。

<5> 的部分，雖然我們沒有處理到 `dict` 的情境，但在這情況下，它會去執行原本的 function，

也就是 `def fun(arg):`，並且印出 `my type: <class 'dict'>`，如果需要加上 `dict`，

就再寫一個 `@fun.register` 即可。

相信大家一定覺得這樣整體乾淨不少，維護性以及可讀性都有提高 :smile:

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡 :laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
