# pandas_tutorial_1

第一個範例，是讓我發現 pandas 強大的地方，假設現在有一個需求，

我需要將下圖

|   |  color | name |
|---|:------:|:----:|
| 0 |   red  |   a  |
| 1 |  blue  |   a  |
| 2 |   red  |   a  |
| 3 |  blue  |   a  |
| 4 |   red  |   b  |
| 5 |  blue  |   b  |
| 6 |   red  |   b  |
| 7 |  blue  |   b  |
| 8 | yellow |   c  |
| 9 |  blue  |   c  |

轉換成

|  name |  blue | red | yellow | All |
|:-----:|:-----:|:---:|:------:|:---:|
|   a   |   2   |  2  |    0   |  4  |
|   b   |   2   |  2  |    0   |  4  |
|   c   |   1   |  0  |    1   |  2  |
|  All  |   5   |  4  |    1   |  10 |

這時候，我們該如何做呢？

這時候，就需要使用 pandas !!

第一步，先做原始資料

```python
df = pd.DataFrame(
        {
            'color': ['red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'yellow', 'blue'],
            'name': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c'],
        }
    )

print(df)
```

|   |  color | name |
|---|:------:|:----:|
| 0 |   red  |   a  |
| 1 |  blue  |   a  |
| 2 |   red  |   a  |
| 3 |  blue  |   a  |
| 4 |   red  |   b  |
| 5 |  blue  |   b  |
| 6 |   red  |   b  |
| 7 |  blue  |   b  |
| 8 | yellow |   c  |
| 9 |  blue  |   c  |

第二步，透過 pandas 中的 groupby 方法計算出數量

```python
df_size = df.groupby(['name', 'color']).size().reset_index(name='total')
print(df_size)
```

|   | name |  color | total |
|---|:----:|:------:|-------|
| 0 |   a  |  blue  |   2   |
| 1 |   a  |   red  |   2   |
| 2 |   b  |  blue  |   2   |
| 3 |   b  |   red  |   2   |
| 4 |   c  |  blue  |   1   |
| 5 |   c  | yellow |   1   |

第三步，透過 pandas 中的 pivot_table 方法畫出最終表格

```python
pd_pivot_table = pd.pivot_table(df_size, index=['name'], columns=['color'],aggfunc=[np.sum], fill_value=0, margins=True)
print(pd_pivot_table)
```

|       |  sum  |     |        |     |
|:-----:|:-----:|:---:|:------:|:---:|
|       | total |     |        |     |
| color |  blue | red | yellow | All |
|  name |       |     |        |     |
|   a   |   2   |  2  |    0   |  4  |
|   b   |   2   |  2  |    0   |  4  |
|   c   |   1   |  0  |    1   |  2  |
|  All  |   5   |  4  |    1   |  10 |

如果覺得 sum 和 total 很礙眼，可以使用

```python
print(pd_pivot_table['sum']['total'])
```

這樣是不是越來越像一個完整的表格（ 最終表格 ）了呢？

| color | blue | red | yellow | All |
|:-----:|:----:|:---:|:------:|:---:|
|  name |      |     |        |     |
|   a   |   2  |  2  |    0   |  4  |
|   b   |   2  |  2  |    0   |  4  |
|   c   |   1  |  0  |    1   |  2  |
|  All  |   5  |  4  |    1   |  10 |

基本上到這邊就完成了:relieved:

下方我要介紹的是假設前端需要這個表格的資料，

先將 row 顯示出來

```python
list_1 = [list(pd_pivot_table['sum']['total'].reset_index())]
print(list_1)
>>> [['name', 'blue', 'red', 'yellow', 'All']]
```

將每個 row 顯示出來

```python
list_2 = pd_pivot_table['sum']['total'].to_records()
print(list_2)
>>> [('a', 2, 2, 0,  4) ('b', 2, 2, 0,  4) ('c', 1, 0, 1,  2) ('All', 5, 4, 1, 10)]
list_2 = [list(p) for p in list_2]
print(list_2)
>>> [['a', 2, 2, 0, 4], ['b', 2, 2, 0, 4], ['c', 1, 0, 1, 2], ['All', 5, 4, 1, 10]]
```

最後將兩個 row 串起來

```python
print(list_1 + list_2)
>>> [['name', 'blue', 'red', 'yellow', 'All'], ['a', 2, 2, 0, 4], ['b', 2, 2, 0, 4], ['c', 1, 0, 1, 2], ['All', 5, 4, 1, 10]]
```

然後將他回傳給前端，這時候，前端就可以無痛串出如下圖的表格了 :satisfied:

|  name |  blue | red | yellow | All |
|:-----:|:-----:|:---:|:------:|:---:|
|   a   |   2   |  2  |    0   |  4  |
|   b   |   2   |  2  |    0   |  4  |
|   c   |   1   |  0  |    1   |  2  |
|  All  |   5   |  4  |    1   |  10 |
