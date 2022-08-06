from model.reversi_game import ReversiGame
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

rules, players, size = GameConsoleView.display_menu()
game = ReversiGame(size)
view = GameConsoleView(game)
controller = GameController(game, view, players[0], players[1])
controller.run_game(rules)