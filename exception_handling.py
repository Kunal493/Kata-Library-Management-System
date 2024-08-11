def check_book_parameter(isbn, title, author, total_book_copies):
    """
    Validate the parameters for creating book instance.
    """
    if not isinstance(title, str) or not title:
        raise ValueError("Title must be a non-empty string.")
    
    if not isinstance(author, str) or not author:
        raise ValueError("Author must be a non-empty string.")
    
    if not isinstance(isbn, str) or not isbn:
        raise ValueError("ISBN must be a non-empty string.")

    if not isinstance(total_book_copies, int) or total_book_copies < 0:
        raise ValueError("Number of copies must be a non-negative integer.")
    
