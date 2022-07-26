from model.board import Board

class BoardConsoleView:
    """Represents board view in console
    """
    symbols = {0: " ", 1: "X", 2: "O"}
    def __init__(self, board: Board):
        """Initializes attributes as board object 
        """
        self.board = board

    def draw_board(self):
        """Prints board
        """
        board_size = self.board.size
        header = "---+"
        cols_lst = []
        for col in range(board_size):
            cols_lst.append(f'{col + 1} |')

        cols = " ".join(map(str, cols_lst))
        print("   |", cols)
        print(header + (header * board_size))
        for row in range(board_size):
            print(" ",row + 1, end="")
            for col in range(board_size):
                cell = self.board.get_location(row, col)
                print(f'| {BoardConsoleView.symbols[cell]} ', end = "")
            print("|")
            print(header + (header * board_size))
