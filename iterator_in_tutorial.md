## in 也會消費 iterator

先從簡單的例子看起,

```python
var_iter = iter('apple')
print([char for char in var_iter])
# -> ['a', 'p', 'p', 'l', 'e']
```

看起來沒問題.

```python
var_iter = iter('apple')
print([char for char in var_iter])
# -> ['a', 'p', 'p', 'l', 'e']
print([char for char in var_iter])
# -> []
```

第二次輸出會是空的, 是因為在第一次的時候已經消費完了.

再回到主題 in 也會消費 iterator, 看一個例子,

```python
s1 = 'apple'
var_iter = iter(s1)

print(bool('a' in var_iter))
# -> True
print(list(var_iter))
# -> ['p', 'p', 'l', 'e']

# -> 可以看到 in 也會消費 iterator
```

如果今天我們多加幾個 in 呢:question:

```python
s1 = 'apple'
var_iter = iter(s1)

print(bool('a' in var_iter))
# -> True
print(bool('l' in var_iter))
# -> True
print(list(var_iter))
# -> ['e']

# 因為一直消費 iterator, 直到找到目標為為止,
# 所以輸出只有 'e' ('l' 為倒數第2個)
```

上面的例子都是有找到, 如果沒有找到呢:question:

```python
s1 = 'apple'
var_iter = iter(s1)

print(bool('x' in var_iter))
# -> False
print(list(var_iter))
# -> []

# 因為一直消費 iterator, 直到找到目標為為止,
# 但消費完後, 還是沒有找到, 所以輸出 []
```

有了這些概念, 假設現在有一個需求,

我想要知道 s1 是否是 s2 的 subsequence,

這時候就可以利用剛剛學到的概念來完成,

```python
var_iter = iter(s1)
print(
    all(c in var_iter for c in s2)
)
```

先來看一個屬於的例子

```python
s1 = 'apple'
var_iter = iter(s1)
s2 = 'ppl'

# 使用方法
# print('s2 belong to s1 subsequence')
# print(all(c in var_iter for c in s2))
# -> Ture

# 分解流程
print(list(c in var_iter for c in s2))
# -> [True, True, True]
print(list(var_iter))
# -> ['e']
```

來看一個不屬於的例子,

```python
s1 = 'apple'
var_iter = iter(s1)
s2 = 'px'

# 使用方法
# print('s2 not belong to s1 subsequence')
# print(all(c in var_iter for c in s2))
# -> False

# 分解流程
print(list(c in var_iter for c in s2))
# -> [True, False]
print(list(var_iter))
# -> []
```