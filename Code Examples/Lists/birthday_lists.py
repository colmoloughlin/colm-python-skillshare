### 23 / 12/ 2019
### Author: Colm O'Loughlin
### How to Edit Lists

# Creating a list of months
birthday_months = ['spril', 'may', 'july', 'august', 'october', 'december']

# Print our list
print(birthday_months)

# Changing an element of our list
birthday_months[0] = 'april'

print(birthday_months)

# Using the append method to add to list
birthday_months.append('june')

print(birthday_months)

# Creating an empty list
birthday_months = []

print(birthday_months)

birthday_months.append('january')

print(birthday_months)

# Using the insert method to add to start of list
birthday_months.insert(0, 'march')

print(birthday_months)

# Using the delete statement to remove values from a list
del birthday_months[1]

print(birthday_months)