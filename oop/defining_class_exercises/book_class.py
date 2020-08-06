# Create a Book class that contains three attributes. Ask for user input to create a book.


class Book:
    def __init__(self, title, cost, author):
        self.title = title
        self.cost = cost
        self.author = author


all_books = []
while True:
    title = input("Enter a title: ")
    if not title:
        break
    cost = float(input("Enter the cost of the book: "))
    author = input("Enter the author's name: ")

    all_books.append(Book(title, cost, author))

print(all_books)
