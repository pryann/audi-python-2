from os import path
import file_handler
import crud

FILE_PATH = path.join(path.dirname(__file__), "books.csv")
books = file_handler.read_file(FILE_PATH)


def list_books():
    # no processing, just listing
    print(crud.list_items(books))


def find_book_by_id():
    # check characters before convert to int all places where use this:
    id = int(input("Add meg a keresendő könyv azonosítóját (id): "))
    book = crud.find_item(id, books)
    print(book)


def update_book():
    id = int(input("Add meg a frissítendő könyv azonosítóját (id): "))
    title = input("Add meg a könyv címét: ")
    author = input("Add meg a könyv szerzőjét: ")

    # if you have many key, use a loop, and partial update
    # book = crud_operations.find_item(id, books)
    # for k in book.keys():
    #     data = input(f'Add meg a könyv új {k} értékét!: ')
    #     if data:
    #         book.update({k: data})

    book = {"id": id, "title": title, "author": author}
    crud.update_item(id, book, books)
    file_handler.write_file(books, FILE_PATH)


def create_book():
    title = input("Add meg az új könyv címét: ")
    author = input("Add meg az új könyv szerzőjét: ")
    # validate date
    book = {"title": title, "author": author}
    crud.create_item(book, books)
    file_handler.write_file(books, FILE_PATH)


def remove_book():
    id = int(input("Add meg a törlendő könyv azonosítóját (id): "))
    crud.remove_item(id, books)
    file_handler.write_file(books, FILE_PATH)
