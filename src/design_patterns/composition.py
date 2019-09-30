"""Composition has-a/whole-part relationship """


class BookSelf:

    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookSelf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Python")
book2 = Book("Java")

self = BookSelf(book, book2)
print(self)  # BookSelf with 2 books
print(self.books)  # This is how we can check the BookSelf storage
