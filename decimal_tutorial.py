import decimal

# Solve the accuracy problem

if __name__ == "__main__":
    float_a = 1.0
    float_b = 0.8
    print('float_a-float_b = ', float_a - float_b)

    decimal_a = decimal.Decimal('1.0')
    decimal_b = decimal.Decimal('0.8')
    print('float_decimal-float_decimal = ', decimal_a - decimal_b)
