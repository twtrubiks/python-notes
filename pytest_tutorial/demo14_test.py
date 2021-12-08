from time import sleep

import pytest

# pytest.ini

# @pytest.mark.name_of_the_mark decorator will trigger an error.
# @pytest.mark.slwo
@pytest.mark.slow
def test_super_slow_test():
    sleep(2)


def test_a():
    assert 1 == 1


if __name__ == "__main__":
    pytest.main()
