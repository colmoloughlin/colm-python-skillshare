### 23 / 12 / 2019
### Colm O'Loughlin
### Using a dictionary within a list

stock_items = []

# Make 50 blue pens

for blue_pen in range(0,50):
    new_blue_pen = {'colour' : 'blue', 'type' : 'ballpoint', 'price' : '1.99'}
    stock_items.append(new_blue_pen)

# Change price of first 5 pens

for blue_pen in stock_items[0:5]:
    if blue_pen['price'] == '1.99':
        blue_pen['price'] = '0.99'

for blue_pen in stock_items[0:5]:
    print(blue_pen)