from players import Player

class Warlock(Player):
    def __init__(self, name, location, life, magical):
        super().__init__(name, location, life)
        self.magical = magical

    def get_power(self):
        self.power = (self.life * 5) + (self.magical * 0.2)
        return self.power