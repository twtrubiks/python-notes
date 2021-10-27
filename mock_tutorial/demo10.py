import my_user
from unittest.mock import create_autospec

user = create_autospec(my_user)
print(
    user.get_today()
)

print(
    user.get_users()
)


# AttributeError: Mock object has no attribute 'not_this_func'
# user.not_this_func()
