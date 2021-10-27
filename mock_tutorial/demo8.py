from unittest.mock import patch
import my_user
import datetime

mock_date = datetime.datetime(year=2021, month=10, day=10)

# 比較好的寫法
with patch('my_user.get_today', return_value = mock_date):
    # mock 成功
    print(
        my_user.get_today()
    )