# ref.
# https://docs.python.org/3.9/library/decimal.html

import decimal

# python3
# Solve the accuracy problem

def exmaple_1():
    print(decimal.Decimal(3.499))
    print(decimal.Decimal('3.499')) # It is recommended to use str.

def exmaple_2():
    float_a = 1.0
    float_b = 0.8
    print('float_a-float_b = ', float_a - float_b)

def exmaple_2_fix():
    decimal_a = decimal.Decimal('1.0')
    decimal_b = decimal.Decimal('0.8')
    print('float_decimal-float_decimal = ', decimal_a - decimal_b)

def exmaple_3():
    print(round(1.5))
    print(round(2.5))

def exmaple_3_fix():
    # ROUND_HALF_UP is the same as Python 2.X's old behavior.
    print(decimal.Decimal('1.5').quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_HALF_UP))
    print(decimal.Decimal('2.5').quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_HALF_UP))

def exmaple_4():
    # ROUND_HALF_UP is the same as Python 2.X's old behavior.
    print(decimal.Decimal(3.501).quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_HALF_UP))
    print(decimal.Decimal('3.501').quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_HALF_UP))
    print(decimal.Decimal(3.4999).quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_HALF_UP))
    print(decimal.Decimal('3.4999').quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_HALF_UP))

def exmaple_5():
    print(decimal.Decimal(3.501).quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_DOWN))
    print(decimal.Decimal('3.501').quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_DOWN))
    print(decimal.Decimal(3.4999).quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_DOWN))
    print(decimal.Decimal('3.4999').quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_DOWN))

def exmaple_6():
    a = 1.0-0.8
    print(decimal.Decimal(a))
    print(decimal.Decimal(a).quantize(decimal.Decimal('1.'),rounding=decimal.ROUND_DOWN))

if __name__ == "__main__":
    exmaple_1()
    # exmaple_2()
    # exmaple_2_fix()
    # exmaple_3()
    # exmaple_3_fix()
    # exmaple_4()
    # exmaple_5()
    # exmaple_6()





