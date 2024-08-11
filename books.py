class Book:
    def __init__(self,  isbn:int, title:str, author:str, total_book_copies:int = 1):
        #initialize a new book instance
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_book_copies = total_book_copies
        self.borrow = 0
