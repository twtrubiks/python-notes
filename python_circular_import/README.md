***circular import***

[Youtube Tutorial - What is Python Circular Imports](https://youtu.be/RQhN24QtDAE)

在介紹 circular import 之前，我們先來看一個例子，

大家一定常常使用 `import abc` or `from aa import c` 去 import module，

另外一種是 `from a import *`，這種就非常不建議，因為會讓 code 變的很亂，

而且你使用 module 中的什麼東西也不清楚 ( 容易造成衝突也不容易維護 )。

來看一下 [demo1](https://github.com/twtrubiks/python-notes/tree/master/python_circular_import/demo1) 資料夾，裡面有 `a.py`，`b.py`，`c.py`，

假設 `a.py` 以及 `b.py` 裡面都有 `hello` 這個 function，

[a.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo1/a.py) 如下，

```python
def hello():
    print('hello in a.py')
```

[b.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo1/b.py) 如下，

```python
def hello():
    print('hello in b.py')
```

[c.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo1/c.py) 如下，

```python
from a import hello
from b import hello

if __name__ == '__main__':
    hello()
```

這樣輸出的結果是 `hello in b.py`，也就是說後面的會蓋掉前面的，`a.py` 的 `hello` function 會被覆蓋掉。

如果真的遇到這種情況該如何解決呢?

可以改使用 `import` 的方式，參考 [c_fix.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo1/c_fix.py)，

```python
import a
import b

if __name__ == '__main__':
    a.hello()
    b.hello()
```

使用上面這種方法就可以正常的顯示。

所以當你使用 `from a import b` 這種方法時，

要多思考一下，雖然現在大多數的 IDE 都會提醒你這樣使用會有問題 ( import 的 module 有重複的 function 或 class )，

但在一些情況下，你可以直接使用 `from a import b`的方式，

* 很確定的只需要 import 某個 function 或 class，而且這方法不會和其他的 module 衝突。
* 非常高的頻率一直要輸入 a.b 這種的時候，可以考慮使用 `from a import b`。
* module 的文件明確的建議使用 `from a import b`。

看完上面的例子之後，那到底什麼是 circular import 循環引用呢 ?

我們來看 [demo2](https://github.com/twtrubiks/python-notes/tree/master/python_circular_import/demo2) 這個資料夾，裡面有 `a2.py` 以及 `b2.py`

[a2.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo2/a2.py)

```python
from b2 import hello


def world():
    print('world in a2')


def show():
    print('show in a2')
    hello()


if __name__ == '__main__':
    show()

```

[b2.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo2/b2.py)

```python
from a2 import world


def hello():
    print('hello in b2')


def show():
    print('show in b2')
    world()


if __name__ == '__main__':
    show()

```

不管你執行 `a2.py` 或 `b2.py`，都會發生如下的錯誤訊息，

```text
ImportError: cannot import name 'xxxx'
```

原因就是 circular import 循環引用，先來看 `a2.py`，

第一行是 `from b2 import hello`，於是進入 `b2.py` 找 `hello` function，

因為 python 又是一行一行執行，而且 `b2.py` 的第一行又是 `from a2 import world`，

但 `a2.py` 的過程根本還沒有結束，所以會出問題，也就是互相不退讓的概念。

那該如何解決 circular import 循環引用呢?

第一種方法是使用 `import ...` 的方法，不要使用 `from xxx import ...` 的方法。

看 [demo3](https://github.com/twtrubiks/python-notes/tree/master/python_circular_import/demo3) 的資料夾，

[a3.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo3/a3.py)

```python
import b3


def world():
    print('world in a3')


def show():
    print('show in a3')
    b3.hello()


if __name__ == '__main__':
    show()

```

[b3.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo3/b3.py)

```python
import a3


def hello():
    print('hello in b3')


def show():
    print('show in b3')
    a3.world()


if __name__ == '__main__':
    show()

```

這樣子就可以正常的執行，因為我們是直接 import 整個 module，以 [a3.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo3/a3.py) 為例，

當執行 `import b3` 時，只會檢查 b3 這個 module 是否存在，而不會像 `from b2 import hello`

一樣會去找出 hello 這個 function，導致 circular import。

第二種方法是將 import 放在 function 之中，也就是所謂的 **延遲 import**，

看 [demo4](https://github.com/twtrubiks/python-notes/tree/master/python_circular_import/demo4) 的資料夾

[a4.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo4/a4.py)

```python
def world():
    print('world in a2')


def show():
    from b4 import hello
    print('show in a2')
    hello()


if __name__ == '__main__':
    show()
```

[b4.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo4/b4.py)

```python
def hello():
    print('hello in b2')


def show():
    from a4 import world
    print('show in b2')
    world()


if __name__ == '__main__':
    show()

```

將 import 的部分放到 `show` function 之中，所以當我們有 call `show` function

的時候才會被使用到，也可以避免 circular import，但這方法有點 hack ( 或是說偷雞 )，

所以請斟酌使用。

這邊再補充一個方法 ( 感謝網友的提醒 )，除了上述的方法之外，我們也可以這樣使用，請看 看 [demo5](https://github.com/twtrubiks/python-notes/tree/master/python_circular_import/demo5) 的資料夾，

[a5.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo5/a5.py)

```python
def world():
    print('world in a5')


from demo5.b5 import hello


def show():
    print('show in a5')
    hello()


if __name__ == '__main__':
    show()
```

[b5.py](https://github.com/twtrubiks/python-notes/blob/master/python_circular_import/demo5/b5.py)

```python
def hello():
    print('hello in b5')


from demo5.a5 import world


def show():
    print('show in b5')
    world()


if __name__ == '__main__':
    show()
```

雖然這種方法，會有 pep8 的警告訊息 :sweat_smile:

最後一種方法就是好好思考你的架構，或許說你本來就將不該拆開的部分拆開了，所以才導致 circular import。
