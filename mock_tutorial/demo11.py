import my_user
from unittest.mock import patch

with patch('__main__.my_user', autospec=True) as user:
    print(
        user.get_today()
    )
    print(
        user.get_users()
    )

    # AttributeError: Mock object has no attribute 'not_this_func'
    # user.not_this_func()
