import pytest

from books import Book


def test_book_initialization():
    """Test the Book object"""
    book = Book(isbn = 2523252326, title = "Python", author = "mejoltny shibaha", total_book_copies= 10)
    assert book.isbn == 2523252326
    assert book.title == "Python"
    assert book.author == "mejoltny shibaha"
    assert book.total_book_copies == 10