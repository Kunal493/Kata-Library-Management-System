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
    
    