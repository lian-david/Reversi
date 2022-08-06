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
        self.player = Players.WHITE_DISK
        self.opponent = Players.BLACK_DISK

    def get_move(self):
        """Returns best move for computer to make based on one step lookahead

        Returns:
            best_move(tuple): row and column indices for computer play 
        """
        valid_moves = self.game.get_moves()
        best_score = -1
        for r,c in valid_moves:
            board_copy = copy.deepcopy(self.board)
            board_copy.update_location(r, c, self.player)
            
            black_score = board_copy.score_book["X"]
            white_score = board_copy.score_book["O"]
            score = white_score - black_score
            if score > best_score:
                best_move = r,c
                best_score = score
        return best_move

    def choose_move(self, board: Board):
        valid_moves = self.game.get_moves()
        loss_value = -2
        for r,c in valid_moves:
            board_copy = copy.deepcopy(board)
            board_copy.update_location(r, c, self.player)
            board_value = self.minimax(board_copy, self.player, self.opponent)
            if board_value > loss_value:
                best_move = r,c 

        return best_move

    def minimax(self, board: Board, max_player, min_player):
        if self.terminal_state(board):
            if board.get_winner() == self.player:
                return 1
            elif board.get_winner() == self.opponent:
                return -1
            elif board.get_winner() == 3:
                return 0
        
        valid_moves = []
        for row in range(board.size):
            for col in range(board.size):
                if self.game.is_valid_move(row, col) != False:
                    valid_moves.append([row, col])

        values = []
        for r,c in valid_moves:
            board_copy = copy.deepcopy(board)
            board_copy.update_location(r, c, self.player)
            board_value = self.minimax(board_copy, self.opponent, self.player)
            values.append(board_value)
        
        if self.game.curr_player == max_player:
            return max(values)
        else:
            return min(values)

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
