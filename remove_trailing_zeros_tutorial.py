# ref. https://docs.python.org/3.6/library/decimal.html

import decimal
import unittest


# ref. `to_integral` identical to the `to_integral_value`
# Round to the nearest integer

# ref.  `normalize(x)` Reduces x to its simplest form.


def remove_trailing_zeros(**kwargs):
    number = kwargs.get('number')
    number = decimal.Decimal(str(number))

    if number == number.to_integral_value():
        result = number.to_integral_value()
    else:
        result = number.normalize()
    return result


class TestCase(unittest.TestCase):
    def test_case_1(self):
        result = remove_trailing_zeros(number=0.00)
        self.assertEqual(result, decimal.Decimal('0'))

    def test_case_2(self):
        result = remove_trailing_zeros(number=3.02)
        self.assertEqual(result, decimal.Decimal('3.02'))

    def test_case_3(self):
        result = remove_trailing_zeros(number=1.10)
        self.assertEqual(result, decimal.Decimal('1.1'))

    def test_case_4(self):
        result = remove_trailing_zeros(number=1.00)
        self.assertEqual(result, decimal.Decimal('1'))


if __name__ == "__main__":
    unittest.main()
