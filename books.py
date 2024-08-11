class Book:
    def __init__(self, title, author, isbn, copies=1):
        #initialize all book moduls
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = copies