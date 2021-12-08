import pytest


@pytest.mark.parametrize(
    "input",
    (
        (1, 1, 2),
        (2, 2, 4),
        (3, 3, 6),
    ),
)
class Test_Demo11:
    def test_case1(self, input):
        print("run test_case1")
        print(input)
        assert input[0] + input[1] == input[2]


if __name__ == "__main__":
    pytest.main()
