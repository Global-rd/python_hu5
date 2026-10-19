

class Author:

    def __init__(self, name:str, nationality:str):
        self.name = name
        self.nationality = nationality

    def __str__(self):
        return f"{self.name}"


class Book:

    def __init__(self, title: str, genre: str, author: Author):
        self.title = title
        self.genre = genre
        self.author = author

    def __str__(self):
        return f"{self.author.name} - {self.genre} -  {self.title}"


class Library:

    def __init__(self, name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        print(f"Available books in {self.name}")
        for book in self.books:
            print(book)

    def remove_books(self, title: str):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return
        print(f"No book found with this title: {title}")


author_1 = Author("X", "hungarian")
author_2 = Author("Y", "ukranian")

print(author_1.name)
print(author_2.nationality)


book_1 = Book("How to get away with murder", "crime", author_1)
book_2 = Book("Testing", "crime", author_2)



print(book_1.author.name)

lib = Library("Szavó Ervin Városi Könyvtár")

print(lib.books)

lib.add_book(book_1)
lib.add_book(book_2)

lib.list_books()

print(lib.books)

lib.remove_books("Testing")

print(lib.books)
