import pytest


def setup_function():
    print("setup...")


def teardown_function():
    print("teardown...")


def test_case1():
    print("run test_case1")
    assert 2 + 2 == 4


def test_case2():
    print("run test_case2")
    assert 1 + 12 == 13


def test_case3():
    print("run test_case3")
    assert 199 + 1 == 200
