books_file = 'books.txt'

action = "\nВарианты:\n'д' - добавить новую книгу\n'с' - вывести список\n'у' - уалить книгу\n'в' - выйти\nНажмите:\n"


def list_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    return [
        {'Название': line[0], 'Автор': line[1], 'Описание': line[2]}
        for line in lines
    ]


def add_book(name, author, descr):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author}, {descr}\n')


def save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['Название']},{book['Автор']},{book['Описание']}\n")


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)

def delete_book(name):
    books = list_books()
    books = [book for book in books if book['Название'] != name]
    save_all_books(books)


# ---------------- handlers


def add_book_handler():
    name = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    descr = input('Введите описание книги: ')

    add_book(name, author, descr)


def list_books_handler():
    for book in list_books():
        print(f"Название: {book['Название']}\nАвтор: {book['Автор']}\nОписание: {book['Описание']}\n")


def delete_book_handler():
    name = input('Введите название книги, которую вы хотите удалить: ')

    delete_book(name)


def menu():
    user_input = input(action).lower()

    while user_input != 'в':
        if user_input == 'д':
            add_book_handler()
        elif user_input == 'с':
            list_books_handler()
        elif user_input == 'у':
            delete_book_handler()

        user_input = input(action).lower()


menu()
