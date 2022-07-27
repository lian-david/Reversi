from model.reversi_game import ReversiGame
from view.reversi_user import ReversiUser
from view.game_console_view import GameConsoleView
from controller.game_controller import GameController

choice = ReversiUser.display_menu()
players = ReversiUser.get_players()
game = ReversiGame(ReversiUser.get_board_size())
view = GameConsoleView(game)
controller = GameController(game, view)
controller.run_game(choice, players)