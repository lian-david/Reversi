from model.players import Players

class Board:
    EMPTY_CELL = 0

    def __init__(self, size):
        """Initializes board attributes

        Args:
            size(int) = user input size 
        """
        self.size = size

        #allocate the board with empty squares 
        self._board = [[self.EMPTY_CELL] * size for _ in range(size)]
        
        #initialize starting positions
        self.mid = size // 2
        self._board[self.mid - 1][self.mid - 1] = Players.WHITE_DISK
        self._board[self.mid][self.mid] = Players.WHITE_DISK
        self._board[self.mid - 1][self.mid] = Players.BLACK_DISK
        self._board[self.mid][self.mid - 1] = Players.BLACK_DISK

    def get_location(self, row, col):
        """Retrieves board location
        
        Args:
            row(list): row index of board matrix
            col(list): column index of board matrix
        """
        return self._board[row][col]

    def update_location(self, row, col, player):
        """Updates board location
        
        Args:
            row(list): row index of board matrix
            col(list): column index of board matrix
            player(Players): the current player 
        """
        self._board[row][col] = player
        
    def valid_location(self, row, col):
        """Returns True/False if row, col are within board range 

        Args:
            row(list): row index of board matrix
            col(list): column index of board matrix
        """
        return row >= 0 and row <= self.size - 1 \
             and col >= 0 and col <= self.size - 1
