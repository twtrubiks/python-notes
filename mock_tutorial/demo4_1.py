from unittest.mock import Mock


mock = Mock()
values = {'a': 1, 'b': 2, 'c': 3}
def side_effect(arg):
    return values[arg]

mock.side_effect = side_effect
print(
    mock('a'), mock('b'), mock('c')
)
# (1, 2, 3)


mock_1 = Mock()
mock_1.side_effect = [5, 4, 3, 2, 1]
print(
    mock_1(), mock_1(), mock_1()
)
# (5, 4, 3)