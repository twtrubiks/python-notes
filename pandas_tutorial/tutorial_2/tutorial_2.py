import pandas as pd

'''
ref. https://pandas.pydata.org/pandas-docs/stable/merging.html

pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
'''

if __name__ == "__main__":
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
