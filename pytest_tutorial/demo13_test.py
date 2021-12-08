import pytest


@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f():
    1 / 0


@pytest.mark.skip(reason="pass.....")
def test_s():
    1 / 0


if __name__ == "__main__":
    pytest.main()
