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
    