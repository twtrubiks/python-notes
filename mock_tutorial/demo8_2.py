from unittest.mock import patch
from my_user import get_today
import datetime

mock_date = datetime.datetime(year=2021, month=10, day=10)

with patch('__main__.get_today', return_value = mock_date):
    # mock 成功
    print(
        get_today()
    )