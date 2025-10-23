# library_system.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        Book.__init__(self, title, author)  # Explicitly call base class __init__
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        Book.__init__(self, title, author)  # Explicitly call base class __init__
        self.page_count = page_count


class Library:
    def __init__(self):
        self.books = []  # Initialize books list

    def add_book(self, book):
        self.books.append(book)  # Add book to the list

    def list_books(self):
        for book in self.books:
            if type(book).__name__ == "EBook":
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif type(book).__name__ == "PrintBook":
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")