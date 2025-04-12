# 在 python 中，常常看到 `_` 以及 `__` 到底是什麼

[Youtube Tutorial - what is private and protected attribute in python](https://youtu.be/tafpaPq6pH4)

在 python 中 `_` ( underscore ) 其實很有趣 :smirk:

最主要有幾種，

第一種， `__init__`，python 中所謂的 special methods。

第二種，`_foo`，python 中所謂的 protected attribute。

第三種，`__foo`，python 中所謂的 private attribute。

第四種，`foo_` or `foo__`，只是要避免和 built-in keywords 發生衝突而已。

## 第一種

可以唸 dunder-init ( dunder methods )，既然它都被叫做 special methods，

就不要隨便自己定義 __foo__，因為未來有一天他可能會被定義。

## 第二種

如果你有學過 java，你可以直接把 `_foo` 想成是 protected attribute，通常是因為不想讓它

直接被訪問。但要注意，這只是一種保護，如果你故意要去 access 它，你還是可以訪問。

```python
class Person:
    def __init__(self, name):
        self._name = name

    def _hello(self):
        print('hello: ', self._name)

def main():
    p = Person('twtrubiks')
    p._hello()

if __name__ == "__main__":
    main()
```

你會發現卻還是輸出 `hello:  twtrubiks`。

所以再強調一次，這只是一種保護，如果你故意要去 access 它，你還是可以訪問。

## 第三種

private attribute，先來看一個例子

```python
class Person:
    def __init__(self, name):
        self._name = name

    def __hello(self):
        print('hello: ', self._name)

def main():
    p = Person('twtrubiks')
    p.__hello()

if __name__ == "__main__":
    main()
```

當你執行它，你會得到以下的錯誤，

`AttributeError: 'Person' object has no attribute '__hello'`。

但再次強調，這只是一種保護，如果你故意要去 access 它，你還是可以訪問。

像是可以改成 `p._Person__hello()`，這樣就可以正常顯示了。

( 但非常不建議這樣使用 :unamused:)

```python
class Person:
    def __init__(self, name):
        self._name = name

    def __hello(self):
        print('hello: ', self._name)

def main():
    p = Person('twtrubiks')
    p._Person__hello()

if __name__ == "__main__":
    main()
```

輸出 `hello:  twtrubiks`。

其實這是 Name mangling。 ( Name mangling is about safety, not security )。

```python
class Person:
    def __init__(self, name):
        self._name = name

    def __hello(self):
        print('hello: ', self._name)

def main():
    p = Person('twtrubiks')
    print([attr for attr in dir(p) if 'hello' in attr])

if __name__ == "__main__":
    main()
```

輸出 `['_Person__hello']`。

正確的用法應該是這樣，要從內部去呼叫它，像是下面這樣。

```python
class Person:
    def __init__(self, name):
        self._name = name

    def print_hello(self):
        self.__hello()

    def __hello(self):
        print('hello: ', self._name)

def main():
    p = Person('twtrubiks')
    p.print_hello()

if __name__ == "__main__":
    main()
```

輸出 `hello:  twtrubiks`。

## 第四種

這種其實很簡單，就單純是要避免和 built-in keywords 或 built-in functions 發生衝突而已，

舉個例子，假如今天你有一個變數想叫做 `type`，但這個是 Keywords，所以有時候就會把變數命名為

`type_` 或 `type__`，但除非沒辦法，不然我會建議改其他名稱 :grin: