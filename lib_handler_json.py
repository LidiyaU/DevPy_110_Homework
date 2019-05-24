import json

books_file = 'books.json'
action = "\nВарианты (сначала надо выбрать (1) или создать файл (2), после этого можно выбирать другие действия:\n'1' - выбрать существующий файл библиотеки\n'2' - создать новый файл библиотеки\n'3' - добавить книгу\n'4' - редактировать книгу\n'5' - вывести список\n'6' - удалить книгу\n'7' - найти книгу\n'0' - выйти\nВаш выбор: "


def create_book_table():
    global books_file
    books_file = input('Введите желаемое название файла: ')
    books_file = books_file + '.json'
    with open(books_file, 'w') as file:
        json.dump([], file)  # содает файл как пустой лист

def get_file():
    global books_file
    books_file = input("Введите название библиотеки (файла в формате json): ")
    books_file = books_file + ".json"
	
def list_books():
    with open(books_file, 'r') as file:
        return json.load(file)

def add_book(name, author, descr):
    books = list_books()
    books.append({'Название': name, 'Автор': author, 'Описание': descr})
    save_all_books(books)

def search_book(keyword):
    keyword.lower()
    books = list_books()
    book = [book for book in books if keyword in book['Название'].lower()]
    #print(book)
    for x in book: print(x)
    if book == []:
        print(f'Не найдено: "{keyword}"')

def edit_book(e_name):
    #search_book(e_name)
    books = list_books()
    book = [book for book in books if book['Название'] == e_name]
    if book == []:
        print(f"Такой книги нет в бибилиотеке")
        edit_book_handler()

    print(f"Книга была сохранена в таком виде:\n {book}")
    answer = list((input('Нужно исправить? [Д]а? [Н]ет: ')).lower().split())[0]
    if answer == 'н':
        lib()
    else:
        delete_book(e_name)
        add_book_handler()


def save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


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

def edit_book_handler():
    e_name = input('Введите название книги, которую вы хотите отредактировать: ')

    edit_book(e_name)

def list_books_handler():
    for book in list_books():
        print(f"Название: {book['Название']}\nАвтор: {book['Автор']}\nОписание: {book['Описание']}\n")

def search_book_handler():
    keyword = input('Введите название книги, полностью или часть, которую вы хотите найти: ')

    search_book(keyword)

def delete_book_handler():
    name = input('Введите название книги, которую вы хотите удалить: ')

    delete_book(name)

def lib():
    user_input = input(action)

    while user_input != '0':
        if user_input == '1':
            get_file()
        elif user_input == '2':
            create_book_table()
        elif user_input == '3':
            add_book_handler()
        elif user_input == '4':
            edit_book_handler()
        elif user_input == '5':
            list_books_handler()
        elif user_input == '6':
            delete_book_handler()
        elif user_input == '7':
            search_book_handler()

        user_input = input(action)


lib()
