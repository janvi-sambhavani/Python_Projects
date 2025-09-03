import json

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn


class Library:
    def __init__(self):
        self.books = []
        self.filename = "library.json"
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                for b in data:
                    self.books.append(Book(b["title"], b["author"], b["isbn"]))
        except FileNotFoundError:
            pass

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump([b.__dict__ for b in self.books], f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn):
        self.books = [b for b in self.books if b.isbn != isbn]
        self.save_books()

    def search_book(self, title):
        return [b.__dict__ for b in self.books if title.lower() in b.title.lower()]


if __name__ == "__main__":
    lib = Library()

    while True:
        print("\n1. Add Book\n2. Remove Book\n3. Search Book\n4. View All Books\n5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            book = Book(title, author, isbn)
            lib.add_book(book)
            print("Book added successfully!")

        elif choice == "2":
            isbn = input("Enter ISBN of book to remove: ")
            lib.remove_book(isbn)
            print("Book removed successfully!")

        elif choice == "3":
            title = input("Enter title to search: ")
            results = lib.search_book(title)
            if results:
                print("Search results:", results)
            else:
                print("No book found.")

        elif choice == "4":
            if lib.books:
                print("Books in library:")
                for b in lib.books:
                    print(b.__dict__)
            else:
                print("Library is empty.")

        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")