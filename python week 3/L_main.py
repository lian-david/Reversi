from book import Book
from library import Library

def display_menu():
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Display all books")
    print("4. Search for a book by ISBN")
    print("5. Search for a book by author")
    print("6. Search for a book by price")
    print("7. Exit")

def handle_option(option):
    if option == 1:
        book = Book()
        book.set_book()
        library.add_book(book)
    elif option == 2:
        ISBN = input("Enter ISBN: ")
        if library.remove_book(ISBN):
            print("Book was successfully removed.")
        else:
            print("Book was not found.")
    elif option == 3:
        library.display_books()

    


EXIT_OPTION = 7
library = Library()

print("Welcome to the library")
print("--------------------------------")
display_menu()
option = int(input("Choose an option: "))
while option != EXIT_OPTION:
    handle_option(option)
    display_menu()
    option = int(input("Choose an option: "))
