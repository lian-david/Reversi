from model.board import Board
from model.players import Player

class Game:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.curr_player = Player.X

    def change_player(self):
        self.curr_player = 3 - self.curr_player

    def make_move(self, row, col):
        self.board.update_cell(row, col, self.curr_player)

    def is_valid_move(self, row, col):
        return self.board.get_cell(row, col) == Board.EMPTY_CELL

    def check_winner(self):
        #TODO
        pass

    