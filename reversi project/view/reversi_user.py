class ReversiUser:
    """Reversi user interface
    """
    def get_board_size():
        """Retreives board size from user
        """
        try: 
            board_size = int(input("Enter the board size: "))
        except ValueError:
            print("Input must be numeric.")

        return board_size 

    def get_rules():
        """Retrieves rules for game from user
        """
        rules = input("Enter the game type (classical, alternative): ")
        return rules

    def get_AI():
        pass

    def display_menu():
        """Displays starting menu.

        Returns:
            ans(str): user input
        """
        print("----------Welcome to Reversi----------")
        print("Would you like to start a new game? [s]")
        ans = input("Or would you like to end session? [e] ").lower()
        if ans != "s" and ans != "e":
            ans = input("Please enter a valid option: ").lower()
        return ans

