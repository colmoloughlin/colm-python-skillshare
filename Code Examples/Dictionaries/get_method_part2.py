### 23 / 12 / 2019
### Colm O'Loughlin
### Editing & deleting values in a dictionary

### Replace value in dictionary
###terms = {'integer' : 'Is a number that contains a decimal place'}
###terms['integer'] = 'A whole number'

###print(terms.get('integer'))

### Remove key value pair in dictionary
terms = {'integer' : 'Is a number that contains a decimal place', 'string' : 'a sequence of characters'}

del terms['integer']

print(terms)