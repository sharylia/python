import json
from typing import List, Optional

# Класс Book
class Book:
    def __init__(self, title: str, author: str, year: int, genre: str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    # Представление объекта книги в виде строки
    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year}) - {self.genre}"

    # Метод для сравнения двух книг
    def __eq__(self, other) -> bool:
        if isinstance(other, Book):
            return (self.title == other.title and self.author == other.author and 
                    self.year == other.year and self.genre == other.genre)
        return False

# Класс Reader
class Reader:
    def __init__(self, name: str, reader_id: int):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books: List[Book] = []

    # Метод для взятия книги читателем
    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)

    # Метод для возврата книги читателем
    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    # Представление объекта читателя в виде строки
    def __str__(self) -> str:
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books]) or "None"
        return f"Reader {self.name} (ID: {self.reader_id}), Borrowed books: {borrowed_titles}"

# Класс Library
class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []
        self.readers: List[Reader] = []

    # Метод для добавления книги в библиотеку
    def add_book(self, book: Book):
        self.books.append(book)

    # Метод для удаления книги из библиотеки
    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
        else:
            raise ValueError("The book does not exist in the library")

    # Метод для регистрации нового читателя
    def register_reader(self, reader: Reader):
        self.readers.append(reader)

    # Метод для выдачи книги читателю
    def lend_book(self, book_title: str, reader_id: int):
        book = self.find_book(book_title)
        if not book:
            raise ValueError("Book not found")

        reader = self.find_reader_by_id(reader_id)
        if not reader:
            raise ValueError("Reader not found")

        reader.borrow_book(book)
        self.books.remove(book)

    # Метод для возврата книги читателем
    def return_book(self, book_title: str, reader_id: int):
        reader = self.find_reader_by_id(reader_id)
        if not reader:
            raise ValueError("Reader not found")

        book = next((b for b in reader.borrowed_books if b.title == book_title), None)
        if not book:
            raise ValueError("Reader does not have this book")

        reader.return_book(book)
        self.books.append(book)

    # Метод для поиска книги по названию
    def find_book(self, title: str) -> Optional[Book]:
        return next((book for book in self.books if book.title == title), None)

    # Метод для поиска читателя по ID
    def find_reader_by_id(self, reader_id: int) -> Optional[Reader]:
        return next((reader for reader in self.readers if reader.reader_id == reader_id), None)

    # Метод для получения списка книг, взятых читателем
    def get_reader_books(self, reader_id: int) -> List[Book]:
        reader = self.find_reader_by_id(reader_id)
        if reader:
            return reader.borrowed_books
        return []

    # Метод для сохранения состояния библиотеки в файл
    def save_library_state(self, filename: str):
        state = {
            "books": [{"title": b.title, "author": b.author, "year": b.year, "genre": b.genre} for b in self.books],
            "readers": [{
                "name": r.name, "reader_id": r.reader_id,
                "borrowed_books": [{"title": b.title, "author": b.author, "year": b.year, "genre": b.genre} for b in r.borrowed_books]
            } for r in self.readers]
        }
        with open(filename, 'w') as file:
            json.dump(state, file, indent=4)

    # Метод для загрузки состояния библиотеки из файла
    def load_library_state(self, filename: str):
        with open(filename, 'r') as file:
            state = json.load(file)

        self.books = [Book(b["title"], b["author"], b["year"], b["genre"]) for b in state["books"]]
        self.readers = [Reader(r["name"], r["reader_id"]) for r in state["readers"]]
        for reader, reader_data in zip(self.readers, state["readers"]):
            reader.borrowed_books = [Book(b["title"], b["author"], b["year"], b["genre"]) for b in reader_data["borrowed_books"]]

# Пример использования системы управления библиотекой
if __name__ == "__main__":
    # Создание библиотеки
    library = Library("Central Library")

    # Добавление книг
    library.add_book(Book("1984", "George Orwell", 1949, "Dystopia"))
    library.add_book(Book("Brave New World", "Aldous Huxley", 1932, "Science Fiction"))
    library.add_book(Book("Fahrenheit 451", "Ray Bradbury", 1953, "Dystopia"))

    # Регистрация читателей
    reader1 = Reader("Alice", 1)
    reader2 = Reader("Bob", 2)
    library.register_reader(reader1)
    library.register_reader(reader2)

    # Выдача книги читателю
    library.lend_book("1984", 1)

    # Вывод информации о читателях
    print(reader1)
    print(reader2)

    # Возврат книги в библиотеку
    library.return_book("1984", 1)

    # Сохранение состояния библиотеки в файл
    library.save_library_state("library_state.json")

    # Загрузка состояния библиотеки из файла
    new_library = Library("New Library")
    new_library.load_library_state("library_state.json")
    print("Состояние библиотеки загружено.")
