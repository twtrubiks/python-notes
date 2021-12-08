import pytest


@pytest.fixture()
def hello():
    print("hello world")
    return 66
