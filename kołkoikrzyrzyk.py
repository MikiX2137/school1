def print_board(board):
    print("  1 2 3")
    for i in range(3):
        row = str(i+1) + " "
        for j in range(3):
            if board[i][j] == 0:
                row += "| "
            elif board[i][j] == 1:
                row += "|X"
            elif board[i][j] == 2:
                row += "|O"
        print(row + "|")

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != 0:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]
    return 0

def play_game():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 1
    while True:
        print_board(board)
        print("Player", player, "turn")
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if board[row-1][col-1] != 0:
            print("Invalid move, try again")
            continue
        board[row-1][col-1] = player
        winner = check_win(board)
        if winner != 0:
            print_board(board)
            print("Player", winner, "wins!")
            break
        if 0 not in [elem for row in board for elem in row]:
            print_board(board)
            print("It's a tie!")
            break
        player = 3 - player

play_game()
