# library_system.py

class Book:
    def __init__(self, title, author):
        """Initialize base book attributes"""
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize eBook with additional file_size attribute"""
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize print book with additional page_count attribute"""
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self):
        """Initialize library with empty books list"""
        self.books = []

    def add_book(self, book):
        """Add a book to the library"""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library with EXACT output format"""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")