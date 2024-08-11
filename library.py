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

    def borrow_book(self, isbn: str):
        """
        Borrow a book from the library.       
        :param isbn: The ISBN number of the book to be borrowed.
        """
        if isbn not in self.books:
            raise KeyError("Book not found in the library.")
        
        book = self.books[isbn]
        if book.total_book_copies - book.borrow > 0:
            book.borrow += 1
        else:
            raise ValueError("No available copies to borrow.")

    def return_book(self, isbn: str):
        """
        Return a book to the library.
        :param isbn: The ISBN number of the book to be returned.
        """
        if isbn not in self.books:
            raise KeyError("Book not found in the library.")
        
        book = self.books[isbn]
        if book.borrow > 0:
            book.borrow -= 1
        else:
            raise ValueError("All borrowed copies have already been returned.")

    def display_available_books(self):
        """
        Display all available books in the library.       
        :return: A list of Book instances that have available copies.
        """
        return [book for book in self.books.values() if book.total_book_copies - book.borrow > 0]