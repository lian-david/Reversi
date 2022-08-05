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

    def display_menu():
        """Displays starting menu.

        Returns:
            rules(str): user input for game logic
            ans(str): user input for player choice
            board_size(int): user input for board size 
        """
        print("----------Welcome to Reversi----------")
        rules = input("Enter the game type (classical [c], alternative [a]): ").lower()
        if rules != "c" and rules != "a":
            rules = input("Please enter a valid option: ").lower()

        print("Would you like to play against another player? [p]")
        ans = input("Or would you like to play against the simple computer player? [c] ").lower()
        if ans != "p" and ans != "c":
            ans = input("Please enter a valid option: ").lower()

        try: 
            board_size = int(input("Enter the board size: "))
        except ValueError:
            board_size = int(input("Input must be numeric. Enter the board size: "))
        if board_size <= 0:
            board_size = int(input("Please enter a positive board size: "))
        
        return rules, ans, board_size

    def get_move(self):
        """Retreives move from user 

        Returns:
            row, col(tuple): location of move 
        """
        try:
            move = input("Enter your move (row, col): ").split(",")
            row = int(move[0]) - 1
            col = int(move[1]) - 1
        except IndexError:
            move = input("Please enter a valid move: ").split(",")
            row = int(move[0]) - 1
            col = int(move[1]) - 1
        except ValueError:
            move = input("Please enter a valid move: ").split(",")
            row = int(move[0]) - 1
            col = int(move[1]) - 1
        
        return row, col

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
        winner = self.game.get_winner()
        if player == winner:
            if player == 1 or player == 2:
                print(f'Player {GameConsoleView.symbols[winner]} has won!') 
            else:
                print(GameConsoleView.symbols[winner])
