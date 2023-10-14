# (1) Prompt the user to enter two words and a number, storing each into separate variables. Then, output those three values on a single line separated by a space.

# (2) Output two passwords using a combination of the user input. Format the passwords as shown below.

# (3) Output the length of each password (the number of characters in the strings).

favorite_color = input()
favorite_flower = input()
favorite_number = input()

print(f'You entered: {favorite_color} {favorite_flower} {favorite_number}')

password1 = f'{favorite_color}_{favorite_flower}'
password2 = f'{favorite_number}{favorite_color}{favorite_number}'
len_password1 = len(password1)
len_password2 = len(password2)
print()
print(f'First password: {password1}')
print(f'Second password: {password2}')
print()
print(f'Number of characters in {password1}: {len_password1}')
print(f'Number of characters in {password2}: {len_password2}')
