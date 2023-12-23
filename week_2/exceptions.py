import sys
try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print('Inputs must be ints or floats')
    sys.exit(1)

try:
    result = x / y
    print(f'{x} / {y} = {result}')
except ZeroDivisionError:
    print('Cannot divide by zero')
    sys.exit(1)