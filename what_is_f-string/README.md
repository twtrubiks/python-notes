# f-string 字串格式化(python3.6) 是什麼:bulb:

[Youtube Tutorial - f-string 字串格式化(python3.6) 是什麼](https://youtu.be/3agdMlpxG-4)

## %-formatting

這種應該是大家最早接觸 python 會看到的:smirk:

```python
>>> 'Hello, %s' % ('World')
'Hello, World'
```

## str.format

這個出自 [PEP 3101](https://www.python.org/dev/peps/pep-3101/)，

現在大多數我都是使用這種

```python
text = "World"
>>> 'Hello, {}'.format(text)
'Hello, World'
```

但他是速度最慢的 (我今天才知道 :sweat_smile:)

## f-string

介紹今天的主角 Literal String Interpolation，

出自 [PEP 498](https://www.python.org/dev/peps/pep-0498/), 注意, **python 3.6** 才可以這樣使用。

```python
>>> text = "World"
>>> f'Hello, {text}'
'Hello, World'
```

官方範例

```python
>>> import datetime
>>> name = 'Fred'
>>> age = 50
>>> anniversary = datetime.date(1991, 10, 12)
>>> f'My name is {name}, my age next year is {age+1}, my anniversary is {anniversary:%A, %B %d, %Y}.'
'My name is Fred, my age next year is 51, my anniversary is Saturday, October 12, 1991.'
>>> f'He said his name is {name!r}.'
"He said his name is 'Fred'.
```

似乎感覺寫起來比較方便:+1:

如果用以前的寫法 ( str.format) 會一大串:sweat_smile:

```python
>>> import datetime
>>> name = 'Fred'
>>> age = 50
>>> anniversary = datetime.date(1991, 10, 12)
>>> 'My name is {}, my age next year is {}, my anniversary is {:%A, %B %d, %Y}.'.format(name, age+1, anniversary)
'My name is Fred, my age next year is 51, my anniversary is Saturday, October 12, 1991.'
```

### f-string 一些比較特別的用法

```python
# 向右補 0
n = 1
print(f"{n:0<5}") # 10000

n = 12
print(f"{n:0<5}") # 12000

n = 123456
print(f"{n:0<5}") # 123456


# 向左補 0
n = 1
print(f"{n:0>5}") # 00001

n = 12
print(f"{n:0>5}") # 00012

n = 123456
print(f"{n:0>5}") # 123456
```

## speed

使用 timeit 觀察速度，

```python
import timeit
>>> timeit.timeit("x = 10; 'X is {}'.format(x)")
0.3328074
>>> timeit.timeit("x = 10; 'X is %s' % x")
0.18661060000000163
>>> timeit.timeit("x = 10; f'X is {x}'")
0.18618709999999794
```

查了一下，基本上是 f-string (最快) > %-formatting  > str.format (最慢)，

不過我有時候跑 f-string 和 %-formatting 是差不多的 (很接近)，

不知道是不是和 python 版本有關係:expressionless:

總之，如果 python 都是使用 3.6 以上的，就建議都使用 f-string 吧:smile:

## Template Strings

多補充一個，這個也不算是特殊，他是 Standard Library。

官方文件可以點選這邊 [template-strings](https://docs.python.org/3/library/string.html#template-strings)，

來自 [PEP 292 -- Simpler String Substitutions](https://www.python.org/dev/peps/pep-0292/)。

舉個例子，

```python
>>> from string import Template
>>> text = "World"
>>> t = Template('Hello, $text!')
>>> t.substitute(text=text)
'Hello, World!'
```

str.format 造成的安全性問題，

```python
SECRET = 'secret token'

class Error:
    def __init__(self):
        pass

user_input = '{error.__init__.__globals__[SECRET]}'
err = Error()
output = user_input.format(error=err)
print(output)

### secret token
```

但如果透過 Template Strings 可避免這個問題，

```python
from string import Template

SECRET = 'secret token'

class Error:
    def __init__(self):
        pass

user_input = '${error.__init__.__globals__[SECRET]}'
err = Error()
output = Template(user_input).substitute(error=err)
print(output)

### ValueError: Invalid placeholder in string: line 1, col 1
```

假如有 user-supplied format string，就記得一定要使用 Template Strings。

## 執行環境

* Python 3.6.6

## Reference

* [Python String Formatting Best Practices](https://realpython.com/python-string-formatting/)
