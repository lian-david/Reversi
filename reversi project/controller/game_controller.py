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

    def run_game(self, choice, players):
        """Runs game
        """
        while choice == "s":
            while players == "p":
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
            while players == "c":
                while True:
                    self.model.change_player()
                    self.view.draw_board()
                    row, col = self.view.get_move()
                    self.model.make_move(row, col)
                    self.model.change_player()
                    row, col = self.model.computer_move()
                    if self.model.is_terminated(row, col):
                        player = self.model.get_winner()
                        self.view.display_winner(player)
                        print("Thanks for playing!")
                        break
                    else:
                        self.model.make_move(row, col)
                break
            break
        
        today = datetime.now()
        start = today.strftime("%m/%d/%Y %H:%M:%S")
        p_view = self.view.symbols[player]
        with open("reversi_scores.txt", "a") as f:
            f.write(f'\nDate and Time: {start}, Winning Player/Draw: {p_view}, Scores: X: {self.model.board.score_book["X"]}, O: {self.model.board.score_book["O"]}')

