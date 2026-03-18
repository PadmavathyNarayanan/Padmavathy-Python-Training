def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueen(board, row, n):
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueen(board, row + 1, n)
            board[row] = -1


# Example usage
n = 4
board = [-1] * n
solve_nqueen(board, 0, n)