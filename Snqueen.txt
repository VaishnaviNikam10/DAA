# Function to check if placing a queen at board[row] = col is safe
def is_safe(board, row, col):
    n = len(board)
    for r in range(n):
        if r == row:
            continue
        c = board[r]
        if c == -1:
            continue
        # Check for same column or diagonal conflict
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


# Recursive function to solve N-Queens using backtracking
def solve_from_row(board, start=0):
    n = len(board)
    # Find the next empty row
    row = start
    while row < n and board[row] != -1:
        row += 1

    # Base case: all queens placed successfully
    if row == n:
        return True

    # Try placing queen in each column
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            if solve_from_row(board, row + 1):
                return True
            # Backtrack
            board[row] = -1
    return False


# Function to print the N-Queens board
def print_board(board):
    n = len(board)
    for r in range(n):
        print(" ".join('Q' if board[r] == c else '.' for c in range(n)))
    print()


# Main function that allows first queen placement
def n_queens_with_first(n, first_row=-1, first_col=-1):
    board = [-1] * n

    # Place first queen if user provided coordinates
    if first_row != -1 and first_col != -1:
        if not (0 <= first_row < n and 0 <= first_col < n):
            print("First queen coordinates out of range.")
            return
        board[first_row] = first_col
        if not is_safe(board, first_row, first_col):
            print("Pre-placed queen conflicts with another (invalid).")
            return

    # Solve using backtracking
    if solve_from_row(board, 0):
        print(f"\nOne valid {n}-Queens solution (with first queen at ({first_row}, {first_col})):")
        print_board(board)
    else:
        print("No solution exists for the given pre-placement.")


# Driver code
if __name__ == "__main__":
    n = int(input("Enter board size n (e.g., 8): "))
    fr = int(input("Enter row of first queen (0-indexed) or -1 to skip: "))
    fc = -1
    if fr != -1:
        fc = int(input("Enter column of first queen (0-indexed): "))
    n_queens_with_first(n, first_row=fr, first_col=fc)
