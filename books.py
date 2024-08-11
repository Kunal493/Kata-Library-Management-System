class Book:
    def __init__(self, isbn: str, title: str, author: str, total_book_copies: int = 1):
        """
        Initialize a new book instance.
        
        :param isbn: ISBN number of the book (must be unique for each book)
        :param title: Title of the book
        :param author: Author of the book
        :param total_book_copies: Number of available copies (default is 1)
        :param borrow: Number of borrowed books (default is 0)
        """
        # Validate the parameters using the check_book_parameter function
        check_book_parameter(isbn, title, author, total_book_copies)
        
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_book_copies = total_book_copies
        self.borrow = 0
