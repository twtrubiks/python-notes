# PEP 484 Type Hints 介紹

[Youtube Tutorial - PEP 484 Type Hints 介紹](https://youtu.be/kXB__qIz5gY)

## 說明

Type Hints [pep-0484](https://www.python.org/dev/peps/pep-0484/) 這個東西在 python 3.5 就出現了,

當初我看幾乎沒甚麼人用, 於是就不理他, 時間過了那麼久之後, 我發現越來越多專案開始有用這個東西,

像是我之後會介紹的 [pydantic](https://pydantic-docs.helpmanual.io/) 以及 [fastapi](https://fastapi.tiangolo.com/),

甚至有時候看一些 source code 也都會寫 Type Hint, 所以在這邊決定寫一篇簡單的文章和大家分享.

Type Hint 說簡單不簡單, 如果你沒有看他的介紹, 你當下看到有 type hint 的 python 時會覺得

這是我所認知的 python 嗎？

例外補充一下, Type Hint 絕對不是強制性的, 根據團隊的習慣以及需求.

Type Hint 另一個好處是可以透過 IDE 下去協助檢查錯誤.

最後, Type Hint 不會影響到任何的效能問題.

## 教學

因為 python 版本真的蠻多的, 這邊是使用 python 3.8 當作範例.

先來看一個最簡單的例子

```python
def greeting(name: str) -> str:
    return 'Hello ' + name
```

`(name: str)` 除了原本的變數, 後面多了 `:str`, 指定這個參數的型態.

`-> str` return 的型態.

這邊只提最基本的概念, 因為他的東西確實不少, 大家可以參考官方文章 Type Hints [pep-0484](https://www.python.org/dev/peps/pep-0484/).

### Type comments

```python
x = [1, 2]            # type: List[int]
```

注意, 這個註解是會被 mypy 辨識出來的 (有意義的, 建議觀看影片說明).

詳細說明可參考 [type-comments](https://www.python.org/dev/peps/pep-0484/#type-comments).

## mypy

既然使用了 Type Hint, 建議搭配 [mypy](https://github.com/python/mypy) 協助檢查.

```python
pip3 install mypy
```

使用方法很簡單, 直接 `mypy xxx.py` 就會幫你檢查是否有錯誤.

![alt tag](https://i.imgur.com/wrvs8au.png)

當然也可以結合 VScode 中, `Ctrl+Shift+P` 找到 `Python:Select Linter` 選擇 mypy,

這樣當有錯誤的時候, 就會提醒.

![alt tag](https://i.imgur.com/nJHztC3.png)
