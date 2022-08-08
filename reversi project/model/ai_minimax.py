from model.reversi_game import ReversiGame
from model.board import Board
from model.players import Players
import copy

class AdvancedAI:
    """Represents AI Player using MiniMax algorithm"""
    def __init__(self, game: ReversiGame):
        """Initializes Advanced AI Player attributes"""
        self.game = game
        self.board = self.game.board
        self.player = Players.WHITE_DISK
        self.opponent = Players.BLACK_DISK
        
    def get_move(self):
        """Returns best move for computer to make based on minimax

        Returns:
            best_move(tuple): row and column indices for computer play 
        """
        valid_moves = self.game.get_moves()
        loss_value = -2
        for r,c in valid_moves:
            board_copy = copy.deepcopy(self.board)
            board_copy.update_location(r, c, self.player)
            board_value = self.minimax(board_copy, 5, self.player, self.opponent)
            if board_value > loss_value:
                best_move = r,c
                loss_value = board_value 

        return best_move

    def minimax(self, board: Board, depth, max_player, min_player):
        """Computes AI move based on current state of board
        Args:
            board(Board): the copy of the current board passed to function
            depth(int): depth of comparisons utilized to determine move
            max_player(Players): the max player 
            min_player(Players): the min player 
        Returns:
            values(list): returns max/min element from values, the list of board values
        """
        if depth == 0 or self.terminal_state(board):
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
            board_copy.update_location(r, c, max_player)
            board_value = self.minimax(board_copy, depth - 1, max_player, min_player)
            values.append(board_value)
        
        if self.player == max_player:
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
