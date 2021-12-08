import pytest


@pytest.fixture(scope="function", params=[[3, 1, 4], [99, 2, 101], [1, 1, 2]])
def data(request):
    yield request.param


class Test_Demo10:
    def test_case1(self):
        print("run test_case1")
        assert 2 + 2 == 4

    def test_case2(self):
        print("run test_case2")
        assert 1 + 12 == 13

    def test_case3(self):
        print("run test_case3")
        assert 199 + 1 == 200

    def test_case4(self, data):
        print("run test_case4")
        assert data[0] + data[1] == data[2]


if __name__ == "__main__":
    pytest.main()
