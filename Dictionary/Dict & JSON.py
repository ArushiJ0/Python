##Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.
import json
Book = {'title' :'a', 'author' :'b','year':2026, 'genre':'Fiction'}
book_json = json.dumps(Book)
print(book_json)
