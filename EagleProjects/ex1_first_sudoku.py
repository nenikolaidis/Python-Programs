# Given board
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 0, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

count = 0

def is_valid(board, row, col, num):
    # Check if the number is valid in the current row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is valid in the current column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is valid in the current 3x3 block
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def solve_sudoku(board):
    global count
    empty = find_empty_cell(board)
    if not empty:
        return True  # Puzzle solved

    row, col = empty
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True

            board[row][col] = 0  # Undo the move (backtrack)
            count += 1  # Increment the backtracking count
    
    return False

if solve_sudoku(board):
    for row in board:
        print(row)
else:
    print("No solution exists.")

print("Backtracking steps:", count)
