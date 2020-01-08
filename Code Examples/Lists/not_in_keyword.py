### 23 / 12 / 2019
### Colm O'Loughlin
### Checking if a value is not in a list

# Admin users
admin_users = ['colm', 'frank']

#Ask for username
username = input("Please enter your username")

#Check if username is admin
if username not in admin_users:
    print("User is not an admin")
else:
    print("Hey admin!")
