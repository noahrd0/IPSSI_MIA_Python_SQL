# Library Management System

This project demonstrates the creation and management of a library system using Python. The project includes creating classes for books, students, and the library, and implementing various methods to manage library operations such as borrowing and returning books.

## Files

- `library_system.py`: Contains the Python code for the library management system.
- `library_data.txt`: Contains the sample data for the library books.

## Classes and Methods

### Book Class

Represents a book in the library.

#### Attributes

- `title` (str): The title of the book.
- `author` (str): The author of the book.
- `is_available` (bool): Indicates whether the book is available for borrowing.

#### Methods

- `__init__(self, title: str, author: str)`: Initializes a book object.
- `__str__(self)`: Returns a readable string representation of the book.

### Student Class

Represents a student who can borrow books from the library.

#### Attributes

- `name` (str): The name of the student.
- `borrowed_books` (list): A list of books borrowed by the student.

#### Methods

- `__init__(self, name: str)`: Initializes a student object.
- `borrow_book(self, book_title: str, library: Library)`: Tries to borrow a book by title from the library.
- `return_book(self, book_title: str, library: Library)`: Returns a borrowed book to the library.

### Library Class

Represents the library containing books and managing operations.

#### Attributes

- `books` (list): A list of books in the library.

#### Methods

- `__init__(self)`: Initializes a library object.
- `add_book(self, title: str, author: str)`: Adds a book to the library.
- `list_books(self) -> list`: Returns a list of strings showing each book's title, author, and availability.
- `load_books(self, file_path: str)`: Reads a file with book data and populates the library.
- `lend_book(self, book_title: str, student: Student) -> bool`: Lends a book to a student if it’s available and returns True. Returns False if the book is unavailable.
- `accept_return(self, book_title: str, student: Student)`: Accepts a book being returned by a student and updates its availability.
- `search_book(self, query: str) -> list`: Returns a list of books matching the search query in title or author.
- `save_books(self, file_path: str)`: Writes all books and their availability to a file.

## Sample Data

The `library_data.txt` file contains the following sample data:

```
1984,George Orwell,False
To Kill a Mockingbird,Harper Lee,True
The Great Gatsby,F. Scott Fitzgerald,True
Pride and Prejudice,Jane Austen,True
The Catcher in the Rye,J.D. Salinger,True
The Hobbit,J.R.R. Tolkien,True
Moby Dick,Herman Melville,True
War and Peace,Leo Tolstoy,True
The Odyssey,Homer,True
Crime and Punishment,Fyodor Dostoevsky,True
```

## How to Run

1. Ensure you have Python installed on your system.
2. Place the `library_system.py` and `library_data.txt` files in the same directory.
3. Run the script using the command:

```sh
python library_system.py
```

### Features

- **View all books**: Lists all books in the library with their availability status.
- **Search for a book**: Allows searching for books by title or author.
- **Add a new book**: Adds a new book to the library.
- **Borrow a book**: Allows a student to borrow a book if it is available.
- **Return a book**: Allows a student to return a borrowed book.
- **Save and exit**: Saves the current state of the library and exits the program.

## Additional Information

- The library system enforces a borrowing limit of 3 books per student.
- The library data is saved to `library_data.txt` upon exiting the program.