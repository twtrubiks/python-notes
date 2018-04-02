import numpy as np
import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame(
        {
            'color': ['red', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'blue', 'yellow', 'blue'],
            'name': ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c'],
        }
    )
    print(df)

    df_size = df.groupby(['name', 'color']).size().reset_index(name='total')
    print(df_size)

    pd_pivot_table = pd.pivot_table(df_size, index=['name'], columns=['color'],
                                    aggfunc=[np.sum], fill_value=0, margins=True)
    print(pd_pivot_table)
    print(pd_pivot_table['sum']['total'])

    list_1 = [list(pd_pivot_table['sum']['total'].reset_index())]
    print(list_1)
    list_2 = pd_pivot_table['sum']['total'].to_records()
    print(list_2)
    list_2 = [list(p) for p in list_2]
    print(list_2)
    print(list_1 + list_2)
