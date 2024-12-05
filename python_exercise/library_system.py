Library = ""

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} is {'available' if self.is_available else 'not available'}."
    
class Student:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_title: str, library: Library):
        for book in library.books:
            if book.title == book_title and book.is_available:
                book.is_available = False
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed '{book_title}'")
                return True
        print(f"'{book_title}' is not available")
        return False

    def return_book(self, book_title: str, library: Library):
        for book in self.borrowed_books:
            if book.title == book_title:
                book.is_available = True
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book_title}'")
                return True
        print(f"{self.name} does not have '{book_title}'")
        return False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str):
        book = Book(title, author)
        self.books.append(book)

    def list_books(self) -> list:
        list_books = []
        for book in self.books:
            list_books.append(book.__str__())
        return list_books
    
    # def load_books(self, file_path: str):
    #     try:
    #         with open(file_path, 'r') as file:
    #             for line in file:
    #                 title, author = line.strip().split(',')
    #                 self.add_book(title, author)
    #     except Exception as e:
    #         print(f"An error occurred: {e}")

    def load_books(self, file_path: str):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    title, author, is_available = line.strip().split(',')
                    book = Book(title, author)
                    book.is_available = is_available == 'True'
                    self.books.append(book)
        except Exception as e:
            print(f"An error occurred: {e}")

    def lend_book(self, book_title: str, student: Student) -> bool:
        for book in student.borrowed_books:
            if book.title == book_title:
                print(f"{student.name} has already borrowed '{book_title}'")
                return False
        for book in self.books:
            if book.title == book_title and book.is_available:
                book.is_available = False
                student.borrowed_books.append(book)
                print(f"{student.name} borrowed '{book_title}'")
                return True
        print(f"'{book_title}' is not available")
        return False
    
    def accept_return(self, book_title: str, student: Student):
        for book in student.borrowed_books:
            if book.title == book_title:
                book.is_available = True
                student.borrowed_books.remove(book)
                print(f"{student.name} returned '{book_title}' to the library")
        print(f"{student.name} does not have '{book_title}' to return")

    def search_book(self, query: str) -> list:
        search_results = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                search_results.append(book.__str__())
        return search_results
    
    def save_books(self, file_path: str):
        try:
            with open(file_path, 'w') as file:
                for book in self.books:
                    file.write(f"{book.title},{book.author},{book.is_available}\n")
        except Exception as e:
            print(f"An error occurred: {e}")


class Student:
    def __init__(self, name: str):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_title: str, library: Library):
        if len(self.borrowed_books) >= 3:
            print(f"{self.name} has reached the borrowing limit of 3 books.")
            return False
        for book in library.books:
            if book.title == book_title and book.is_available:
                book.is_available = False
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed '{book_title}'")
                return True
        print(f"'{book_title}' is not available")
        return False

    def return_book(self, book_title: str, library: Library):
        for book in self.borrowed_books:
            if book.title == book_title:
                book.is_available = True
                self.borrowed_books.remove(book)
                print(f"{self.name} returned '{book_title}'")
                return True
        print(f"{self.name} does not have '{book_title}'")
        return False

def run_library_system():
    library = Library()
    library.load_books('library_data.txt')
    student_dict = {}

    while True:
        print("\nLibrary Management System")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Add a new book")
        print("4. Borrow a book")
        print("5. Return a book")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nBooks in library:")
            for book in library.list_books():
                print(book)
        elif choice == '2':
            query = input("Enter the title or author to search: ")
            results = library.search_book(query)
            if results:
                print("\nSearch results:")
                for result in results:
                    print(result)
            else:
                print("No books found.")
        elif choice == '3':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            library.add_book(title, author)
            print(f"Book '{title}' by {author} added to the library.")
        elif choice == '4':
            student_name = input("Enter your name: ")
            student = student_dict.get(student_name)
            if not student:
                student = Student(student_name)
                student_dict[student_name] = student
            book_title = input("Enter the book title to borrow: ")
            student.borrow_book(book_title, library)
        elif choice == '5':
            student_name = input("Enter your name: ")
            student = student_dict.get(student_name)
            if not student:
                print(f"{student_name} is not registered.")
                continue
            book_title = input("Enter the book title to return: ")
            student.return_book(book_title, library)
        elif choice == '6':
            library.save_books('library_data.txt')
            print("Library data saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

run_library_system()