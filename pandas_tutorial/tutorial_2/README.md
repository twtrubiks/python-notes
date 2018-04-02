# pandas_tutorial_2

* [Youtube Tutorial Part2 - pandas tutorial ( join )](xxx) - 等待新增

這個範例主要是要和大家介紹，

用 pandas 也可以玩像是 database 中的 `inner join` `outer join` `left join` `right join`，

大家可以直接執行程式碼（ 或看影片教學 ），這樣會比較了解:smile:

```python
df_1 = pd.DataFrame(
        {
            'id': [1, 2, 3],
            'key': ['a', 'b', 'c'],
        }
    )
print('=== df_1 ===')
print(df_1)

df_2 = pd.DataFrame(
    {
        'key': ['b', 'c', 'd'],
        'value': ['b_value', 'c_value', 'd_value'],
    }
)
print('=== df_2 ===')
print(df_2)

# inner join
pd_inner_join = pd.merge(df_1, df_2, how='inner', on='key', sort=True)
print('=== inner_join ===')
print(pd_inner_join)

# left join
pd_left_join = pd.merge(df_1, df_2, how='left', on='key', sort=True)
print('=== left_join ===')
print(pd_left_join)

# right join
pd_right_join = pd.merge(df_1, df_2, how='right', on='key', sort=True)
print('=== right_join ===')
print(pd_right_join)

# outer join
pd_outer_join = pd.merge(df_1, df_2, how='outer', sort=True)
print('=== outer_join ===')
print(pd_outer_join)
```
