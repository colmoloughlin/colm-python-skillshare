### 07 / 01 / 2020
### Colm O'Loughlin
### Using a dictionary within a list

my_ordered_car = {
    'type' : 'standard four door saloon',
    'extras' : ['alloy wheels', 'climate control', 'leather heated seats'],
}

# Print order summary

print("The car you ordered is a " + my_ordered_car['type'] + " with the following extras:")

for extra in my_ordered_car['extras']:
    print("\t" + extra)