# 什麼是 abstractmethod

[Youtube Tutorial - 什麼是 abstractmethod in python](https://youtu.be/G-W_F9Sblj4)

這篇文章主要會介紹 abstractmethod,

Abstract Base Class 又簡稱 ABC.

它被定義在 [PEP 3119](https://www.python.org/dev/peps/pep-3119/) (詳細說明也可以看這裡).

一步一步帶大家慢慢了解, 先來看一個例子,

[demo1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_abstractmethod/demo1.py)

```python
class A:

    def action1(self):
        raise NotImplemented

    def action2(self):
        raise NotImplemented

class B(A):
    pass

b = B()

# 沒有使用 abstractmethod 不一定要實作 action1, action2
# (這句話可以先忽略, 因為你看到後面就會懂了)

b.action1()
# raise NotImplemented
```

當你執行 [demo1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_abstractmethod/demo1.py) 的時候, 可以成功的實例化 b,

但執行到 `b.action1()` 會跳出 `raise NotImplemented` 錯誤.

修正方法很簡單, 就是把他實作即可, 請參考 [demo1_fix.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_abstractmethod/demo1_fix.py)

```python
class A:

    def action1(self):
        raise NotImplemented

    def action2(self):
        raise NotImplemented

class B(A):
    def action1(self):
        print('hello action1')

    def action2(self):
        pass

b = B()

# 沒有使用 abstractmethod 不一定要實作 action1, action2
# (這句話可以先忽略, 因為你看到後面就會懂了)

b.action1()
b.action2()
```

一般來說, 這樣使用沒甚麼問題, 但有沒有更嚴謹的使用方式呢:question:

有沒有在實例化的時候就去檢查是否都有正確實作了, 而不是等到去呼叫時, 才發現沒有實作.

答案是有的:smile: 透過 abstractmethod,

請看 [demo2.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_abstractmethod/demo2.py)

```python
import abc


# class A(metaclass=abc.ABCMeta):
class A(abc.ABC):

    @abc.abstractmethod
    def action1(self):
        pass

    @abc.abstractmethod
    def action2(self):
        pass

class B(A):
    pass

# 有使用 abstractmethod 一定要實作 action1, action2
b = B()
# TypeError: Can't instantiate abstract class B with abstract methods action1, action2

```

首先, 你想用以下哪種方式定義 class 都可以

```python
......
class A(metaclass=abc.ABCMeta):
    pass
......
```

或

```python
......
class A(abc.ABC):
    pass
......
```

然後透過 `@abc.abstractmethod` 這個裝飾器即可.

當你執行 [demo2.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_abstractmethod/demo2.py) 時,

你會發現, 當你在實例化, 也就是執行到 `b = B()` 這段程式時,

就會跳出以下錯誤訊息,

`TypeError: Can't instantiate abstract class B with abstract methods action1, action2`

錯誤訊息說的很清楚, 你必須實作 abstract methods.

修正方法很簡單, 就把有加上 `@abc.abstractmethod` 的部份實作好即可:smile:

修正後如下 [demo2_fix.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_abstractmethod/demo2_fix.py)

```python
import abc


# class A(metaclass=abc.ABCMeta):
class A(abc.ABC):

    @abc.abstractmethod
    def action1(self):
        pass

    @abc.abstractmethod
    def action2(self):
        pass

class B(A):
    def action1(self):
        print('hello action1')

    def action2(self):
        pass

# 有使用 abstractmethod 一定要實作 action1, action2
b = B()
b.action1()
b.action2()

```

這樣子可能有人會問, `abstractmethod` 可以搭配 `staticmethod` 和 `classmethod` 使用嗎:question:

[介紹 classmethod and staticmethod in python](https://github.com/twtrubiks/python-notes/tree/master/what_is_classmethod_and_staticmethod)

是可以的:smile:

請參考 [demo3.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_abstractmethod/demo3.py)

```python
import abc


# class A(metaclass=abc.ABCMeta):
class A(abc.ABC):

    # abc.abstractmethod 請放在最內層
    @staticmethod
    @abc.abstractmethod
    def action1(x, y):
        pass

    # abc.abstractmethod 請放在最內層
    @classmethod
    @abc.abstractmethod
    def action2(cls, x, y):
        pass

    @abc.abstractmethod
    def display(self):
        pass

class B(A):

    @staticmethod
    def action1(x, y):
        print('hello action1')
        print('x', x)
        print('y', y)

    @classmethod
    def action2(cls, x, y):
        print('hello action2', cls)
        print('x', x)
        print('y', y)
        return cls()

    def display(self):
        print('hello display')


B.action1('x1', 'y1')
B.action2('x2', 'y2').display()

```

請注意裝飾器的堆疊順序, 很重要:exclamation::exclamation: `@abc.abstractmethod` 需要放在最內層.

因為裝飾器是一層包一層的, 可參考之前的文章 [介紹 python decorator](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_python_decorator).
