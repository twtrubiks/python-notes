# pandas_tutorial

[pandas](https://pandas.pydata.org/) 真的非常的強大，這邊會記錄以及介紹一些我有用過的方法，

* [pandas_tutorial_1](https://github.com/twtrubiks/python-notes/tree/master/pandas_tutorial/tutorial_1) - 透過 `pivot_table` 完成表格

* [pandas_tutorial_2](https://github.com/twtrubiks/python-notes/tree/master/pandas_tutorial/tutorial_2) - 透過 pandas 把玩 `inner join` `outer join` `left join` `right join`


## 其他筆記

[pandas.date_range](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html)

```python
import pandas as pd
from datetime import date

>>> start_date = date(2022, 3, 1)
>>> end_date = date(2022, 3, 8)
>>> pd.date_range(start_date, end_date).date
array([datetime.date(2022, 3, 1), datetime.date(2022, 3, 2),
       datetime.date(2022, 3, 3), datetime.date(2022, 3, 4),
       datetime.date(2022, 3, 5), datetime.date(2022, 3, 6),
       datetime.date(2022, 3, 7), datetime.date(2022, 3, 8)], dtype=object)
```

## Reference

* [pandas](https://pandas.pydata.org/)
