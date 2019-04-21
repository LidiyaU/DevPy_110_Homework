board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
action = "Введите, за кого хочет играть первый игрок - 'х' или '0', дальше игроки будут меняться автоматически: "


def board_print():
    print('Поле для игры в Крестики-Нолики размером 3 на 3:')
    for i in range(3):
        print(board[i][0] + ' ' + board[i][1] + ' ' + board[i][2])
    print('')


def coordinates():
    position = []
    for i in range(0, 2):  # set up loop to run 5 times
        user_input = int(input('Введите координаты позиции: сначала строку, затем столбец: '))  # prompt user for number
        position.append(user_input)  # append to our_list
    return position


def winner(symbol):

    # проверка по столбцам и строкам
    for i in range(3):
        if all(board[i][col] == symbol for col in range(3)):
            return True
        if all(board[row][i] == symbol for row in range(3)):
            return True
    # диагональ слева направо
    if all(board[i][i] == symbol for i in range(3)):
        return True
    # диагональ справа налево
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False


def game():
    board_print()
    symbol = input(action).lower()
    counter = 0
    while counter < 9:
        position = coordinates()
        row, col = position[0] - 1, int(position[1]) - 1

        if board[row][col] != '.':
            raise ValueError('Invalid input')
        board[row][col] = symbol

        for i in range(3):
            print(board[i][0] + ' ' + board[i][1] + ' ' + board[i][2])
        print('----------')

        if winner(symbol):
            print(f"\nGAME OVER. \nИграющий за {symbol.title()} выиграл!")
            counter = 0
            # обновление поля
            for i in [0, 1, 2]:
                board[i][0] = board[i][1] = board[i][2] = '.'
        # Смена игрока: 'x' на '0'
        symbol = 'o' if symbol == 'x' else 'x'
        counter += 1
    print("Ничья")


game()

# Кто-то выиграет
# 1,2
# 3,2
# 1,3
# 2,1
# 3,3
# 3,1
# 2,3


# ничья
# 1,1
# 1,2
# 1,3
# 3,3
# 2,2
# 2,3
# 3,2
# 3,1
# 2,1
