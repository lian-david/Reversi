from model.reversi_game import ReversiGame
from model.board import Board
from model.players import Players
import copy

class AI:
    """Represents AI Player"""
    def __init__(self, game: ReversiGame):
        """Initializes AI Player attributes"""
        self.game = game
        self.board = self.game.board

    def computer_move(self):
        """Returns best move for computer to make based on one step lookahead

        Returns:
            best_move(tuple): row and column indices for computer play 
        """
        valid_moves = self.game.get_moves()
        best_score = -1
        best_move = -1, -1 
        for r,c in valid_moves:
            board_copy = copy.deepcopy(self.board)
            board_copy.update_location(r, c, self.game.curr_player)
            
            black_score = board_copy.score_book["X"]
            white_score = board_copy.score_book["O"]
            score = white_score - black_score
            if score > best_score:
                best_move = r,c
                best_score = score
        
        return best_move

    def minimax(self, board: Board, max_player, min_player):
        if self.terminal_state(board):
            if self.game.get_winner() == Players.WHITE_DISK:
                return 1
            elif self.game.get_winner() == Players.BLACK_DISK:
                return -1
            elif self.game.get_winner() == 3:
                return 0
        
        values = []


    def terminal_state(self, board: Board):
        """Determines if board is in terminal state

        Args:
            board(Board): the board in its current state
        Returns:
            T/F if board contains empty cells 
        """
        scores = board.score_book
        if scores["E"] == 0:
            return True 
        return False 
