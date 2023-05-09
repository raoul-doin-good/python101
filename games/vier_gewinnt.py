# Vier gewinnt

# possible field states
state_free = "-"        # this field is unoccupied
state_player1 = "O"     # this field is occupied by player 1
state_player2 = "X"     # this field is occupied by player 2

# Initialize playing board
column_size = 6
row_size = 7

column = []
while len(column) < column_size:
    column.append(state_free)

board = []
while len(board) < row_size:
    board.append(column[:])

# Function to print the board


def show_board(board):
    current_row = 0
    num_cols = len(board)
    num_rows = len(board[0])
    output_string = "1 2 3 4 5 6 7\n"
    while current_row < num_rows:
        for column in board:
            output_string += column[current_row]
            output_string += " "
        output_string += "\n"
        current_row += 1
    print(output_string)


def check_player_choice(player_choice, board):
    if player_choice > (len(board)-1):
        return False

    if player_choice < 0:
        return False

    return state_free in board[player_choice]


def apply_player_choice(player_choice, board, player):
    new_column = board[player_choice]
    index = len(new_column) - 1
    for value in new_column[-1::-1]:
        if value == state_free:
            if player == 1:
                new_column[index] = state_player1
            else:
                new_column[index] = state_player2
            break
        index -= 1

    board[player_choice] = new_column
    return board


def has_winner(board):
    # Check columns
    for column in board:
        if column.count(state_player1) == 4 or column.count(state_player2) == 4:
            return True

    # Check rows
    row_index = 0
    while row_index < len(board[0]):
        row = []
        for column in board:
            row.append(column[row_index])

        if row.count(state_player1) == 4 or row.count(state_player2) == 4:
            return True

        row_index += 1

    # Check diagonals
    #   0 1 2 3 4 5 6
    # 0 - - - - - - -
    # 1 - - - - - - -
    # 2 X - - - - - -
    # 3 - X - - - - -
    # 4 - - X - - - -
    # 5 - - - X - - -
    diagonal1 = [board[0][2], board[1][3], board[2][4], board[3][5]]

    #   0 1 2 3 4 5 6
    # 0 - - - - - - -
    # 1 X - - - - - -
    # 2 - X - - - - -
    # 3 - - X - - - -
    # 4 - - - X - - -
    # 5 - - - - - - -
    diagonal2 = [board[0][1], board[1][2], board[2][3], board[3][4]]

    #   0 1 2 3 4 5 6
    # 0 - - - - - - -
    # 1 - - - - - - -
    # 2 - X - - - - -
    # 3 - - X - - - -
    # 4 - - - X - - -
    # 5 - - - - X - -
    diagonal3 = [board[1][2], board[2][3], board[3][4], board[4][5]]
    diagonals = [
        diagonal1,
        diagonal2,
        diagonal3,
    ]
    for diagonal in diagonals:
        if diagonal.count(state_player1) == 4 or diagonal.count(state_player2) == 4:
            return True

    return False


def is_draw(board):
    for column in board:
        if state_free in column:
            return False
    return True


current_player = 1
game_over = False


print("Willkommen zu Vier gewinnt!")

# main loop
while not game_over:
    show_board(board)
    print("Spieler*in", current_player, "ist an der Reihe.")

    player_choice = int(input("Wähle die Spalte (1-7): ")) - 1

    if not check_player_choice(player_choice, board):
        print("Ungültige Eingabe!")
        continue

    board = apply_player_choice(player_choice, board, current_player)

    if has_winner(board):
        print("Spieler*in", current_player, "hat gewonnen!")
        break
    elif is_draw(board):
        print("Keine Züge mehr möglich! Unentschieden!")
        break

    if current_player == 1:
        current_player = 2
    else:
        current_player = 1

show_board(board)
