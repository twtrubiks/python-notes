# 什麼是 `if __name__ == '__main__'`

[Youtube Tutorial - 什麼是 `if __name__ == '__main__'`](xxx)

直接進入主題，如果你寫 python，一定常常看到如下的東西，

```python
if __name__ == '__main__':
    pass
```

而且，好像有他沒他也沒什麼影響，今天我就來介紹他到底是什麼東東:bulb:

直接來看一個例子，[demo1.py](demo1.py)

```python
def a1_func():
    print('hello a1_func')

print('demo1.py is called')
a1_func()
```

輸出很簡單，就是

```text
demo1.py is called
hello a1_func
```

以上很簡單，應該沒什麼問題。

接著看 [demo2.py](demo2.py)

```python
from demo1 import a1_func

print('demo2.py is called')
a1_func()
```

我們預期的結果應該是如下，

```text
demo2.py is called
hello a1_func
```

不過你如果執行 `python demo2.py`，你會發現結果卻是，

```text
demo1.py is called
hello a1_func
demo2.py is called
hello a1_func
```

為什麼會這樣呢:question:

原因是因為當 module 載入時 ( `from demo1 import a1_func` )，python 中的 interpreter 會

一行一行的去執行 `demo1.py` 中的內容，所以才會造成這樣的輸出結果。

那該如何解決這個問題呢 :question:

就是使用 `__name__ == '__main__'`，你可以把他想成是程式的**進入點**，

請看 [demo3.py](demo3.py)

```python
def a1_func():
    print('hello a1_func')

if __name__ == '__main__':
    print('demo3.py is called')
    a1_func()
```

這個範例的執行結果和 [demo1.py](demo1.py) 的完全一模一樣，

接著看 [demo4.py](demo4.py)

```python
from demo3 import a1_func
print('demo4.py is called')
a1_func()
```

執行結果如下，

```text
demo2.py is called
hello a1_func
```

現在這樣的結果就是我們希望的 ( 可以和 [demo2.py](demo2.py) 比較，會更清楚 :smile: )

所以，在這裡我們可以簡單理解 `if __name__ == '__main__'`，假如 module 是直接執行的，

會從這個進入點執行 ; 反之，假如是使用 import module 的方式，此區塊則不會被執行。

因為有時候程式可能會同時需要被單獨執行 ( 自己本身的功能或是跑測試 ) 以及被 import module 的方式。

這邊可以再延伸閱讀 [Package - 等待新增](xxx)。

## Donation

如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## License

MIT license
