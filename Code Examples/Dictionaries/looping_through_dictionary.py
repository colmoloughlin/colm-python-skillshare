### 23 / 12 / 2019
### Colm O'Loughlin
### Looping through a dictionary

birthday_months = {
    'colm' : 'april',
    'ste' : 'july',
    'tara' : 'june',
}

for name, birthday in birthday_months.items():
    print("\nName: " + name)
    print("Birthday Month: " + birthday)

### Looping through key value pairs
book_1 = {
    'name' : 'elon musk',
    'author' : 'ashlee vance',
    'price' : '14.99',
    'publisher' : 'virgin books',
}

for key, value in book_1.items():
    print("\nKey: " + key)
    print("Value: " + value)

### Other ways to loop through a dictionary

birthday_months_2 = {
    'colm' : 'april',
    'ste' : 'june',
    'tara' : 'june',
}

for name in birthday_months_2.keys():
    print(name.title())

for months in birthday_months_2.values():
    print(months.title())

### Does not print duplicates
for months in set(birthday_months_2.values()):
    print(months.title())

### Using a dictionary as a list

book_0 = {'title' : 'elon musk', 'author' : 'ashlee vance', 'price' : '14.99', 'publisher' : 'virgin books'}
book_1 = {'title' : 'my life', 'author' : 'colm oloughlin', 'price' : '200.50', 'publisher' : 'awkward turtle records'}
book_2 = {'title' : 'hello', 'author' : 'lionel rich tea', 'price' : 'priceless', 'publisher' : 'sony'}

books = [book_0, book_1, book_2]

for book in books:
    print(book)