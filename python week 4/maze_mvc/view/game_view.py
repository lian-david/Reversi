class GameView:
    #view doesn't need __init bc/ view doesn't have attributes it only has functions    
    #view provides functions for displaying things and getting info from user 

    def show_player_location(self, player_location):
        print("Your current location is: ", player_location)

    def get_direction(self):
        direction = int(input("Choose direction (1 - UP, 2 - DOWN, 3 - LEFT, 4 - RIGHT): "))
        return direction

    def display_target_reached(self):
        print("You have reached the target!")