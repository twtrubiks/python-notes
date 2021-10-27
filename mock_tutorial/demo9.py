from unittest.mock import Mock

user = Mock(spec=['fun1', 'fun2'])

print(
    user.fun1()
)

# AttributeError: Mock object has no attribute 'not_this_func'
# user.not_this_func()
