from model.board import Board
from model.players import Players
import copy

class ReversiGame:
    """Represents game. Including board, players, 
        classical rules, alternative rules.
    """
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
        if self.board._board[row][col] != self.board.EMPTY_CELL or not self.board.valid_location(row, col):
            return False
        self.board._board[row][col] = self.curr_player     #set player in location for checking
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
            if self.board.valid_location(r, c) and self.board._board[r][c] == other_play:
                r += row_direct
                c += col_direct
                if not self.board.valid_location(r, c):
                    continue
                while self.board._board[r][c] == other_play:
                    r += row_direct
                    c += col_direct
                    if not self.board.valid_location(r, c):
                        break
                if not self.board.valid_location(r, c):
                    continue
                #locate pieces to flip and add locations to list 
                if self.board._board[r][c] == self.curr_player:
                    while True:
                        r -= row_direct
                        c -= col_direct
                        if r == row and c == col:
                            break
                        spaces_flip.append([r, c])

        #return empty location after performing possible move
        self.board._board[row][col] = self.board.EMPTY_CELL
        #return F for no spaces to flip
        if len(spaces_flip) == 0:
            return False
        
        return spaces_flip

        #for alt rules just return spaces flip without checking len?

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
        #spaces_flip = self.is_valid_move(row, col)
        # if spaces_flip:
        #     self.board.update_location(row, col, self.curr_player)
        #     for r, c in spaces_flip:
        #         self.board.update_location(r, c, self.curr_player)
        # else:
        #     return False

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

    def computer_move(self):
        """Returns best move for computer to make based on one step lookahead

        Returns:
            best_move(tuple): row and column indices for computer play 
        """
        valid_moves = self.get_moves()
        best_score = -1
        for r,c in valid_moves:
            board_copy = copy.deepcopy(self.board)
            board_copy.update_location(r, c, self.curr_player)
            
            black_score = board_copy.score_book["X"]
            white_score = board_copy.score_book["O"]
            score = white_score - black_score
            if score > best_score:
                best_move = r, c
                best_score = score

        return best_move

    def get_winner(self):
        """Calculates winning score from score book

        Returns:
            winner(player): player with the winning score / tie
        """
        black_score = self.board.score_book["X"]
        white_score = self.board.score_book["O"]

        if black_score > white_score:
            self.winner = Players.BLACK_DISK
        elif white_score > black_score:
            self.winner = Players.WHITE_DISK
        elif black_score == white_score:
            self.winner = 3

        return self.winner

    def is_terminated(self, row, col):
        """Determines if game is terminated based on various conditions

        Args:
            row(int): row index from user input
            col(int): col index from user input  
        """
        black_score = self.board.score_book["X"]
        white_score = self.board.score_book["O"]
        moves = len(self.get_moves())
        
        if self.make_move(row, col) == False:
            return True
        elif black_score == 0 or white_score == 0:  
            return True
        elif moves == 0:
            return True


       