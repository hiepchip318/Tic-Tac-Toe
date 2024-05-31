import random

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to get the available moves
def get_available_moves(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                moves.append((row, col))
    return moves

# Function to make the bot's move using the minimax algorithm
def make_bot_move(board):
    best_score = float("-inf")
    best_move = None

    for move in get_available_moves(board):
        board[move[0]][move[1]] = "O"
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = " "

        if score > best_score:
            best_score = score
            best_move = move

    board[best_move[0]][best_move[1]] = "O"

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return -1
    elif check_win(board, "O"):
        return 1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "O"
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = "X"
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            best_score = min(score, best_score)
        return best_score

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's move
        while True:
            row = int(input("Nhập hàng (0-2): "))
            col = int(input("Nhập cột (0-2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("Nước đi không hợp lệ. Hãy thử lại.")

        print_board(board)

        if check_win(board, "X"):
            print("Xin chúc mừng! Bạn đã chiến thắng!")
            break

        if is_board_full(board):
            print("Đây là một trận hòa!")
            break

        # Bot's move
        make_bot_move(board)
        print("Bot đã đi nước đi của mình:")
        print_board(board)

        if check_win(board, "O"):
            print("Rất tiếc! Bạn đã thua!")
            break

        if is_board_full(board):
            print("Đây là một trận hòa!")
            break

# Start the game
play_game()