# (1) Prompt the user to input a food item name, price, and quantity. Output an itemized receipt.

# (2) Extend the program to prompt the user for a second item. Output an itemized receipt.

# (3) Extend again to output a third receipt that adds a mandatory 15% gratuity to the total cost. Output the total cost, the cost of gratuity, and the grand total.

item1_name = input('Enter food item name:\n')
item1_price = float(input('Enter item price:\n'))
item1_quantity = int(input('Enter item quantity:\n'))
item1_cost = item1_price * item1_quantity
print()
print('RECEIPT')
print(f'{item1_quantity} {item1_name} @ ${item1_price:.2f} = ${item1_cost:.2f}')
print(f'Total cost: ${item1_cost:.2f}')
print()
print()
item2_name = input('Enter second food item name:\n')
item2_price = float(input('Enter item price:\n'))
item2_quantity = int(input('Enter item quantity:\n'))
item2_cost = item2_price * item2_quantity
total_cost = item1_cost + item2_cost
gratuity = 0.15
tip_amount = total_cost * gratuity
total_cost_with_tip = total_cost + tip_amount

print()
print('RECEIPT')
print(f'{item1_quantity} {item1_name} @ ${item1_price:.2f} = ${item1_cost:.2f}')
print(f'{item2_quantity} {item2_name} @ ${item2_price:.2f} = ${item2_cost:.2f}')
print(f'Total cost: ${total_cost:.2f}')
print()
print(f'15% gratuity: ${tip_amount:.2f}')
print(f'Total with tip: ${total_cost_with_tip:.2f}')
