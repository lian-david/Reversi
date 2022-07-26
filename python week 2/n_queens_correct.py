#n queens correction
def place_queens(board_size):
    placements = place_queens_rec(board_size, board_size)
    for queens in placements:
        print_board(queens)
        print()

def place_queens_rec(board_size, n_queens):
    if n_queens == 0:
        return [[]]

    placements = place_queens_rec(board_size, n_queens - 1)
    new = []
    for queens in placements:
        for i in range(board_size):
            if is_legal(queens, i):
                new_placement = queens + [i]
                new.append(new_placement)
    return new

def is_legal(queens, row):
    col = len(queens)
    #check that there are no two queens on the same row
    if row in queens:
        return False
    #check that there are no two queens on the same diagonal
    for i in range(len(queens)):
        if row - queens[i] == col - i:
            return False
        elif queens[i] - row == col - i:
            return False
    return True

def print_board(queens):
    for i in range(len(queens)):
        for j in range(len(queens)):
            if queens[j] == i:
                print("Q", end="")
            else:
                print(".", end="")
        print()

place_queens(4)