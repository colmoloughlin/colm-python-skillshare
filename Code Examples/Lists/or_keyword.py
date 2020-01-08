### 23 / 12 / 2019
### Colm O'Loughlin
### Using the OR keyword to check values in a list

# Names registered
registered_names = ['colm', 'tara']

username = input("Please enter your username")

# Check if username already exists
if username in registered_names:
    print("Sorry, this name is already taken")
else:
    print("Welcome")
