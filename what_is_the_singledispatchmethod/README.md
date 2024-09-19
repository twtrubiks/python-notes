# What is the singledispatchmethod in python

這篇文章主要會介紹 `functools` module 中的 `singledispatchmethod`

前面介紹過 [What is the singledispatch in python](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_singledispatch),

回顧一下, 假設今天把 `singledispatch` 放進去 class 中會發生什麼事情 ❓

[demo1.py](demo1.py)

```python
from functools import singledispatch

class A:

    @singledispatch
    def fun(self, arg):
        print('my type:', type(arg))


    @fun.register(int)
    @fun.register(float)
    def _(self, arg):
        print('hello int or float,', type(arg))


    @fun.register(list)
    def _(self, arg):
        print('hello list')
        for i, elem in enumerate(arg):
            print(i, elem)


    @fun.register(type(None))
    def nothing(self, _):
        print("Nothing.")


if __name__ == '__main__':
    a = A()
    a.fun(123)
    # 正確應該要輸出 hello int or float, <class 'int'>
    # 但這邊卻輸入 my type: <class 'int'>
    # 代表 singledispatch 沒有生效
```

你會發現 `singledispatch` 在 class 中沒有正常的生效.

這時候必須修改成 `singledispatchmethod`,

[demo2.py](demo2.py)

```python
"""
ref:
https://docs.python.org/3.12/library/functools.html#functools.singledispatchmethod

the dispatch happens on the type of the first non-self or non-cls argument
"""

from functools import singledispatchmethod

class A:

    @singledispatchmethod
    def fun(self, arg):
        print('my type:', type(arg))


    @fun.register(int)
    @fun.register(float)
    def _(self, arg):
        print('hello int or float,', type(arg))


    @fun.register(list)
    def _(self, arg):
        print('hello list')
        for i, elem in enumerate(arg):
            print(i, elem)


    @fun.register(type(None))
    def nothing(self, _):
        print("Nothing.")


if __name__ == '__main__':
    a = A()
    a.fun(123) # 有正確輸出 hello int or float, <class 'int'>
```

你會發現正確輸出了.

所以如果使用 class 就必須使用 `singledispatchmethod`, `singledispatch` 在 class 中沒作用 ❗

除了基本的 `int` `float` `str` ... 這些之外, 也可以使用 `class`,

下面的範例就是依照對應的 class 顯示 DATA1 或 DATA2

[demo3.py](demo3.py)

```python
from functools import singledispatchmethod

class DATA1:
    def show(self):
        print("DATA1")

class DATA2:
    def show(self):
        print("DATA2")

class A:

    @singledispatchmethod
    def fun(self, arg):
        raise NotImplementedError()


    @fun.register(DATA1)
    def _(self, arg):
        arg.show()


    @fun.register(DATA2)
    def _(self, arg):
        arg.show()


    @fun.register(type(None))
    def nothing(self, _):
        print("Nothing.")

if __name__ == '__main__':

    data1 = DATA1()
    data2 = DATA2()
    a = A()
    a.fun(data1) # DATA1
    a.fun(data2) # DATA2
    a.fun(None) # Nothing.
```

衍生閱讀, 其實這個和 [match_case_tutorial.py](https://github.com/twtrubiks/python-notes/blob/master/match_case_tutorial.py) 的概念有點類似,

都是不想寫很醜的 if...else...

除了這樣的定義方式之外, 還記得 [PEP 484 Type Hints 介紹](https://github.com/twtrubiks/python-notes/tree/master/type-hints-tutorial) 這個嗎 ❓

`singledispatchmethod` 也可以用這個方式來定義,

[demo4.py](demo4.py)

```python
from functools import singledispatchmethod

class DATA1:
    def show(self):
        print("DATA1")

class DATA2:
    def show(self):
        print("DATA2")

class A:

    @singledispatchmethod
    def fun(self, arg):
        raise NotImplementedError()


    @fun.register
    def _(self, arg: DATA1):
        arg.show()


    @fun.register
    def _(self, arg: DATA2):
        arg.show()


    @fun.register
    def nothing(self, _: None):
        print("Nothing.")

if __name__ == '__main__':
    data1 = DATA1()
    data2 = DATA2()
    a = A()
    a.fun(data1) # DATA1
    a.fun(data2) # DATA2
    a.fun(None) # Nothing.
```