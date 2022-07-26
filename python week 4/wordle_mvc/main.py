from model.wordle_game import WordleGame
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

game = WordleGame()
view = GameConsoleView()
controller = GameController(game, view)

controller.run_game()

