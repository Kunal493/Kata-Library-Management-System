from books import Book


class Library:
    def __init__(self):
        """
        Initialize a new library instance with an empty collection of books.
        """
        self.books = {}

    def add_book(self, book: Book):
        """
        Add a book to the library collection.
        :param book: An instance of the Book class.
        """
        if not isinstance(book, Book):
            raise TypeError("Invalid book type.")
        
        if book.isbn in self.books:
            self.books[book.isbn].total_book_copies += 1
        else:
            self.books[book.isbn] = book

    