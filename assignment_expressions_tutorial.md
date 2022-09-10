# PEP 572 – Assignment Expressions

注意, 至少要 python3.8 才有這個語法,

Assignment Expressions 又被稱為 海象運算符 `:=`

詳細說明可參考 [https://peps.python.org/pep-0572/](https://peps.python.org/pep-0572/)

## 說明

先看下面這個例子,

```python
def demo1():
    content = "12345"
    if len(content) < 6:
        print(f"len: {len(content)}")

demo1()
```

`len(content)` 使用了兩次, 分別是在 if 判斷的時候, 以及 print 的時候.

或是可以改成這樣寫,

```python
def demo2():
    content = "12345"
    length = len(content)
    if length < 6:
        print(f"len: {length}")

demo2()
```

雖然現在 if 和 print 都是使用 length 這個變數,

但是我們還是要在前面多設定 `length = len(content)`

如果現在有 海象運算符 `:=` 可以改成這樣,

```python
def demo3():
    content = "12345"
    if (n := len(content)) < 6:
        print(f"len: {n}")

demo3()
```

這樣我們就節省了一個變數去保存 `len(content)`

再來看一個例子,

```python
def e1():
    n = 0
    while 1:
        n = n + 1
        if n < 5:
            print(n)
        else:
            break

e1()
```

如果透過 海象運算符 `:=` 可以更精簡,

```python
def e2():
    n = 0
    while (n:=n+1) < 5:
        print(n)

e2()
```

簡單說, 海象運算符 `:=` 可以讓你的 code 看起來更精簡, 不需要多設定一個變數:smile: