from view.game_view import GameView
from model.game import Game
from controller.game_controller import GameController

view = GameView()
game = Game()
controller = GameController(game, view)
controller.run_game()