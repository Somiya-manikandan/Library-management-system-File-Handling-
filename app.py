import streamlit as st
import os

FILE_NAME = "library.txt"

st.title("📚 Library Management System")

menu = ["Add Book", "View Books", "Search Book", "Issue Book", "Return Book"]
choice = st.sidebar.selectbox("Menu", menu)

# Add Book
if choice == "Add Book":
    st.subheader("Add New Book")
    book_id = st.text_input("Book ID")
    name = st.text_input("Book Name")
    author = st.text_input("Author Name")

    if st.button("Add"):
        with open(FILE_NAME, "a") as file:
            file.write(f"{book_id},{name},{author},Available\n")
        st.success("Book Added Successfully!")

# View Books
elif choice == "View Books":
    st.subheader("All Books")

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            books = file.readlines()
            for book in books:
                book_id, name, author, status = book.strip().split(",")
                st.write(f"ID: {book_id} | Name: {name} | Author: {author} | Status: {status}")
    else:
        st.warning("No books found.")

# Search Book
elif choice == "Search Book":
    st.subheader("Search Book")
    search_id = st.text_input("Enter Book ID")

    if st.button("Search"):
        found = False
        with open(FILE_NAME, "r") as file:
            for book in file:
                book_id, name, author, status = book.strip().split(",")
                if book_id == search_id:
                    st.success(f"Found: {book_id} | {name} | {author} | {status}")
                    found = True
                    break
        if not found:
            st.error("Book Not Found")

# Issue Book
elif choice == "Issue Book":
    st.subheader("Issue Book")
    issue_id = st.text_input("Enter Book ID")

    if st.button("Issue"):
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
            st.success("Book Issued Successfully!")
        else:
            st.error("Book Not Available or Not Found")

# Return Book
elif choice == "Return Book":
    st.subheader("Return Book")
    return_id = st.text_input("Enter Book ID")

    if st.button("Return"):
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
            st.success("Book Returned Successfully!")
        else:
            st.error("Book Not Found or Already Available")