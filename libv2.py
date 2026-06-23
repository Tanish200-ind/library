import json
import os


class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available

    def to_dict(self):
        return {"title": self.title, "author": self.author, "available": self.available}


def load():
    if not os.path.exists("lib.json"):
        return []
    with open("lib.json", "r") as file:
        data = json.load(file)
        return [Book(d.get("title", ""), d.get("author", ""), d.get("available", "available")) for d in data]


def save(books):
    with open("lib.json", "w") as file:
        json.dump([b.to_dict() for b in books], file, indent=2)


def add():
    books = load()
    title = input("enter book name to add:").strip()
    if any(b.title.strip().lower() == title.lower() for b in books):
        print("book already exists")
        return
    author = input("author of the book:").strip()
    book = Book(title, author, "available")
    books.append(book)
    save(books)
    print("Book saved")


def remove():
    books = load()
    title = input("enter book name to remove:").strip().lower()
    for book in books:
        if book.title.strip().lower() == title:
            books.remove(book)
            save(books)
            print("Book removed")
            return
    print("no such book in library")


def borrow():
    books = load()
    title = input("enter book name to borrow:").strip().lower()
    for book in books:
        if book.title.strip().lower() == title:
            if book.available == "available":
                book.available = "not available"
                save(books)
                print("You borrowed the book")
                return
            else:
                print("book is not available")
                return
    print("no such book in library")


def retrn():
    books = load()
    title = input("enter book name to return:").strip().lower()
    for book in books:
        if book.title.strip().lower() == title:
            if book.available == "not available":
                book.available = "available"
                save(books)
                print("Book returned")
                return
            else:
                print("book was already available")
                return
    print("no such book in library")


if __name__ == "__main__":
    while True:
        print("\n1.add 2.remove 3.borrow 4.return 5.view 6.quit")
        choice = input("choice:").strip()
        if choice == "1":
            add()
        elif choice == "2":
            remove()
        elif choice == "3":
            borrow()
        elif choice == "4":
            retrn()
        elif choice == "5":
            books = load()
            for i, b in enumerate(books, 1):
                print(f"{i}. {b.title} by {b.author} - {b.available}")
        else:
            break
