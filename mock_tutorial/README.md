# Mock 教學

官方文件 [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

在 Python 3.3 之後內建 unittest.mock,

可以使用 Mock 來模擬物件進行我們的測試

```python
from unittest.mock import Mock
mock = Mock()
mock
```

[demo1.py](demo1.py) 這個範例示範了如何 mock `datetime.datetime.today()`,

主要是透過 mock 中的 `return_value` 設定我們需要 mock 的值.

如果單純的只是想要 mock `datetime`, 可使用 [https://github.com/spulec/freezegun](https://github.com/spulec/freezegun).

如果遇到動態的回傳值或 raise Exception, 就必須去設定 `side_effect`

[demo2.py](demo2.py) 這邊示範了如何 mock requests 的 HTTPError,

可以透過 `assert_called_once()` 確認只呼叫一次, 超過一次就會出現錯誤.

[demo3.py](demo3.py) 這邊示範了結合 unittest.

[demo4.py](demo4.py) 這邊示範說明了 side_effect 是可以被 iterable

[demo4_1.py](demo4_1.py) 請看一下 side_effect 的官方範例.

[demo5.py](demo5.py) 這邊示範透過 `patch()` 來完成 mock, 可以把 `patch()` 想成是 Decorator,

[my_user.py](my_user.py) 是我們的 code, [demo5.py](demo5.py) 則是我們的測試, 分開了測試以及功能,

在這邊 import 並且 mock `my_user.requests`

這邊其實是有用到 Monkey patching 的概念.

[demo6.py](demo6.py) `patch()` 除了用 Decorator 完成之外, 也可以用 context manager (with as) 完成.

[demo7.py](demo7.py) 透過 `patch.object` patch 特定的 method, 像這邊只針對 `get` 這個 method.

接著是注意 patch 的位置,

[demo8.py](demo8.py) 像這樣就是比較好的方法, 成功 mock.

[demo8_1.py](demo8_1.py) 這樣就是比較不好的 mock, 而且 mock 是失敗的.

主要的差別就是 `import` 物件的時候要注意, 如果真的要寫的像 [demo8_1.py](demo8_1.py),

請改成 `__main__`, 如下範例

[demo8_2.py](demo8_2.py) 修改之後, 就可以成功 mock 了.

因為可能不知道該物件有哪些方法, 可以透過 `spec` 來解決,

[demo9.py](demo9.py) 透過 `spec` 這個參數, 可以設定我們需要 mock 的東西,

像是範例中的 `not_this_func` 沒有被設定, 呼叫的時候就會錯誤.

[demo9_1.py](demo9_1.py) `spec` 也可以直接放入 `my_user` 物件,

它會自動找裡面有的方法, 如果你呼叫 `not_this_func` 會錯誤 (因為不在 `my_user.py` 中).

這邊 mock 任意指定一個屬性 `attr_a` 是可行的.

[demo9_2.py](demo9_2.py) `spec_set` 和上面不同的是, 不能去 mock 除了 [my_user.py](my_user.py) 之外的物件,

像是這邊如果你去 mock `attr_a` 會發生錯誤.

[demo10.py](demo10.py) 也可以直接透過 `create_autospec` 來完成.

[demo11.py](demo11.py) 如果是透過 `patch()` 的方式, 可以透過 `autospec=True` 來完成.
