# What is the property

[Youtube Tutorial - What is the property in python](https://youtu.be/i8eHJDgKEsE)

這篇文章主要會介紹 property，在介紹之前，建議大家對 decorator 有一些基本的認識，

如果不了解，可參考 [What is the python decorator](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_python_decorator)。

python 中有幾個內建的 decorator，今天要來和大家介紹其中的一個，**property**。

這邊我不多做解釋，直接來看程式碼，

[demo1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_property/demo1.py)

```python
class A:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        if not hasattr(self, '_content'):
            return "content not exists"
        return self._content

    def set_content(self, value):
        self._content = value

    def delete_content(self):
        del self._content


if __name__ == "__main__":
    a = A('hello')
    print('content:', a.get_content())  # get content
    a.set_content('world')  # set content
    print('content:', a.get_content())
    a.delete_content()  # delete content
    print('content:', a.get_content())  # content not exists
```

A class 提供幾個方法，分別為 `get_content` 得到資料， `set_content` 設定資料，

`delete_content` 刪除資料，原因是為了避免直接對 `_content` 屬性操作，

也就是達到封裝的效果。

雖然看起來沒什麼問題，但就是覺得使用上沒那麼直覺，舉個例子，要得到資料，必須執行

`a.get_content()`，總覺得有點長，能不能更簡單一點:question:

可以:smile:

讓我們看改善後的例子，

[demo2.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_property/demo2.py)

```python
class A:
    def __init__(self, content):
        self._content = content

    @property
    def content(self):
        if not hasattr(self, '_content'):
            return "content not exists"
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @content.deleter
    def content(self):
        del self._content


if __name__ == "__main__":
    a = A('hello')
    print('content:', a.content)  # automatically calls getter
    a.content = 'world'  # automatically calls setter
    print('content:', a.content)
    del a.content  # automatically calls deleter
    print('content:', a.content)  # content not exists
```

透過 `@property` 的幫助，A class 中的 method 也不會在那麼的冗長，現在就很清楚且

簡單多了，而在使用上，也就得方便不少，像是要得到資料，直接執行 `a.content` 就可以

達到目的，而要設定資料，很直覺的執行 `a.content = 'world'` 即可 ( 當執行的時候，

他其實會去 call setter，可以使用中斷點觀察 )。

大家可以再比較 [demo1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_property/demo1.py) 以及 [demo2.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_property/demo2.py)，看看哪個比較簡便:smirk:

還有另一種寫法, 參考 [demo2_1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_property/demo2_1.py),

就是將 property 抽出來另外寫, 格式如下

`property(fget=None, fset=None, fdel=None, doc=None)`

```python
class A:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        if not hasattr(self, '_content'):
            return "content not exists"
        return self._content

    def set_content(self, value):
        self._content = value

    def del_content(self):
        del self._content

    # property(fget=None, fset=None, fdel=None, doc=None)
    content = property(get_content, set_content, del_content, 'my content property')
```

`@property` 還可以來建立 read only ( 透過他的 getter 和 setter 的特性 )，

看下面這個例子，

[demo3.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_property/demo3.py)

```python
import datetime

class A:
    def __init__(self, content):
        self._content = content

    @property
    def time(self):
        return datetime.datetime.now()


if __name__ == "__main__":
    a = A('hello')
    print('a.time:', a.time)
    # a.time = datetime.time(12, 20) # AttributeError: can't set attribute
```

像我們只有提供 `time` 的 getter，並沒有提供 setter，所以說當我們嘗試設定值到 time

的時候，就會出現錯誤，也就達成了 read only。

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
