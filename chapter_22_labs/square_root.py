# Given a floating-point number as input, output the square root of the given number.

# Hint: Use the appropriate function from the math module to perform the operation.

# Ex: If the input is:

# 9.0
# the output is:

# Sqrt: 3.0

import math

user_num = float(input())
sqrt_num = math.sqrt(user_num)

print(f'Sqrt: {sqrt_num}')