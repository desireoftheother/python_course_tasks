# Задача 2: Збереження помилок у пам'яті
#
# Створіть контекстний менеджер, який перехоплює всі винятки, які виникають у блоку коду, який він обгортає, і повертає їх список (у серіалізованому в рядок форматі)
# Якщо винятків не виникає, поверніть пустий список

# Hint: думаю, зручніше буде тут використати декоратор @contextmanager

class Book:
    num_of_books = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.num_of_books += 1


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = list()

    def print_books(self):
        print(f'Number of books written by {self.name}: {len(self.books)}')
        print('Book names:')
        for book in self.books:
            print(book.name)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = list()
        self.authors = list()

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        author.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

Stephen_King = Author('Stephen King', 'Portland', '1947')
Shinning = Book('The Shinning', 1977, Stephen_King)
It = Book('It', 1986, Stephen_King)

Stephen_King.print_books()
