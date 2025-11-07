# Function to print the chessboard
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

# Check if placing queen at (row, col) is safe
def is_safe(board, row, col, n):
    # Check this column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Backtracking function to solve N-Queens
def solve_nqueens(board, row, n):
    # Base case: if all queens are placed
    if row == n:
        print_board(board, n)
        return True

    # Try placing queen in all columns for current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # place queen
            solve_nqueens(board, row + 1, n)
            board[row][col] = 0  # backtrack

    return False


# --- MAIN PROGRAM ---
n = int(input("Enter the size of the chessboard (N): "))
board = [[0 for _ in range(n)] for _ in range(n)]

# Take user input for first queen position
r = int(input("Enter row position of first queen (0-indexed): "))
c = int(input("Enter column position of first queen (0-indexed): "))

# Place the first queen
board[r][c] = 1

print("\nAll possible solutions with first queen fixed at position (", r, ",", c, "):\n")
solve_nqueens(board, r + 1, n)
