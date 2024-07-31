import random

# Constants
ROWS = 6
COLS = 7
EMPTY = 0
PLAYER = 1
COMPUTER = 2

# Initialize the board
def create_board():
    return [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# Print the board
def print_board(board):
    for row in reversed(board):
        print(' '.join(str(cell) if cell != EMPTY else '.' for cell in row))
    print(' '.join(str(i) for i in range(COLS)))

# Drop a piece into the board
def drop_piece(board, col, piece):
    for row in range(ROWS):
        if board[row][col] == EMPTY:
            board[row][col] = piece
            return True
    return False

# Check if the move is valid
def is_valid_location(board, col):
    return board[ROWS-1][col] == EMPTY

# Check for a win condition
def check_winner(board, piece):
    # Check horizontal locations
    for r in range(ROWS):
        for c in range(COLS-3):
            if all(board[r][c+i] == piece for i in range(4)):
                return True

    # Check vertical locations
    for r in range(ROWS-3):
        for c in range(COLS):
            if all(board[r+i][c] == piece for i in range(4)):
                return True

    # Check positively sloped diagonals
    for r in range(ROWS-3):
        for c in range(COLS-3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True

    # Check negatively sloped diagonals
    for r in range(3, ROWS):
        for c in range(COLS-3):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True

    return False

# Check for a draw
def is_draw(board):
    return all(board[0][c] != EMPTY for c in range(COLS))

# Get player's move
def get_player_move(board):
    while True:
        try:
            col = int(input("Enter your move (0-6): "))
            if 0 <= col < COLS and is_valid_location(board, col):
                return col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 0 and 6.")

# Get computer's move
def get_computer_move(board):
    valid_moves = [c for c in range(COLS) if is_valid_location(board, c)]
    return random.choice(valid_moves)

# Main game loop
def play_game():
    board = create_board()
    game_over = False

    print("Welcome to Connect Four!")
    print_board(board)

    while not game_over:
        # Player's turn
        col = get_player_move(board)
        drop_piece(board, col, PLAYER)
        print_board(board)

        if check_winner(board, PLAYER):
            print("Congratulations! You win!")
            game_over = True
            continue

        if is_draw(board):
            print("It's a draw!")
            game_over = True
            continue

        # Computer's turn
        col = get_computer_move(board)
        drop_piece(board, col, COMPUTER)
        print(f"Computer chooses column {col}")
        print_board(board)

        if check_winner(board, COMPUTER):
            print("Computer wins! Better luck next time.")
            game_over = True
            continue

        if is_draw(board):
            print("It's a draw!")
            game_over = True
            continue

if __name__ == "__main__":
    play_game()
