from view.board_console_view import BoardConsoleView
from model.reversi_game import ReversiGame
from model.user_player import UserPlayer
from model.ai_player import AI

class GameConsoleView:
    """Represents game in console, allows user to input plays
    """
    symbols = {0: " ", 1: "X", 2: "O", 3: "It's a tie!"}
    def __init__(self, game: ReversiGame):
        """Initializes attributes for game view

        Args:
            game(ReversiGame): Reversi game object 
        """
        self.game = game
        self.board_view = BoardConsoleView(game.board)

    @staticmethod
    def display_menu():
        """Displays starting menu.

        Returns:
            rules(str): user input for game logic
            board_size(int): user input for board size 
            players(list): user input for player choice
        """
        print("----------Welcome to Reversi----------")
        rules = input("\nEnter the game type (classical [c], alternative [a]): ").lower()
        if rules != "c" and rules != "a":
            rules = input("Please enter a valid option: ").lower()

        print("\nWould you like to play against another player? [p]")
        print("Or would you like to play against the advanced computer player? [a]")
        players = input("Or would you like to play against the simple computer player? [c]: ").lower()
        if players != "p" and players != "c" and players != "a":
            players = input("Please enter a valid option: ").lower()

        if players == "p":
            players = [UserPlayer, UserPlayer]
        if players == "c" or players == "a":
            players = [UserPlayer, AI]

        try: 
            board_size = int(input("\nEnter the board size: "))
        except ValueError:
            board_size = int(input("Input must be numeric. Enter the board size: "))
        if board_size <= 0:
            board_size = int(input("Please enter a positive board size: "))
        
        return rules, players, board_size

    def draw_board(self):
        """Displays board from game.
        """
        self.board_view.draw_board()
        scores = self.game.board.get_scores()
        print(f'X score: {scores["X"]}, O score: {scores["O"]}')
        print(f'Player {GameConsoleView.symbols[self.game.curr_player]}: It\'s your turn.')
        

    def display_winner(self, player):
        """Displays winning player.
        """
        winner = self.game.board.get_winner()
        if player == winner:
            if player == 1 or player == 2:
                print(f'Player {GameConsoleView.symbols[winner]} has won!') 
            else:
                print(GameConsoleView.symbols[winner])
        print("Thanks for playing!")
