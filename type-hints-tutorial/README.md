# PEP 484 Type Hints 介紹

[Youtube Tutorial - PEP 484 Type Hints 介紹](https://youtu.be/kXB__qIz5gY)

## 說明

Type Hints [pep-0484](https://www.python.org/dev/peps/pep-0484/) 這個東西在 python 3.5 就出現了,

當初我看幾乎沒甚麼人用, 於是就不理他, 時間過了那麼久之後, 我發現越來越多專案開始有用這個東西,

像我介紹過得 [pydantic 教學](https://github.com/twtrubiks/python-notes/tree/master/pydantic_tutorial) 以及 [fastapi](https://fastapi.tiangolo.com/),

甚至有時候看一些 source code 也都會寫 Type Hint, 所以在這邊決定寫一篇簡單的文章和大家分享.

Type Hint 說簡單不簡單, 如果你沒有看他的介紹, 你當下看到有 type hint 的 python 時會覺得

這是我所認知的 python 嗎 ❓

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


再來看個範例

```python
from typing import Dict, List, Optional


def fun1(my_dict: Dict[int, str]) -> Optional[List[str]]:
    return list(my_dict.values()) if my_dict else None
```

`my_dict: Dict[int, str]` dict, 代表 key 必須是 int, value 必須是 str.

`Optional[X]` 等於 `Union[X, None]` 代表可以接受 X 或是 None.

`Optional[List[str]]` 等於 `Union[List[str], None]` 代表會回傳 `List[str]` 或 None.


這邊補充說明一下 `from __future__ import annotations`,

```python
from __future__ import annotations

class Person:
    def __init__(self, name: str, action: Action) -> None:
        self.name = name
        self.action = action

class Action:
    def __init__(self, name: str) -> None:
        self.name = name
```

如果上方這段 code 沒有 `from __future__ import annotations`, 執行時會出現錯誤

```text
Exception has occurred: NameError
name 'Action' is not defined
```

需要透過它來將全部的 annotations 轉化成文字.

官方說明如下,

```text
A compromise is possible where a __future__ import could enable turning all annotations in a given module into string literals
```

### 其他範例

- [Any](https://github.com/twtrubiks/python-notes/blob/master/type-hints-tutorial/Any_tutorial.py)

- [TypeVar](https://github.com/twtrubiks/python-notes/blob/master/type-hints-tutorial/TypeVar_tutorial.py)

- [Tuple](https://github.com/twtrubiks/python-notes/blob/master/type-hints-tutorial/Tuple_tutorial.py)

- [Callable](https://github.com/twtrubiks/python-notes/blob/master/type-hints-tutorial/Callable_tutorial.py)

- [kwargs args](https://github.com/twtrubiks/python-notes/blob/master/type-hints-tutorial/kwargs_args_tutorial.py)

- [KeysView](https://github.com/twtrubiks/python-notes/blob/master/type-hints-tutorial/KeysView_tutorial.py)

- [Protocol](https://github.com/twtrubiks/python-notes/blob/master/type-hints-tutorial/Protocol_tutorial.py)

- [TYPE_CHECKING](https://github.com/twtrubiks/python-notes/tree/master/type-hints-tutorial/TYPE_CHECKING_tutorial) - 說明 TYPE_CHECKING 用法

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
