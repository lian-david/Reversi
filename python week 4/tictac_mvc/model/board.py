class Board:
    EMPTY_CELL = 0

    def __init__(self, size):
        self.size = size

        #allocate the board with empty squares 
        self.mat = [[self.EMPTY_CELL] * size for _ in range(size)]

    def get_cell(self, row, col):
        return self.mat[row][col]

    def update_cell(self, row, col, player):
        self.mat[row][col] = player