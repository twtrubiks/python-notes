# What is the Mixin

[Youtube Tutorial - 什麼是 Mixin in python](https://youtu.be/mWg1sIUcepQ)

這篇文章主要會介紹 Mixin,

先來看一個例子

[demo1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_mixin/demo1.py)

```python
class A:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

if __name__ == '__main__':
    a = A('x1', 'y1')
    print(a)
```

這個範例很簡單, 就是定義一個 class,

那現在需要實作 `__str__`, 但卻又不能去修改 A class 裡面的東西,

這時候該怎麼辦呢 :question:

可以使用 Mixin 的方式下去進行擴充, 範例如下

[demo1_1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_mixin/demo1_1.py)

```python
class StrMixin:
    def __str__(self):
        return '{}_{}'.format(self.x1, self.x2)

class A(StrMixin):
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

if __name__ == '__main__':
    a = A('x1', 'y1')
    print(a)
```

從這個範例可以看出, 我們增加了一個 StrMixin, 並且繼承它, 這樣就實作了 `__str__`,

而且也沒有破壞 A class, 單純只是使用繼承的方式去擴充.

也可以多重的繼承, 多重的 Mixin

[demo1_2.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_mixin/demo1_2.py)

```python
class HelloMixin:
    def display(self):
        print('hello')

class StrMixin:
    def __str__(self):
        return '{}_{}'.format(self.x1, self.x2)

class A(StrMixin, HelloMixin):
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

if __name__ == '__main__':
    a = A('x1', 'y1')
    print(a)
    a.display()
```

這個範例, 將 A Mixin `StrMixin` 以及 `HelloMixin`,

這樣就同時有 `__str__` 以及 `display` 的功能了 :smile:

剛剛看了擴充的例子, 現在來看修改(覆寫)的例子,

[demo2.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_mixin/demo2.py)

```python
class HelloMixin:
    def display(self):
        print('HelloMixin hello')

class A(HelloMixin):
    pass

if __name__ == '__main__':
    a = A()
    a.display()
```

`HelloMixin` 這個因為某些原因我們不能動, 但我又想要修改 `display` 的東西, 這時候可以參考以下的作法,

[demo2_1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_mixin/demo2_1.py)

```python
class HelloMixin:
    def display(self):
        print('HelloMixin hello')

class SuperHelloMixin:
    def display(self):
        print('SuperHello hello')

class A(SuperHelloMixin, HelloMixin):
    pass

if __name__ == '__main__':
    a = A()
    a.display()
```

輸出結果會是 `SuperHello hello`, 因為繼承是有順序性的, 成功的將 `display` 覆寫掉.
