from model.game import Game
from view.game_view import GameView

class GameController:
    def __init__(self, model: Game, view: GameView):
        self.model = model
        self.view = view

    def run_game(self):
        while not self.model.is_terminated():
            player_location = self.model.get_location()
            self.view.show_player_location(player_location)
            direction = self.view.get_direction()
            self.model.move(direction)

        self.view.display_target_reached()