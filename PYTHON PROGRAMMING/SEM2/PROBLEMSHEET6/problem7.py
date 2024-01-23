import sys

print("----------------- CONNECT FOUR -----------------\n\n")


def display_board(board):
    for i in range(0, 6):
        print(
            f"| {board[i][0]} | {board[i][1]} | {board[i][2]} | {board[i][3]} | {board[i][4]} | {board[i][5]} | {board[i][6]} |"
        )
        print("-" * 29)


def checkDraw(board):
    for i in board:
        if " " in i:
            return 0
    return 1


def checkWin(board, Player):
    if Player == "R":
        for i in range(0, 6):
            if (
                board[i][0] == board[i][1] == board[i][2] == board[i][3] == "R"
                or board[i][1] == board[i][2] == board[i][3] == board[i][4] == "R"
                or board[i][2] == board[i][3] == board[i][4] == board[i][5] == "R"
                or board[i][3] == board[i][4] == board[i][5] == board[i][6] == "R"
            ):
                return 1
        for i in range(0, 7):
            if (
                board[0][i] == board[1][i] == board[2][i] == board[3][i] == "R"
                or board[1][i] == board[2][i] == board[3][i] == board[4][i] == "R"
                or board[2][i] == board[3][i] == board[4][i] == board[5][i] == "R"
                # or board[3][i] == board[4][i] == board[5][i] == board[6][i] == "R"
            ):
                return 1
        for i in range(5, -1, -1):
            for j in range(0, 7):
                if i > 2 and j < 4:
                    if (
                        board[i][j]
                        == board[i - 1][j + 1]
                        == board[i - 2][j + 2]
                        == board[i - 3][j + 3]
                        == "R"
                    ):
                        return 1
        for i in range(0, 6):
            for j in range(0, 7):
                if i < 3 and j < 4:
                    if (
                        board[i][j]
                        == board[i + 1][j + 1]
                        == board[i + 2][j + 2]
                        == board[i + 3][j + 3]
                        == "R"
                    ):
                        return 1
        return 0
    if Player == "Y":
        for i in range(0, 6):
            if (
                board[i][0] == board[i][1] == board[i][2] == board[i][3] == "Y"
                or board[i][1] == board[i][2] == board[i][3] == board[i][4] == "Y"
                or board[i][2] == board[i][3] == board[i][4] == board[i][5] == "Y"
                or board[i][3] == board[i][4] == board[i][5] == board[i][6] == "Y"
            ):
                return 1
        for i in range(0, 7):
            if (
                board[0][i] == board[1][i] == board[2][i] == board[3][i] == "Y"
                or board[1][i] == board[2][i] == board[3][i] == board[4][i] == "Y"
                or board[2][i] == board[3][i] == board[4][i] == board[5][i] == "Y"
                # or board[3][i] == board[4][i] == board[5][i] == board[6][i] == "Y"
            ):
                return 1
        for i in range(5, -1, -1):
            for j in range(0, 7):
                if i > 2 and j < 4:
                    if (
                        board[i][j]
                        == board[i - 1][j + 1]
                        == board[i - 2][j + 2]
                        == board[i - 3][j + 3]
                        == "Y"
                    ):
                        return 1
        for i in range(0, 6):
            for j in range(0, 7):
                if i < 3 and j < 4:
                    if (
                        board[i][j]
                        == board[i + 1][j + 1]
                        == board[i + 2][j + 2]
                        == board[i + 3][j + 3]
                        == "Y"
                    ):
                        return 1
        return 0


board_instance = []
for i in range(0, 6):
    board_instance.append([" "] * 7)
display_board(board_instance)

print("PLAYER 1 IS RED(R) AND PLAYER 2 IS YELLOW(Y).")
while checkDraw(board_instance) == 0:
    Player1 = int(input("PLAYER 1 COLUMN : "))
    for i in range(5, -1, -1):
        if board_instance[i][Player1] == " ":
            board_instance[i][Player1] = "R"
            break
        if checkWin(board_instance, "R") == 1:
            display_board(board_instance)
            print("\nPLAYER 1 WINS.\n")
            sys.exit()
    Player2 = int(input("PLAYER 2 COLUMN : "))
    for i in range(5, -1, -1):
        if board_instance[i][Player2] == " ":
            board_instance[i][Player2] = "Y"
            break
        if checkWin(board_instance, "Y") == 1:
            display_board(board_instance)
            print("\nPLAYER 2 WINS.\n")
            sys.exit()
    display_board(board_instance)
