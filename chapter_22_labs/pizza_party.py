# Given the number of people attending a pizza party, output the number of needed pizzas and total cost. For the calculation, assume that people eat 2 slices on average and each pizza has 12 slices and costs $14.95.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'Cost: ${cost:.2f}')

# Hint: Use the ceil() function from the math module to round up the number of pizzas so that enough pizzas are ordered.

# Ex: If the input is:

# 4
# the output is:

# Pizzas: 1
# Cost: $14.95

import math

num_people = int(input())

pizza_slices = 12
pizza_cost = 14.95
avg_slices_eaten = 2

num_pizzas_to_order = math.ceil((num_people * avg_slices_eaten) / pizza_slices)
order_cost = num_pizzas_to_order * pizza_cost

print('Pizzas:', num_pizzas_to_order)
print(f'Cost: ${order_cost:.2f}')