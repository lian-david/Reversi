#script that gets a 9 × 9 Sudoku board (represented by a two-dimensional list)and determines if it is 
# valid according to the following rules: Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 × 3 sub-boxes of the board must contain the digits 1-9 without repetition.

def is_valid_sudoku(board):
    valid_set = set(range(1, 10))

    #check the rows
    for i in range(9):
        if set(board[i]) != valid_set:
            return False
    
    #check the columns
    for i in range(9):
        col = [row[i] for row in board]
        if set(col) != valid_set:
            return False

    #check the sub grids
    for i in range(3):
        for j in range(3):
            sub_grid = []
            for k in range(i * 3, (i + 1) * 3):
                for l in range(j*3, (j + 1) * 3):
                    sub_grid.append(board[k][l])
            if set(sub_grid) != valid_set:
                return False

    return True

board = [[6, 3, 9, 5, 7, 4, 1, 8, 2],
        [5, 4, 1, 8, 2, 9, 3, 7, 6],
        [7, 8, 2, 6, 1, 3, 9, 5, 4],
        [1, 9, 8, 4, 6, 7, 5, 2, 3],
        [3, 6, 5, 9, 8, 2, 4, 1, 7],
        [4, 2, 7, 1, 3, 5, 8, 6, 9],
        [9, 5, 6, 7, 4, 8, 2, 3, 1],
        [8, 1, 3, 2, 9, 6, 7, 4, 5],
        [2, 7, 4, 3, 5, 1, 6, 9, 8]]

print(is_valid_sudoku(board))

