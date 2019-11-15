# python interpreter 說明

很多時候我們打開 `.py` 檔案，開頭的第一行會是 `#!/usr/bin/python3`。

有想過這是為什麼嗎 :question:

`#!/usr/bin/python3` 是用來指定 interpreter 直譯器:exclamation::exclamation:

為什麼要指定 interpreter 直譯器:question:

舉個例子，很多人在系統中同時安裝了 Python2 和 Python3，但是 2 和 3 是不兼容的，

所以執行 `.py` 時必須指定 interpreter 直譯器。

舉個例子，`hello.py` 如下

```python
#!/usr/bin/python3

import sys
print(str(sys.version))
```

你會發現輸出 python3 的資訊。

`#!` 之後的空格是可選擇的，也就是

`#!/usr/bin/env python3` 和 `#! /usr/bin/env python3` 這兩種寫法都是允許的。

如果有指定 interpreter 直譯器，可以直接執行以下指令，就會自動使用 python3 執行。

```cmd
./hello.py
```

如果沒有指定  interpreter 直譯器，也可以再執行時加上去。

```cmd
python3 hello.py
```

總之，目的就是要告訴電腦要用哪種 python 執行:blush:
