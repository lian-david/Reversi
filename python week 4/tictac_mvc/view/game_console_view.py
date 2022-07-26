from view.game_view import GameView
from view.board_console_view import BoardConsoleView
from model.game import Game

class GameConsoleView(GameView):
    def __init__(self, game: Game):
        super().__init__(game)
        self.board_view = BoardConsoleView(game.board)

    def get_move(self):
        s = input("Enter your move (row, col):").split(",")
        row = int(s[0])
        col = int(s[1])
        return row, col

    def draw_board(self):
        self.board_view.draw_board()

    def display_winner(self, player):
        print(player)