print("Tic Tac Toe")
print("Player 1 Symbol: X")
print("Player 2 Symbol: O\n\n")

gg = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def show():
    game = f"{gg[0]} | {gg[1]} | {gg[2]}\n" \
           f"---------\n" \
           f"{gg[3]} | {gg[4]} | {gg[5]}\n" \
           f"---------\n" \
           f"{gg[6]} | {gg[7]} | {gg[8]}\n"

    print(game)


def check_winner(player):
    if gg[0] == gg[1] == gg[2] == player or gg[3] == gg[4] == gg[5] == player or gg[6] == gg[7] == gg[8] == player \
            or gg[0] == gg[4] == gg[8] == player or gg[2] == gg[4] == gg[6] == player or gg[0] == gg[3] == gg[
        6] == player \
            or gg[1] == gg[4] == gg[7] == player or gg[2] == gg[5] == gg[8] == player:

        return True
    else:
        return False


def check_draw():
    for g in gg:
        if str(g).isdigit():
            return False
    return True


show()

player1 = []
player2 = []
for i in range(5):

    # Player 1 Move -X-
    while True:
        try:
            move1 = int(input("Player 1 select number: "))
        except ValueError:
            print("That's not a number!")
            continue
        if move1 in player2:
            print("Box already filled by player 2!")
        elif move1 in player1:
            print("You already filled this box!")
        else:
            try:
                gg[move1 - 1] = "X"
            except IndexError:
                print('Number must be between 1 and 9')
            else:
                player1.append(move1)
                show()
                break

    # check winner after every play
    if check_winner('X'):
        print("Player 1 Won!")
        break
    if check_draw():
        print("Match Draw.")
        break

    # Player 2 Move -O-
    while True:
        try:
            move2 = int(input("Player 2 select number: "))
        except ValueError:
            print("That's not a number!")
            continue
        if move2 in player1:
            print("Box already filled by player 1!")
        elif move2 in player2:
            print("You already filled this box!")
        else:
            try:
                gg[move2 - 1] = "O"
            except IndexError:
                print('Number must be between 1 and 9')
            else:
                player1.append(move2)
                show()
                break

    # check winner after every play
    if check_winner("O"):
        print("Player 2 Won!")
        break

    # check draw
    if check_draw():
        print("Match Draw.")
        break
