from view.game_view import GameView
from model.game import Game

class GameController:
    def __init__(self, view: GameView, model: Game):
        self.view = view
        self.model = model

    def run_game(self):
        while True:
            self.view.draw_board()
            row, col = self.view.get_move()
            while not self.model.is_valid_move(row, col):
                #TODO   display error message in the view 
                row, col = self.view.get_move()

            self.model.make_move(row, col)
            player = self.model.check_winner()

            if player:
                self.view.display_winner(player)
                break

            self.model.change_player()
