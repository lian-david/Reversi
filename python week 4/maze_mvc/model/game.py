from model.directions import Direction

class Game:
    DIRECTION_MOVE = {
        Direction.UP: (0, -1),
        Direction.DOWN: (0, 1),
        Direction.LEFT: (-1, 0),
        Direction.RIGHT: (1, 0)
    }

    def __init__(self, width=3, height=5):
        self.width = width
        self.height = height
        self.target_location = (self.width - 1, self.height - 1) #the bottom right corner
        self.player_location = (0, 0)   # (x, y), the top left corner
    
    def get_location(self):
        return self.player_location

    def move(self, direction: Direction):
        # if direction == Direction.UP:       #y -> y - 1
        #     new_location = self.player_location + (0, -1)
        # elif direction == Direction.DOWN:
        #     new_location = self.player_location + (0, 1) 

        move = self.DIRECTION_MOVE[direction]
        new_location = (self.player_location[0] + move[0], self.player_location[1] + move[1])
        if 0 <= new_location[0] < self.width \
            and 0 <= new_location[1] < self.height:
            self.player_location = new_location

    def is_terminated(self):
        return self.player_location == self.target_location

