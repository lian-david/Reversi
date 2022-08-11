from model.board import Board
from model.players import Players

class ReversiGame:
    """Represents game logic. Including players, classical rules, alternative rules."""
    def __init__(self, board_size):
        """Initializes game attributes 

        Args:
            board_size(int): size of board from user input
        """
        self.board = Board(board_size)
        self.curr_player = None
        
    def change_player(self):
        """Changes player, used for each turn of the game.
        """
        #black disk always plays first 
        if self.curr_player is None:
            self.curr_player = Players.BLACK_DISK
        else:
            if self.curr_player == Players.BLACK_DISK:
                self.curr_player = Players.WHITE_DISK
            else:
                self.curr_player = Players.BLACK_DISK

    def is_valid_move(self, row, col):
        """Determines if move is valid.

        Args:
            row(int): row index from user input
            col(int): col index from user input
        Returns:
            T/F if player's move is valid according to classical rules.
            spaces_flip(list): list of locations if the move is valid.
        """
        if self.board.get_location(row, col) != self.board.EMPTY_CELL \
            or not self.board.valid_location(row, col):
            return False
        self.board.update_location(row, col, self.curr_player)     #set player in location for checking
        if self.curr_player == Players.BLACK_DISK:
            other_play = Players.WHITE_DISK
        else:
            other_play = Players.BLACK_DISK

        spaces_flip = []
        #all possible directions to move row, col
        directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for row_direct, col_direct in directions:
            r, c = row, col
            r += row_direct
            c += col_direct
            #determines if there is other player's disk next to our disk
            if self.board.valid_location(r, c) and self.board.get_location(r, c) == other_play:
                r += row_direct
                c += col_direct
                if not self.board.valid_location(r, c):
                    continue
                while self.board.get_location(r, c) == other_play:
                    r += row_direct
                    c += col_direct
                    if not self.board.valid_location(r, c):
                        break
                if not self.board.valid_location(r, c):
                    continue
                #locate pieces to flip and add locations to list 
                if self.board.get_location(r, c) == self.curr_player:
                    while True:
                        r -= row_direct
                        c -= col_direct
                        if r == row and c == col:
                            break
                        spaces_flip.append([r, c])

        #return empty location after performing possible move
        self.board.update_location(row, col, self.board.EMPTY_CELL)
        #return F for no spaces to flip
        if len(spaces_flip) == 0:
            return False
        
        return spaces_flip

    def make_move(self, row, col):
        """Makes move if it is valid.

        Args:
            row(int): row index from user input
            col(int): col index from user input
        """
        spaces_flip = self.is_valid_move(row, col)
        if spaces_flip == False:
            return False
        
        self.board.update_location(row, col, self.curr_player)
        for r, c in spaces_flip:
            self.board.update_location(r, c, self.curr_player)
        return True

    def make_move_alt(self, row, col):
        """Makes move if it is valid according to alternative rules, which allow player to place
            disk at any location. 

        Args:
            row(int): row index from user input
            col(int): col index from user input
        """
        spaces_flip = self.is_valid_move(row, col)
        if spaces_flip:
            for r, c in spaces_flip:
                self.board.update_location(r, c, self.curr_player)
                
        self.board.update_location(row, col, self.curr_player)

    def get_moves(self):
        """Returns list of valid moves

        Returns:
            valid_moves(list): list of tuples referring to valid row/col indices for play 
        """
        valid_moves = []
        for row in range(self.board.size):
            for col in range(self.board.size):
                if self.is_valid_move(row, col) != False:
                    valid_moves.append([row, col])
        return valid_moves

    def is_terminated(self, row, col):
        """Determines if game is terminated based on various conditions

        Args:
            row(int): row index from user input
            col(int): col index from user input  
        """
        black_score = self.board.score_book["X"]
        white_score = self.board.score_book["O"]
        is_full = self.board.score_book["E"]
        moves = len(self.get_moves())
        
        if self.make_move(row, col) == False:
            return True
        elif black_score == 0 or white_score == 0:  
            return True
        elif is_full == 0:
            return True 
        elif moves == 0:
            return True