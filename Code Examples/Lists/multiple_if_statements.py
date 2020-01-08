### 23 / 12 / 2019
### Colm O'Loughlin
### Using IF statements with lists

# Creating our shopping cart
shopping_cart = ['pens', 'stapler', 'paper', 'notes']

# Adding each item to an order
for item in shopping_cart:
    if item == 'pens':
        print("Sorry " + item + " is out of stock")
    else:
        print("Adding " + item + " to your order")

print("Order is complete")
