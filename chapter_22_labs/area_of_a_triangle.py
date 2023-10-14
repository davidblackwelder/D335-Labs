# Using Heron's formula, you can calculate the area of a triangle if you know the lengths of all three sides. Given the length of each side of a triangle as input, calculate the area of the triangle using Heron's formula as follows:

# s = half of the triangle's perimeter
# area = the square root of s(s-a)(s-b)(s-c), where a, b, and c are each sides of the triangle.
# Hint: Use the sqrt() function from the math module to calculate the square root.

# Output the floating-point value of the area with three digits after the decimal point, which can be achieved as follows:
# print(f'The area of the triangle is: {your_value:.3f}')

# Ex: If the input for a, b, and c is:

# 3.0
# 4.0
# 5.0
# the output is:

# The area of the triangle is: 6.000

import math
a = float(input())
b = float(input())
c = float(input())
s = (a + b + c) / 2

area = math.sqrt((s * ((s-a) * (s-b) * (s-c))))

print(f'The area of the triangle is: {area:.3f}')