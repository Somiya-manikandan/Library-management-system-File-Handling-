import os

FILE_NAME = "library.txt"


def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{book_id},{name},{author},Available\n")

    print("Book added successfully!\n")



def view_books():
    if not os.path.exists(FILE_NAME):
        print("No books available.\n")
        return

    with open(FILE_NAME, "r") as file:
        books = file.readlines()

        if not books:
            print("No books available.\n")
        else:
            print("\nLibrary Books:")
            for book in books:
                book_id, name, author, status = book.strip().split(",")
                print(f"ID: {book_id} | Name: {name} | Author: {author} | Status: {status}")
            print()



def search_book():
    search_id = input("Enter Book ID to search: ")
    found = False

    with open(FILE_NAME, "r") as file:
        for book in file:
            book_id, name, author, status = book.strip().split(",")
            if book_id == search_id:
                print(f"Found: {book_id} | {name} | {author} | {status}\n")
                found = True
                break

    if not found:
        print("Book not found.\n")


def issue_book():
    issue_id = input("Enter Book ID to issue: ")
    updated_books = []
    found = False

    with open(FILE_NAME, "r") as file:
        for book in file:
            book_id, name, author, status = book.strip().split(",")
            if book_id == issue_id and status == "Available":
                updated_books.append(f"{book_id},{name},{author},Issued\n")
                found = True
            else:
                updated_books.append(book)

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_books)

    if found:
        print("Book issued successfully!\n")
    else:
        print("Book not available or not found.\n")


def return_book():
    return_id = input("Enter Book ID to return: ")
    updated_books = []
    found = False

    with open(FILE_NAME, "r") as file:
        for book in file:
            book_id, name, author, status = book.strip().split(",")
            if book_id == return_id and status == "Issued":
                updated_books.append(f"{book_id},{name},{author},Available\n")
                found = True
            else:
                updated_books.append(book)

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_books)

    if found:
        print("Book returned successfully!\n")
    else:
        print("Book not found or already available.\n")



while True:
    print("===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        print("Exiting program...")
        break
    else:

        print("Invalid choice! Try again.\n")
