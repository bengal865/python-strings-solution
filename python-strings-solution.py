# Mike Jenkins
# 03 MAY 20XX
# Python Strings SOLUTION

# Concatenation
first_name = 'Abraham'
last_name = 'Lincoln'
full_name = first_name + " " + last_name
print(f'My first name is {first_name}.')
print(f'My last name is {last_name}.')
print(f'My full name is {full_name}.')

# input(), float() and int() functions
city = input('Enter the name of the city in Michigan you live in:\n')
print('The user lives in the Michigan city of: ' + city)

# Using float() and input() functions together to get numeric input
hourly_wage = float(input('Enter your hourly wage: (Example: 12.25)\n'))
print(f'Mikey earns ${hourly_wage) an hour at Burger King.')

# Using int() and input() functions together to get numeric input
age = int(input('Enter your age: (Example: 21)\n'))
print(f"The user's age is: ${age)")

# Converting to upper- and lowercase characters using `upper()` and `lower()` methods

user_last_name = input('Please enter your last name in all lowercase characters: (Example: smith)\n').upper()
print(f'Your last name is: {user_last_name}')

user_city = input('Please enter in all UPPERCASE the name of the city you live in: (Example: DETROIT)\n').lower()
print(f'You live in: {user_city}')







