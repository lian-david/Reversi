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
        
        self.score_book = {}

    def get_location(self, row, col):
        """Retrieves board location
        
        Args:
            row(int): row index of board matrix
            col(int): column index of board matrix
        """
        return self._board[row][col]

    def update_location(self, row, col, player):
        """Updates board location
        
        Args:
            row(int): row index of board matrix
            col(int): column index of board matrix
            player(Players): the current player 
        """
        self._board[row][col] = player
        
    def valid_location(self, row, col):
        """Returns True/False if row, col are within board range 

        Args:
            row(int): row index of board matrix
            col(int): column index of board matrix
        """
        return row >= 0 and row <= self.size - 1 \
             and col >= 0 and col <= self.size - 1

    def get_scores(self):
        """Calculates scores for each player

        Returns:
            score_book(dict): dictionary of player scores
        """
        black_score = 0
        white_score = 0
        empty = 0
        for r in range(self.size):
            for c in range(self.size):
                if self.get_location(r, c) == Players.BLACK_DISK:
                    black_score += 1
                if self.get_location(r, c) == Players.WHITE_DISK:
                    white_score += 1
                if self.get_location(r, c) == Board.EMPTY_CELL:
                    empty += 1

        self.score_book = {"X":black_score, "O":white_score, "E":empty}
        return self.score_book

    def get_winner(self):
        """Calculates winning score from score book

        Returns:
            winner(player): player with the winning score / tie
        """
        black_score = self.score_book["X"]
        white_score = self.score_book["O"]

        #check how scores compare to determine winner 
        if black_score > white_score:
            winner = Players.BLACK_DISK
        elif white_score > black_score:
            winner = Players.WHITE_DISK
        elif black_score == white_score:
            winner = 3

        return winner
