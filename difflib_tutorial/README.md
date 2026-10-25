# difflib

`difflib` 是 Python 標準庫, 用來比較序列 (文字, list) 之間的差異, 不需額外安裝.

你平常在 pytest 看到 assert 失敗時那段 `-` `+` 的差異訊息, 或是 Django 的 `assertHTMLEqual`, 底層都是 difflib 產生的.

官方文件 [difflib — Helpers for computing deltas](https://docs.python.org/3/library/difflib.html)

## SequenceMatcher - 計算相似度

[demo1.py](demo1.py)

```python
from difflib import SequenceMatcher

a = "hello world"
b = "hello python"

ratio = SequenceMatcher(None, a, b).ratio()
print(ratio)  # 0.6086956521739131 (相似度 0 ~ 1)
```

`ratio()` 的公式是 `2.0 * M / T`, M 是配對到的字元數, T 是兩個序列的總長度.

`get_opcodes()` 可以看 a 要怎麼變成 b (equal, replace, delete, insert), 不只字串, list 也可以比.

## unified_diff - 統一差異格式 (最常用)

[demo2.py](demo2.py)

輸出類似 `git diff`

```python
from difflib import unified_diff

old = """def greet(name):
    print("Hello")
    return True
""".splitlines(keepends=True)

new = """def greet(name):
    print(f"Hello, {name}")
    print("Welcome!")
    return True
""".splitlines(keepends=True)

diff = unified_diff(old, new, fromfile='old.py', tofile='new.py')
print(''.join(diff))
```

輸出

```diff
--- old.py
+++ new.py
@@ -1,3 +1,4 @@
 def greet(name):
-    print("Hello")
+    print(f"Hello, {name}")
+    print("Welcome!")
     return True
```

注意 `splitlines(keepends=True)` 要保留換行, 否則輸出會黏在一起.

參數 `n` 控制上下文顯示幾行, 預設 3.

## HtmlDiff - 產生 HTML 差異比較頁面

[demo3.py](demo3.py)

```python
from difflib import HtmlDiff

old = ["apple", "banana", "cherry"]
new = ["apple", "blueberry", "cherry", "date"]

html = HtmlDiff().make_file(old, new, fromdesc='舊版', todesc='新版')
with open('diff.html', 'w', encoding='utf-8') as f:
    f.write(html)
```

用瀏覽器開啟會看到並排的彩色差異比較表.

`make_file()` 產生完整的 HTML, `make_table()` 只產生 `<table>`, 方便塞進自己的頁面.

## get_close_matches - 模糊匹配

[demo4.py](demo4.py)

```python
from difflib import get_close_matches

words = ['apple', 'application', 'banana', 'apply', 'appreciate']

matches = get_close_matches('appla', words, n=3, cutoff=0.6)
print(matches)  # ['apply', 'apple', 'application']
```

參數

- `n`: 最多回傳幾個結果
- `cutoff`: 相似度門檻 (0 ~ 1), 低於此值不回傳

回傳結果會依相似度由高到低排序, `apply` 和 `appla` 只差一個字母, 所以排第一.

實際應用像是使用者打錯指令時給建議, 類似 git 的 `Did you mean`

```python
commands = ["commit", "checkout", "cherry-pick", "clone", "config"]
suggestion = get_close_matches("comit", commands, n=1)
print(suggestion)  # ['commit']
```

## Differ / ndiff - 逐行比較 (帶標記)

[demo5.py](demo5.py)

```python
from difflib import Differ

old = ["cat\n", "dog\n", "fish\n"]
new = ["cat\n", "horse\n", "fish\n", "bird\n"]

diff = Differ().compare(old, new)
print(''.join(diff))
```

輸出

```text
  cat       # 無變化
- dog       # 被移除
+ horse     # 新增
  fish      # 無變化
+ bird      # 新增
```

兩行很相似時, `Differ` 會多給一行 `?` 用 `^` `-` `+` 標出上一行哪個位置有差異, 這是 `unified_diff` 做不到的.

```text
- print('hello world')
?              ^ ^^^
+ print('hello python')
?              ^^^^ ^
```

`ndiff(old, new)` 是 `Differ().compare(old, new)` 的快捷寫法.

### restore - 從 diff 還原

`restore()` 可以從 `ndiff` 的結果還原出原始內容, 第二個參數 `1` 還原 old, `2` 還原 new, 適合只存 diff 不存全文的情境.

```python
from difflib import ndiff, restore

diff = list(ndiff(old, new))
print(''.join(restore(diff, 1)))  # 還原 old
print(''.join(restore(diff, 2)))  # 還原 new
```

## 實用場景總結

| 功能 | 適用場景 |
|------|---------|
| `SequenceMatcher` | 計算兩段文字的相似度分數 |
| `unified_diff` | 產生類似 git diff 的輸出 |
| `HtmlDiff` | 產生視覺化的 HTML 差異報告 |
| `get_close_matches` | 拼字建議, 模糊搜尋, 「你是不是要找...」 |
| `Differ` / `ndiff` | 逐行詳細比對, 標出行內差異位置 |
| `restore` | 從 diff 還原原始內容 |
