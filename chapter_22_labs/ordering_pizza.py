# A local pizza shop is selling a large pizza for $9.99. Given the number of pizzas to order as input, output the subtotal for the pizzas, and then output the total after applying a sales tax of 6%.

# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f'Subtotal: ${yourValue:.2f}')

# Ex: If the input is:

# 3
# the output is:

# Subtotal: $29.97
# Total due: $31.77

num_pizzas = int(input())
lrg_pizza_cost = 9.99
sales_tax = 0.06
# Calculate subtotal for pizzas
subtotal = num_pizzas * lrg_pizza_cost
# Calculate total with tax
total_due = subtotal * (1 + sales_tax)
# Display Subtotal: $XX.XX
print(f'Subtotal: ${subtotal:.2f}')
# Display Total due: $XX.XX
print(f'Total due: ${total_due:.2f}')