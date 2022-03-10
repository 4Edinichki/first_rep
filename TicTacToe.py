field = [
    [" ", "0", "1", "2"],
    ["0", "-", "-", "-"],
    ["1", "-", "-", "-"],
    ["2", "-", "-", "-"]
]
player = "one"

print("Нi, this is a tic-tac-toe game.")


def change_players(player):
    if player == "one":
        return "two"
    else:
        return "one"


def salute(func):
    def message_(player=None):
        if player == "one":
            print("Player one, please make your move.")
        elif player == "two":
            print("Player two, please make your move.")
        func()

    return message_


def check_input(func):
    def check_(field_, player):
        while True:
            try:
                x, y = map(int, input("Enter the step index through space: ").split())
                break
            except:
                print("Incorrect data")
        while True:
            if all([0 <= x <= 2, 0 <= y <= 2]):
                if func(field_, player, x, y) == False:
                    print("Incorrect data")
                    x, y = map(int, input("try again: ").split())
                else:
                    break
            else:
                print("Incorrect data")
                x, y = map(int, input("try again: ").split())

    return check_


@check_input
def check_position(field_check_pos, pl, x_, y_):
    if field_check_pos[x_ + 1][y_ + 1] == "-":
        if pl == "one":
            field_check_pos[x_ + 1][y_ + 1] = "x"
        else:
            field_check_pos[x_ + 1][y_ + 1] = "o"
        return True
    else:
        return False


@salute
def print_field():
    for row in field:
        print(*row)


def check_combo(rezult):
    if any([rezult[1][1] == rezult[1][2] == rezult[1][3] != "-",
            rezult[2][1] == rezult[2][2] == rezult[2][3] != "-",
            rezult[3][1] == rezult[3][2] == rezult[3][3] != "-",

            rezult[1][1] == rezult[2][1] == rezult[3][1] != "-",
            rezult[1][2] == rezult[2][2] == rezult[3][2] != "-",
            rezult[1][3] == rezult[2][3] == rezult[3][3] != "-",

            rezult[1][1] == rezult[2][2] == rezult[3][3] != "-",
            rezult[3][3] == rezult[2][2] == rezult[1][3] != "-"]):
        return True
    return False


counter = 1
while player:
    print_field(player)
    check_position(field, player)
    if check_combo(field):
        print_field()
        print(f'Player {player} won!!!')
        break
    if counter == 9:
        print_field()
        print(f'Draw!!!')
        break
    player = change_players(player)
    counter += 1