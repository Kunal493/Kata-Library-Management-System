# Kata-Library-Management-System
# Library Management System

## Overview

This project is a simple Library Management System that allows users to manage a collection of books. The system provides functionality to add books, borrow books, return books, and view available books in the library. It is built using Python, with a focus on clean, maintainable code, and error handling.

##Features

Book Management: Add and search for books in the library.
Borrow and Return: Track the borrowing and returning of books by library members.
Exception Handling: Robust error handling for common issues like book unavailability.
Testing: Unit tests to ensure the reliability and stability of the system.

## Project Structure

The project is organized into the following files:
Kata Library Management System/
│
├── .git/                   # Git repository metadata
├── .pytest_cache/          # Pytest cache directory
├── .vscode/                # VSCode workspace settings
├── __pycache__/            # Python cache files
├── books.py                # Module for managing book-related operations
├── exception_handling.py   # Module for handling exceptions
├── library.py              # Main library management logic
├── test_books.py           # Unit tests for the books module
├── test_library.py         # Unit tests for the library management system
└── requirements.txt        # List of dependencies

## Requirements

- Python 3.2 or higher
- `pytest` for testing

For Run Install dependencies:

If you don't have pytest installed, you can install it using pip:

bash
pip install pytest
