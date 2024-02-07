def print_board(board):
    for i in range(3):
        for j in range(3):
            print(f"{board[i][j]:^3}", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("-----------")
    print()

def make_move(player, position, board, counter):
    row, col = position // 3, position % 3
    if board[row][col] == ' ':
        board[row][col] = player
        counter += 1
        return True, counter
    else:
        print('This position is already taken')
        return False, counter

def check_winner(board):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]

        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[1][1]

    return None

def check_tie(board):
    return all(cell != ' ' for row in board for cell in row)

def reset_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def run_tic_tac_toe():
    board = reset_board()
    counter = 0

    while True:
        print_board(board)
        player = 'X' if counter % 2 == 0 else 'O'
        print(f"{player} turn")
        pos = input('Enter a number from 1 to 9: ')
        position = int(pos) - 1

        if 0 <= position <= 8:
            success, counter = make_move(player, position, board, counter)
            if success:
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print(f'Player {winner} wins!')
                    break
                elif check_tie(board):
                    print_board(board)
                    print('It\'s a tie!')
                    break
        else:
            print('Invalid input. Enter a number from 1 to 9.')

if __name__ == "__main__":
    run_tic_tac_toe()
