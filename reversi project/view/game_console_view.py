from view.board_console_view import BoardConsoleView
from model.reversi_game import ReversiGame

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

    def get_move(self):
        """Retreives move from user 

        Returns:
            row, col: location of move 
        """
        move = input("Enter your move (row, col):").split(",")
        row = int(move[0]) - 1
        col = int(move[1]) - 1
        return row, col

    def draw_board(self):
        """Displays board from game.
        """
        self.board_view.draw_board()
        scores = self.game.get_scores()
        print(f'X score: {scores["X"]}, O score: {scores["O"]}')
        print(f'Player {GameConsoleView.symbols[self.game.curr_player]}: It\'s your turn.')
        

    def display_winner(self, player):
        """Displays winning player.
        """
        winner = self.game.get_winner()
        if player == winner:
            if player == 1 or player == 2:
                print(f'Player {GameConsoleView.symbols[winner]} has won!') 
            else:
                print(GameConsoleView.symbols[winner])

    def display_menu(self):
        """Displays starting menu.

        Returns:
            ans(str): user input
        """
        print("Would you like to start a new game? [s]")
        ans = input("Or would you like to end session? [e] ").lower()
        if ans != "s" and ans != "e":
            ans = input("Please enter a valid option: ").lower()
        return ans
