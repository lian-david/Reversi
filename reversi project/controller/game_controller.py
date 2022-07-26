from view.game_console_view import GameConsoleView
from model.reversi_game import ReversiGame
from model.user_player import UserPlayer
from model.ai_player import AI
from model.ai_minimax import AdvancedAI
from datetime import datetime

class GameController:
    def __init__(self, model: ReversiGame, view: GameConsoleView, black_disk: UserPlayer, white_disk, rules):
        """Initializes controller attributes to reversi game and view, 
            allowing user to input and view display.

        Args:
            model(ReversiGame): the ReversiGame object
            view(GameConsoleView): the console view of ReversiGame
            black_disk(UserPlayer): the user player
            white_disk(any): varies depending on player choice of opponent 
        """
        self.model = model
        self.view = view
        self.black_disk = black_disk
        self.white_disk = white_disk
        if issubclass(white_disk, AI):
            self.white_disk = AI(model)
        elif issubclass(white_disk, AdvancedAI):
            self.white_disk = AdvancedAI(model)
        else:
            self.white_disk = UserPlayer()
        self.rules = rules

    def run_game(self):
        """Runs game based on logic conditions.
        """
        #play game with classical rules
        while self.rules == "c":
            while True:
                self.model.change_player()
                self.view.draw_board()
                row, col = self.black_disk.get_move()
                self.model.make_move(row, col)
                self.model.change_player()
                if isinstance(self.white_disk, UserPlayer):
                    self.view.draw_board()
                if isinstance(self.white_disk, AI) or isinstance(self.white_disk, AdvancedAI):
                    try: 
                        row, col = self.white_disk.get_move()
                    except UnboundLocalError:
                        print("The computer player cannot make a move.")
                else:
                    row, col = self.white_disk.get_move()
                if self.model.is_terminated(row, col):
                    player = self.model.board.get_winner()
                    self.view.display_winner(player)
                    break
                else:
                    self.model.make_move(row, col)
            break
        #play game with alternative rules
        while self.rules == "a":
            while True:
                self.model.change_player()
                self.view.draw_board()
                row, col = self.black_disk.get_move()
                self.model.make_move_alt(row, col)
                self.model.change_player()
                if isinstance(self.white_disk, UserPlayer):
                    self.view.draw_board()
                if isinstance(self.white_disk, AI) or isinstance(self.white_disk, AdvancedAI):
                    try: 
                        row, col = self.white_disk.get_move()
                    except UnboundLocalError:
                        print("The computer player cannot make a move.")
                else:
                    row, col = self.white_disk.get_move()
                if self.model.is_terminated(row, col):
                    player = self.model.board.get_winner()
                    self.view.display_winner(player)
                    break
                else:
                    self.model.make_move_alt(row, col)
            break
        
        #save game results to text file
        today = datetime.now()
        start = today.strftime("%m/%d/%Y %H:%M:%S")
        p_view = self.view.symbols[player]
        with open("reversi_scores.txt", "a") as f:
            f.write(f'\nDate and Time: {start}, Winning Player/Draw: {p_view}, Scores: X: {self.model.board.score_book["X"]}, O: {self.model.board.score_book["O"]}')

