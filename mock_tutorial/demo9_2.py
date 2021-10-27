import my_user
from unittest.mock import Mock

user = Mock(spec_set=my_user)
print(
    user.get_today()
)

print(
    user.get_users()
)

# AttributeError: Mock object has no attribute 'attr_a'
# user.attr_a = 123