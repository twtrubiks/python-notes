# fibonacci numbers ( 費氏數列 )

[Youtube Tutorial - 什麼是費氏數列 in python - recursive - part 1](https://youtu.be/JWGCrICTars)

[Youtube Tutorial - 什麼是費氏數列 in python - lru_cache - part 2](https://youtu.be/TA0Dpx0LOeY)

[Youtube Tutorial - 什麼是費氏數列 in python - tail recursive - part 3](https://youtu.be/WyDn6wiwW74)

[Youtube Tutorial - 什麼是費氏數列 in python - iterative  - part 4](https://youtu.be/iCSNHH45EeI)

在介紹之前，先和大家說為什麼我會提他，原因就是面試有機會會考，而且可以考很多東西。

那什麼是 費氏數列 呢:question:

其實也很簡單，規則如下，

```txt
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233……
```

就是下一項等於自身加前一項的和 ( 也可以說是前兩項 ) 這樣。

( 這題在 leetcode 中也有出現，[070-Climbing Stairs](https://github.com/twtrubiks/leetcode-python/blob/master/Climbing_Stairs_070.py) )

好，知道他是什麼了，首先，使用遞迴 ( recursive ) 的方式，

[demo1.py](demo1.py)

```python
def normal_recursion(n):
    if n < 2:
        return n
    return normal_recursion(n - 1) + normal_recursion(n - 2)
```

其實很好理解，請看下方的圖，

![img](https://i.imgur.com/mscvxyG.png)

首先，只要 n ( 項數，從第 0 項開始 ) 小於 2，就回傳 n ( 第 0 項回傳 0 , 第 1 項回傳 1 )。

當 n 大於 1 ( n<2 )，就是 `normal_recursion(n - 1) + normal_recursion(n - 2)`。

雖然用遞迴的方式來解題一目瞭然，但其實有缺點，就是執行的效率很差，除了浪費資源之外，還有可能

造成錯誤 `RecursionError: maximum recursion depth exceeded in comparison`。

舉個浪費資源的例子，改成如下測試，

```python
def normal_recursion(n):
    print('call')
    if n < 2:
        return n
    return normal_recursion(n - 1) + normal_recursion(n - 2)

if __name__ == '__main__':
    print(normal_recursion(5))
```

你會發現 call 被印出不只 5 次，原因就是因為一層 call 一層的關係以及一直重複計算。

原因如下，他的時間複雜度 ( Time Complexity ) 為 O(2^n) ( 非常接近 )，

如下圖，

![img](https://i.imgur.com/HcuE9jD.png)

這時候你可能會說，越左邊到後面就不用計算那麼多層了，想像 n 數字很大，就非常接近 O(2^n)。

至於實際運算的過程如下，從下往上看 ( 如下圖 )。

![img](https://i.imgur.com/Eg0hXWB.png)

然後如果今天數值很大，`normal_recursion(100000)`，你會發現他直接噴錯。

[Youtube Tutorial - 什麼是費氏數列 in python - lru_cache - part 2](https://youtu.be/TA0Dpx0LOeY)

其實這個題目我之前也有提過，既然它一直重複的計算，那我就把算過的部分快取起來，

( 可參考 [What is the functools.lru_cache in python](https://github.com/twtrubiks/python-notes/tree/master/what_is_the_functools.lru_cache) )

[demo2.py](demo2.py)

```python
import functools

@functools.lru_cache()
def fib_lru_cache(n):
    print('call')
    if n < 2:
        return n
    return fib_lru_cache(n - 1) + fib_lru_cache(n - 2)

if __name__ == '__main__':
    print(fib_lru_cache(5))
```

你會發現 call 被印出 5+1 次 ( 從第 0 項開始 )，原因是如果有重複的，就會直接從快取中拿。

其實 `functools.lru_cache` 是使用 dict 的概念實現的，讓我們也來寫一個

簡易版的 `functools.lru_cache`，

[demo3.py](demo3.py)

```python
my_dict = dict()

def my_cache(fun):
    def wrap(*args, **kwargs):
        key = args[0]
        if key not in my_dict:
            my_dict[key] = fun(*args, **kwargs)
        return my_dict[key]

    return wrap

@my_cache
def fib_self_cache(n):
    if n < 2:
        return n
    return fib_self_cache(n - 1) + fib_self_cache(n - 2)

if __name__ == '__main__':
    print(fib_self_cache(5))
```

大家可以跑跑看，答案是一樣的。

除了一般的 recursion 之外，我們還可以使用 tail recursion 來改善它，

[Youtube Tutorial - 什麼是費氏數列 in python - tail recursive - part 3](https://youtu.be/WyDn6wiwW74)

什麼是 tail recursion 呢 :question:

tail recursion 就是把當前的運算結果再傳到下一層去，這樣就不會有一般的

recursion 造成一直重複計算的問題。

[demo4.py](demo4.py)

```python
def fib_tail_recursion(num, result, temp):
    print('call')
    if num == 0:
        return result
    else:
        return fib_tail_recursion(num - 1, temp, result + temp)

if __name__ == '__main__':
    print(fib_tail_recursion(5, 0, 1))
```

num 就是 n，也就是費氏數列的第幾項，result 則是我們的結果 ( 從 0 開始 )，

而 temp 則是一個暫存的變數 ( 從 1 開始 )。

說明如下，請看下方的圖，

![img](https://i.imgur.com/JSv9jNX.png)

雖然這個方法解決了一直重複運算的問題，

但還是沒有解決 `RecursionError: maximum recursion depth exceeded` 這個問題。

( 可用 `fib_tail_recursion(100000, 0, 1)` 測試 )

[Youtube Tutorial - 什麼是費氏數列 in python - iterative  - part 4](https://youtu.be/iCSNHH45EeI)

這時候，使用 iterative 的方法解決，空間換取時間，

可以將時間複雜度 ( Time Complexity ) 降為 O(n)。

[demo5.py](demo5.py)

```python
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == '__main__':
    fib_iterative(5)
```

這樣就解決了 `RecursionError: maximum recursion depth exceeded` 這個問題。

( 可用 `fib_iterative(100000)` 測試 )

說明如下，請看下方的圖，

![img](https://i.imgur.com/zmJ4hTN.png)

## Donation

文章都是我自己研究內化後原創，如果有幫助到您，也想鼓勵我的話，歡迎請我喝一杯咖啡:laughing:

綠界科技ECPAY ( 不需註冊會員 )

![alt tag](https://payment.ecpay.com.tw/Upload/QRCode/201906/QRCode_672351b8-5ab3-42dd-9c7c-c24c3e6a10a0.png)

[贊助者付款](http://bit.ly/2F7Jrha)

歐付寶 ( 需註冊會員 )

![alt tag](https://i.imgur.com/LRct9xa.png)

[贊助者付款](https://payment.opay.tw/Broadcaster/Donate/9E47FDEF85ABE383A0F5FC6A218606F8)

## 贊助名單

[贊助名單](https://github.com/twtrubiks/Thank-you-for-donate)

## License

MIT license
