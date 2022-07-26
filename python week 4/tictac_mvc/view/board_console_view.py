from board_view import BoardView
from model.board import Board

class BoardConsoleView(BoardView):
    symbols = {0: " ", 1: "X", 2: "O"}
    def __init__(self, board: Board):
        super().__init__(board)

    def draw_board(self):
        board_size = self.board_size
        header = '-' * (4 * board_size + 1)
        print(header)
        for i in range(board_size):
            for j in range(board_size):
                cell = self.board.get_cell(i, j)
                print(f'| {self.symbols[cell]} ')
            print("|")
        print(header)
