from view.game_console_view import GameConsoleView
from model.reversi_game import ReversiGame
from datetime import datetime

class GameController:
    def __init__(self, model: ReversiGame, view: GameConsoleView):
        """Initializes controller attributes to reversi game and view, 
            allowing user to input and view display.
        """
        self.model = model
        self.view = view

    def run_game(self, choice):
        """Runs game
        """
        today = datetime.now()
        start = today.strftime("%m/%d/%Y %H:%M:%S")
        while choice == "s":
            while True:
                self.model.change_player()
                self.view.draw_board()
                row, col = self.view.get_move()
                self.model.make_move(row, col)
                self.model.change_player()
                self.view.draw_board()
                row, col = self.view.get_move()
                if self.model.is_terminated(row, col):
                    player = self.model.get_winner()
                    self.view.display_winner(player)
                    print("Thanks for playing!")
                    break
                else:
                    self.model.make_move(row, col)
            break
        p_view = self.view.symbols[player]
        with open("reversi_scores.txt", "w") as f:
            f.write(f'Date and Time: {start}, Winning Player/Draw: {p_view}, Scores: X: {self.model.score_book["X"]}, O: {self.model.score_book["O"]}')

