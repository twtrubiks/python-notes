import pytest


@pytest.fixture(scope="function")
def hello():
    print("hello world")
    return 66


class Test_Demo6:
    def test_case1(self, hello):
        print("run test_case1")
        print(hello)
        assert 2 + 2 == 4

    def test_case2(self, hello):
        print("run test_case2")
        print(hello)
        assert 1 + 12 == 13

    def test_case3(self, hello):
        print("run test_case3")
        print(hello)
        assert 199 + 1 == 200


if __name__ == "__main__":
    pytest.main()
