# Write a program to calculate the cost to paint a wall. Amount of required paint is based on the wall area. Total cost includes paint and sales tax.

# Step 1: Read from input wall height, wall width, and cost of one paint can (floats). Calculate and output the wall's area to one decimal place

# Step 2: Calculate and output the amount of paint needed to three decimal places. One gallon of paint covers 350 square feet.

# Step 3: Calculate and output the number of 1 gallon cans needed to paint the wall. Extra paint may be left over.

# Step 4: Calculate and output the paint cost, sales tax of 7%, and total cost. Dollar values are output with two decimal places.

from math import ceil

wall_height = float(input())
wall_width = float(input())
paint_can_cost = float(input())
paint_can_coverage = 350

wall_area = wall_height * wall_width
paint_needed_gallons = wall_area / paint_can_coverage
paint_cans_needed = ceil(paint_needed_gallons)
tax_percent = 0.07
paint_cost = paint_can_cost * paint_cans_needed
tax_amt = paint_cost * tax_percent
total_cost = paint_cost + tax_amt

print(f'Wall area: {wall_area:.1f} sq ft')
print(f'Paint needed: {paint_needed_gallons:.3f} gallons')
print(f'Cans needed: {paint_cans_needed} can(s)')
print(f'Paint cost: ${paint_cost:.2f}')
print(f'Sales tax: ${tax_amt:.2f}')
print(f'Total cost: ${total_cost:.2f}')