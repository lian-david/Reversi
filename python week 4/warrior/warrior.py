from players import Player

class Warrior(Player):
    def __init__(self, name, location, life, sword):
        super().__init__(name, location, life)
        self.sword = sword

    def get_power(self):
        self.power = self.life * 3
        return self.power