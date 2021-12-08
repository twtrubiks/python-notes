import pytest


@pytest.fixture(scope="class")
def hello1():
    print("hello world")


class Test_Demo7:
    def test_case1(self, hello1):
        print("run test_case1")
        assert 2 + 2 == 4

    def test_case2(self, hello1):
        print("run test_case2")
        assert 1 + 12 == 13

    def test_case3(self, hello1):
        print("run test_case3")
        assert 199 + 1 == 200


if __name__ == "__main__":
    pytest.main()
