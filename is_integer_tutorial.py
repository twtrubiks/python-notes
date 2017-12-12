# ref. https://docs.python.org/3.6/library/stdtypes.html#float.is_integer

import unittest

'''
float.is_integer()
Return True if the float is an integer
'''


def check_is_integer(number):
    result = float(number).is_integer()
    return result


class TestCase(unittest.TestCase):
    def test_case_1(self):
        result = check_is_integer(-2.00)
        self.assertTrue(result)

    def test_case_2(self):
        result = check_is_integer(12.00000)
        self.assertTrue(result)

    def test_case_3(self):
        result = check_is_integer(-3.1)
        self.assertFalse(result)

    def test_case_4(self):
        result = check_is_integer(1.100)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
