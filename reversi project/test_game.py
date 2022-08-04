from model.reversi_game import ReversiGame
from view.reversi_user import ReversiUser
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

choice = ReversiUser.display_menu()
players = ReversiUser.get_players()
size = ReversiUser.get_board_size()
game = ReversiGame(size)
view = GameConsoleView(game)
controller = GameController(game, view)
controller.run_game(choice, players)