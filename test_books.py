import pytest

from books import Book


def test_book_initialization():
    """Test the Book object"""
    # create book instance with all moduls
    book = Book(isbn = 2523252326, title = "Python", author = "mejoltny shibaha", total_book_copies= 10)
    assert book.isbn == 2523252326
    assert book.title == "Python"
    assert book.author == "mejoltny shibaha"
    assert book.total_book_copies == 10

    # create book instance without pass total_book_copies
    book = Book(isbn = 2523252327, title = "Java", author = "morkel holy")
    assert book.isbn == 2523252327
    assert book.title == "Java"
    assert book.author == "morkel holy"
    assert book.total_book_copies == 1

    # create book instance with passing string in isbn
    book = Book(isbn = "2523252328", title = "C", author = "albert")
    assert book.isbn == 2523252328
    assert book.title == "C"
    assert book.author == "albert"
    assert book.total_book_copies == 1

def test_borrow_book():
    library = Library()
    book1 = Book("123", "Test Book 1", "Author 1", 2)
    library.add_book(book1)
    
    # Test borrowing a book
    library.borrow_book("123")
    assert library.books["123"].borrow == 1
    
    # Test borrowing the last available copy
    library.borrow_book("123")
    assert library.books["123"].borrow == 2
    
    # Test borrowing a book with no available copies
    with pytest.raises(ValueError):
        library.borrow_book("123")
    
    # Test borrowing a non-existent book
    with pytest.raises(KeyError):
        library.borrow_book("456")