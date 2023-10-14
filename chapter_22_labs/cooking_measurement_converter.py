# (1) Prompt the user for the number of cups of lemon juice, water, and agave nectar needed to make lemonade. Prompt the user to specify the number of servings the recipe yields. Output the ingredients and serving size.

#   (2) Prompt the user to specify the desired number of servings. Adjust the amounts of each ingredient accordingly, and then output the ingredients and serving size.

# (3) Convert the ingredient measurements from (2) to gallons. Output the ingredients and serving size. Note: There are 16 cups in a gallon.

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings_recipe_yields = float(input('How many servings does this make?\n'))
print()
print(f'Lemonade ingredients - yields {servings_recipe_yields:.2f} servings')
print(f'{lemon_juice_cups:.2f} cup(s) lemon juice')
print(f'{water_cups:.2f} cup(s) water')
print(f'{agave_nectar_cups:.2f} cup(s) agave nectar')
print()
desired_servings_amt = float(input('How many servings would you like to make?\n'))
print()
amt_to_multiply_by = desired_servings_amt / servings_recipe_yields
lemon_juice_cups *= amt_to_multiply_by
water_cups *= amt_to_multiply_by
agave_nectar_cups *= amt_to_multiply_by

print(f'Lemonade ingredients - yields {desired_servings_amt:.2f} servings')
print(f'{lemon_juice_cups:.2f} cup(s) lemon juice')
print(f'{water_cups:.2f} cup(s) water')
print(f'{agave_nectar_cups:.2f} cup(s) agave nectar')
print()
lemon_juice_gallons = lemon_juice_cups / 16
water_gallons = water_cups / 16
agave_nectar_gallons = agave_nectar_cups / 16

print(f'Lemonade ingredients - yields {desired_servings_amt:.2f} servings')
print(f'{lemon_juice_gallons:.2f} gallon(s) lemon juice')
print(f'{water_gallons:.2f} gallon(s) water')
print(f'{agave_nectar_gallons:.2f} gallon(s) agave nectar')