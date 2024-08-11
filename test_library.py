import pytest

from books import Book
from library import Library


def test_add_book():
    library = Library()
    book1 = Book("123", "Test Book 1", "Author 1", 3)
    book2 = Book("456", "Test Book 2", "Author 2", 1)
    
    # Test adding a new book
    library.add_book(book1)
    assert len(library.books) == 1
    assert library.books["123"].total_book_copies == 3
    
    # Test adding a copy of an existing book
    library.add_book(book1)
    assert library.books["123"].total_book_copies == 4
    
    # Test adding another new book
    library.add_book(book2)
    assert len(library.books) == 2
    assert library.books["456"].total_book_copies == 1

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

def test_return_book():
    library = Library()
    book1 = Book("123", "Test Book 1", "Author 1", 2)
    library.add_book(book1)
    library.borrow_book("123")
    
    # Test returning a book
    library.return_book("123")
    assert library.books["123"].borrow == 0
    
    # Test returning a book with no borrowed copies
    with pytest.raises(ValueError):
        library.return_book("123")
    
    # Test returning a non-existent book
    with pytest.raises(KeyError):
        library.return_book("456")

def test_display_available_books():
    library = Library()
    book1 = Book("123", "Test Book 1", "Author 1", 2)
    book2 = Book("456", "Test Book 2", "Author 2", 1)
    library.add_book(book1)
    library.add_book(book2)
    
    # Test display of available books
    available_books = library.display_available_books()
    assert len(available_books) == 2
    
    # Test after borrowing a book
    library.borrow_book("123")
    available_books = library.display_available_books()
    assert len(available_books) == 2
    
    