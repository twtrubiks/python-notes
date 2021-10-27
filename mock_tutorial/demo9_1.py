import my_user
from unittest.mock import Mock

user = Mock(spec=my_user)
print(
    user.get_today()
)

print(
    user.get_users()
)

# AttributeError: Mock object has no attribute 'not_this_func'
# user.not_this_func()

user.attr_a = 123
print(user.attr_a)

