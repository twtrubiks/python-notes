# TYPE_CHECKING 介紹

說明一下 TYPE_CHECKING 的功能, 主要功能是避免 python 循環引用以及讓 IDE 支援靜態檢查.

```python
from typing import TYPE_CHECKING
```

先來看一個例子 [module_a.py](module_a.py)

```python
from module_b import ClassB

class ClassA:
    def __init__(self, b: ClassB) -> None:
        self.b = b

    def use_b(self) -> None:
        print("Using ClassB from ClassA")
```

[module_b.py](module_b.py)

```python
from module_a import ClassA

class ClassB:
    def __init__(self, a: ClassA) -> None:
        self.a = a

    def use_a(self) -> None:
        print("Using ClassA from ClassB")
```

當你執行 [main.py](main.py) 的時候, 會出現循環引用

```python
from module_a import ClassA
from module_b import ClassB

a = ClassA(None)
b = ClassB(a)
b.use_a()
```

那我們應該如何避免循環引用以及同時有 typing hint 的檢查呢 ❓

這時候介紹 TYPE_CHECKING

[module_a_fix.py](module_a_fix.py)

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from module_b_fix import ClassB

class ClassA:
    def __init__(self, b: "ClassB") -> None:
        self.b = b

    def use_b(self) -> None:
        print("Using ClassB from ClassA")
```

注意修改的地方, 首先, `TYPE_CHECKING = False` 預設是 False,

只有在 IDE 的部份才會是 True, 然後需要把 ClassB 加上雙引號變成 `"ClassB"`,

同理, [module_b_fix.py](module_b_fix.py) 一樣的修正方式.

修改完後的 [main_fix.py](main_fix.py) 就可以正常的執行.