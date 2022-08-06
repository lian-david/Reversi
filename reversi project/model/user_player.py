class UserPlayer:
    """Represents User player"""
    @staticmethod
    def get_move():
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