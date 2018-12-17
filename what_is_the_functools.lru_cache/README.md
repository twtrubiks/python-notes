# What is the functools.lru_cache in python

[Youtube Tutorial - What is the functools.lru_cache in python-等待新增](X)

這篇文章主要會介紹 functools module 中的 `functools.lru_cache`，在介紹之前，

建議大家對 decorator 有一些基本的認識，

如果不了解，可參考 [What is the python decorator](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_python_decorator)。

直接看下面這個例子，看完之後我再來解釋，

[demo1.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_functools.lru_cache/demo1.py)

```python
import functools

@functools.lru_cache() # <1>
def job(n):
    print('run very long.....')
    return n + 10000

if __name__ == '__main__':
    print(job(2)) # <2>
    print(job(2)) # <3>
```

<1> 的部分，就是我們的主角，但等等再來介紹，先觀察 <2> 和 <3> 的輸出結果，

```text
run very long.....
10002
10002
```

發現了嗎:question:

竟然只顯示一次的 run very long，不是應該要 print 出兩次嗎:question:

原因就是使用了 `@functools.lru_cache()`，的關係，主要會把結果快取起來，

這樣的好處是就算 `job` 這個 function 要執行非常的久，當我們傳入**同樣的參數**

進去時，他不會再重新運算一次( 浪費運算資源 )，而是會使用之前快取的結果。

英文單字 LRU 為 Least Recently Used 的縮寫，意思也就是說，這個快取不是無限成長，

是有限制的，如果太久沒有被使用，也會從 cache 中移除。

比較典型的例子就是 [Fibonacci number](https://en.wikipedia.org/wiki/Fibonacci_number) ( 費氏數列 )，

以下是 fluent python 中的一段 code ( 再加以修改 )，

[demo2.py](demo2.py)

```python
from clockdeco import clock

@clock # <1>
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print([fib(n) for n in range(16)]) # <2>
```

<1> 的部分，clock 這個裝飾器只是要記錄執行的時間，可參考 [clockdeco.py](https://github.com/twtrubiks/python-notes/blob/master/what_is_the_functools.lru_cache/clockdeco.py)。

<2> 的部分，觀察他的輸出結果，

```text
[0.00000000s] fib(3) -> 2
[0.00100017s] fib(5) -> 5
[0.00000000s] fib(1) -> 1
[0.00000000s] fib(0) -> 0
[0.00000000s] fib(2) -> 1
[0.00000000s] fib(1) -> 1
......
[0.00000000s] fib(1) -> 1
[0.00000000s] fib(3) -> 2
[0.00000000s] fib(5) -> 5
[0.00000000s] fib(7) -> 13
[0.00100017s] fib(9) -> 34
[0.00200033s] fib(11) -> 89
[0.00000000s] fib(1) -> 1
......
[0.00000000s] fib(7) -> 13
[0.00000000s] fib(9) -> 34
[0.00199962s] fib(11) -> 89
[0.00500059s] fib(13) -> 233
[0.01199317s] fib(15) -> 610
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
```

發現到了嗎:question:

有很多重複執行的部分，其實這些地方都是多跑的，因為其實都已經計算過了，可以利用

`@functools.lru_cache()` 將結果快取起來，

[demo3.py](demo3.py)

```python
from lru_cache_tu.clockdeco import clock
import functools

@functools.lru_cache() # <1>
@clock
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print([fib(n) for n in range(16)]) # <2>
```

增加了 <1> 的裝飾器，觀察 <2> 輸出的結果

```text
[0.00000000s] fib(0) -> 0
[0.00000000s] fib(1) -> 1
[0.00000000s] fib(2) -> 1
[0.00000000s] fib(3) -> 2
[0.00000000s] fib(4) -> 3
[0.00000000s] fib(5) -> 5
[0.00000000s] fib(6) -> 8
[0.00000000s] fib(7) -> 13
[0.00000000s] fib(8) -> 21
[0.00000000s] fib(9) -> 34
[0.00000000s] fib(10) -> 55
[0.00000000s] fib(11) -> 89
[0.00000000s] fib(12) -> 144
[0.00000000s] fib(13) -> 233
[0.00000000s] fib(14) -> 377
[0.00000000s] fib(15) -> 610
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
```

每個都只會呼叫一次，因為如果有重複的，就會直接使用快取，減少不必要的開銷。

另外一點要注意的是參數的問題，預設的參數為 `functools.lru_cache(maxsize=128, typed=False)`，

`maxsize` 指的是可以 cache 多少個結果，如果滿了，就會丟棄最近使用較少的快取

( 如果設定為 None，將會讓 cache 無限成長且不會丟棄任何 cache )。

`typed` 指的是是否 f(3.0) 和 f(3) 為不同的結果。

來看一個例子解釋上面這兩個參數，

[demo4.py](demo4.py)

```python
import functools

@functools.lru_cache(maxsize=2, typed=False)
def job(n):
    print('run very long.....')
    return n + 10000

if __name__ == '__main__':
    print(job(2))
    print(job(3))
    print(job(2))
    print(job(4))
    print(job(3)) # <1>
```

觀察輸出結果，

<1> 的部分，會發現沒有被 cache，原因是因為 cache 已經滿了。

[demo5.py](x)

```python
import functools

@functools.lru_cache(maxsize=128, typed=True)
def job(n):
    print('run very long.....')
    return n + 10000


if __name__ == '__main__':
    print(job(1)) # <1>
    print(job(1.0)) # <2>
```

如果將 `typed` 設定為 `True`，你會發現 <1> 和 <2> 他會認為是兩種

不同的結果，所以不會使用 cache，如果設定為 `False` ( 預設值 )，

將會把他們視為是一樣的，也就是會使用 cache。

最後一點要注意的是，因為 lru_cache 是使用 `dict` 的方式去儲存的，

所以被 lru_cache 裝飾的 function 中的參數，必須是 **hashable**。

( 可以將參數改成 `list`，因為他不是 hashable，所以就會噴錯 )

如果你不了解什麼是 **hashable**，可參考 [What is the Hashable](https://github.com/twtrubiks/fluent-python-notes/tree/master/what_is_the_hashable)。

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
