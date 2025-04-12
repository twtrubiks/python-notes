# pytest 教學

官網文件可參考 [pytest](https://docs.pytest.org/en/6.2.x/)

先安裝 pytest

```cmd
pip3 install pytest
```
[demo1_test.py](demo1_test.py) 基本的示範 pytest 的寫法

執行指令如下

```cmd
pytest demo1_test.py -v -s
```

記得要加入 `-s` (才能顯示 print 資訊)

執行結果

```text
collected 1 item

demo1_test.py::test_answer PASSED
```

pytest 也有 初始化 setup 和 清除 teardown 的方法,

它有分很多級別,

`setup_module/teardown_module`

`setup_function/teardown_function`

`setup_class/teardown_class`

`setup_method/teardown_methond` euqal `setup/teardown`

[demo2_module_test.py](demo2_module_test.py) 範例為使用 `*_module` 級別,

setup 和 teardown 只會在最開始和最後個別執行一次

```text
demo2_module_test.py::TestDemo2::test_case1 setup...
run test_case1
PASSED
demo2_module_test.py::TestDemo2::test_case2 run test_case2
PASSED
demo2_module_test.py::TestDemo2::test_case3 run test_case3
PASSEDteardown...
```

[demo2_function_test.py](demo2_function_test.py) 範例為使用 `*_function` 級別,

setup 和 teardown 在每個 function 中都會生效

```text
demo2_function_test.py::test_case1 setup...
run test_case1
PASSEDteardown...

demo2_function_test.py::test_case2 setup...
run test_case2
PASSEDteardown...

demo2_function_test.py::test_case3 setup...
run test_case3
PASSEDteardown...
```

[demo2_class_test.py](demo2_class_test.py) 範例為使用 `*_class` 級別,

setup 和 teardown 只會在 class 最開始和最後個別執行一次

```text
demo2_class_test.py::TestDemo2::test_case1 setup...
run test_case1
PASSED
demo2_class_test.py::TestDemo2::test_case2 run test_case2
PASSED
demo2_class_test.py::TestDemo2::test_case3 run test_case3
PASSEDteardown...
```

[demo2_method_test.py](demo2_method_test.py) 範例為使用 `*_method` 級別,

setup 和 teardown 在每個 function 中都會生效

```text
demo2_method_test.py::TestDemo2::test_case1 setup...
run test_case1
PASSEDteardown...

demo2_method_test.py::TestDemo2::test_case2 setup...
run test_case2
PASSEDteardown...

demo2_method_test.py::TestDemo2::test_case3 setup...
run test_case3
PASSEDteardown...
```

但是在 pytest 中, 有更好的方法可以取代掉這種比較舊的寫法 :smile: (後面會介紹到)

[demo3_test.py](demo3_test.py) `fixture` 這個方法主要是用來改善 `setup/teardown` 這樣的架構,

test_case2 會去取 hello 的值, pytest 會去找擁有 `@pytest.fixture()` hello 的方法,

```text
demo3_test.py::Test_Demo3::test_case1 run test_case1
PASSED
demo3_test.py::Test_Demo3::test_case2 hello world
run test_case2
66
PASSED
demo3_test.py::Test_Demo3::test_case3 run test_case3
PASSED
```

[demo3_share_test.py](demo3_share_test.py) 這個範例和上面是一樣的, 只是將 hello 獨立出來,

寫在 [conftest.py](conftest.py) 中, pytest 會自己到目錄底下尋找.

[demo4_test.py](demo4_test.py) 可以使用 yield 來完成 setup 和 teardown 的功能.

```text
demo4_test.py::Test_Demo4::test_case1 run test_case1
PASSED
demo4_test.py::Test_Demo4::test_case2 start hello world
run test_case2
66
PASSEDend hello world

demo4_test.py::Test_Demo4::test_case3 run test_case3
PASSED
```

[demo5_test.py](demo5_test.py) 除了用 yield 來完成 setup 和 teardown 的功能之外,

也可以用 `addfinalizer` 這個方法.

```text
demo5_test.py::Test_Demo5::test_case1 run test_case1
PASSED
demo5_test.py::Test_Demo5::test_case2 start hello world
run test_case2
66
PASSEDend hello world

demo5_test.py::Test_Demo5::test_case3 run test_case3
PASSED
```

fixture 也有所謂的 Scope (預設為 function), 分別為

`function` 每個 function 都會執行一次

`class` 每個 class 只執行一次

`module` 每個 module 只執行一次

`session` 整個 session 只執行一次

[demo6_test.py](demo6_test.py) 該範例為 `function`,

每一個 function 都會調用一次,

```text
demo6_test.py::Test_Demo6::test_case1 hello world
run test_case1
66
PASSED
demo6_test.py::Test_Demo6::test_case2 hello world
run test_case2
66
PASSED
demo6_test.py::Test_Demo6::test_case3 hello world
run test_case3
66
PASSED
```

[demo7_test.py](demo7_test.py) 該範例為 `class`,

只調用了一次,

```text
demo7_test.py::Test_Demo7::test_case1 hello world
run test_case1
PASSED
demo7_test.py::Test_Demo7::test_case2 run test_case2
PASSED
demo7_test.py::Test_Demo7::test_case3 run test_case3
PASSED
```

[demo8_test.py](demo8_test.py) 該範例為 fixture 自動調用, 透過 `autouse=True` 參數,

因為 default 的 `scope=function`, 所以每個 function 都會被調用.

```text
demo8_test.py::Test_Demo8::test_case1 hello world
run test_case1
PASSED
demo8_test.py::Test_Demo8::test_case2 hello world
run test_case2
PASSED
demo8_test.py::Test_Demo8::test_case3 hello world
run test_case3
PASSED
```

[demo9_test.py](demo9_test.py) 也可以透過 `@pytest.mark.usefixtures` 自動調用 fixture.

```text
demo9_test.py::Test_Demo9::test_case1 hello world
run test_case1
PASSED
demo9_test.py::Test_Demo9::test_case2 hello world
run test_case2
PASSED
demo9_test.py::Test_Demo9::test_case3 hello world
run test_case3
PASSED
```

[demo10_test.py](demo10_test.py) 如果測試都是呼叫相同的參數, 可以將 fixture 參數化.

```text
demo10_test.py::Test_Demo10::test_case1 run test_case1
PASSED
demo10_test.py::Test_Demo10::test_case2 run test_case2
PASSED
demo10_test.py::Test_Demo10::test_case3 run test_case3
PASSED
demo10_test.py::Test_Demo10::test_case4[data0] run test_case4
PASSED
demo10_test.py::Test_Demo10::test_case4[data1] run test_case4
PASSED
demo10_test.py::Test_Demo10::test_case4[data2] run test_case4
PASSED
```

[demo11_test.py](demo11_test.py) 或是透過 `pytest.mark.parametrize` 也可以參數化.

```text
demo11_test.py::Test_Demo11::test_case1[input0] run test_case1
(1, 1, 2)
PASSED
demo11_test.py::Test_Demo11::test_case1[input1] run test_case1
(2, 2, 4)
PASSED
demo11_test.py::Test_Demo11::test_case1[input2] run test_case1
(3, 3, 6)
PASSED
```

[demo12_test.py](demo12_test.py) 預期的錯誤 (expected exceptions) `pytest.raises`

```text
demo12_test.py::test_zero_division PASSED
```

[demo13_test.py](demo13_test.py) pass 預期的錯誤 `pytest.mark.skip` `pytest.mark.xfail`

```text
demo13_test.py::test_f XFAIL
demo13_test.py::test_s SKIPPED (pass.....)
```

[demo14_test.py](demo14_test.py) custom markers (客製化 markers)

先建立 [pytest.ini](pytest.ini) 設定你的 custom markers,

如果沒設定就使用裝飾器 `@pytest.mark.name_of_the_mark`, 會跳出錯誤

```text
'slow' not found in `markers` configuration option
```

如果我想 pass custom markers, 請執行以下的指令.

```cmd
pytest demo14_test.py -v -s --strict-markers -m "not slow"
```

```text
demo14_test.py::test_a PASSED
```

```cmd
pytest demo14_test.py -v -s
```

```text
demo14_test.py::test_super_slow_test PASSED
demo14_test.py::test_a PASSED
```

最後, 如果你想要產生 coverage, 可參考 [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/readme.html)

安裝套件

```cmd
pip install pytest-cov
pip install pytest-xdist
```

```cmd
pytest --cov=.
```

![img](https://i.imgur.com/TvEx7La.png)

```cmd
pytest --cov=. --cov-report=term-missing --cov-report=html
```

執行成功會產生一個 htmlcov 資料夾, 打開底下的 `index.html`

![img](https://i.imgur.com/t8M0O4J.png)
