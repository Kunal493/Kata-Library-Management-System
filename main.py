from books import Book
from library import Library

def main():
    library = Library()

    # Adding books to the library
    try:
        book1 = Book(isbn=1234567890, title="Python Programming", author="John Doe", total_book_copies=5)
        book2 = Book(isbn=8987654321, title="Data Science", author="Jane Smith", total_book_copies=3)
        book3 = Book(isbn=1122334455, title="Machine Learning", author="Alex Johnson", total_book_copies=2)

        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        print("Books added to the library.")

    except ValueError as e:
        print(f"Error while adding books: {e}")

    # Borrowing a book
    try:
        library.borrow_book(1234567890)
        print("Borrowed 'Python Programming' successfully.")
    except (BookNotFoundException, NoAvailableCopiesException) as e:
        print(f"Error while borrowing book: {e}")

    # Display available books
    print("\nAvailable books in the library:")
    available_books = library.display_available_books()
    for book in available_books:
        print(f"Title: {book.title}, Author: {book.author}, Copies Available: {book.total_book_copies - book.borrow}")

    # Returning a book
    try:
        library.return_book(1234567890)
        print("Returned 'Python Programming' successfully.")
    except (BookNotFoundException, AllCopiesReturnedException) as e:
        print(f"Error while returning book: {e}")

if __name__ == "__main__":
    main()
