import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError) as excinfo:
        1 / 0

    assert excinfo.type == ZeroDivisionError
    assert "division by zero" in str(excinfo.value)


if __name__ == "__main__":
    pytest.main()
