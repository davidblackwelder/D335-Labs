# Given two numbers that represent the lengths of a right triangle's legs (sides adjacent to the right angle), output the length of the third side (i.e. hypotenuse) with two digits after the decimal point.

# Note: To output the length of the hypotenuse with two digits after the decimal point, use:
# print(f'Hypotenuse: {side3:.2f}'), where side3 is the variable representing the length of the hypotenuse.

# Ex: If the input is:

# 3.0
# 4.0
# the output is:

# Hypotenuse: 5.00

import math
side1 = float(input())
side2 = float(input())

# calculate length of side3
side3 = math.sqrt(((side1 ** 2) + (side2 ** 2)))
# Display length of side 3 with two digits after the decimal point
print(f'Hypotenuse: {side3:.2f}')