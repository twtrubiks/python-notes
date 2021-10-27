import datetime
from unittest.mock import Mock

print(datetime.datetime.today())

# start mock
mock_date = datetime.datetime(year=2021, month=10, day=10)
datetime = Mock()

# mock .today()
datetime.datetime.today.return_value = mock_date
print(datetime.datetime.today())