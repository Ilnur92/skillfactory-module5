field = [[" ", "0", "1", "2"],
         ["0", "-", "-", "-"],
         ["1", "-", "-", "-"],
         ["2", "-", "-", "-"]]


def show_field():
    for x in field:
        print(x[0], x[1], x[2], x[3])


def ask_field():
    i = input("Введите строку: ")
    i = int(i)
    j = input("Введите столбец: ")
    j = int(j)
    return i, j


for i in range(5):
    show_field()
    print("Ходи X!")
    i, j = ask_field()
    field[i + 1][j + 1] = "x"

    show_field()
    print("Ходи 0!")
    i, j = ask_field()
    field[i + 1][j + 1] = "0"

wins = [((1, 1), (1, 2), (1, 3)), ((2, 1), (2, 2), (2, 3)), ((3, 1), (3, 2), (3, 3)), ((1, 1), (2, 2), (3, 3)),
        ((1, 3), (2, 2), 3, 1)]


def check_win():
    for user in ['x', '0']:
        for i in range(3):
            if f'{field[i][0]}{field[i][1]}{field[i][2]}' == user * 3:
                print(f"Win - {user}")
                return
            elif f'{field[0][i]}{field[1][i]}{field[2][i]}' == user * 3:
                print(f"Win - {user}")
                return

        if f'{field[0][0]}{field[1][1]}{field[2][2]}' == user * 3:
            print(f"Win - {user}")
            return
        elif f'{field[0][2]}{field[1][1]}{field[2][0]}' == user * 3:
            print(f"Win - {user}")
            return
    for j in range(3):
        if field[i + 1][j + 1] not in field[j] and '_' not in field[j]:
            return True
