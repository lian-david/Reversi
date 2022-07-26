from players import Player

class Medic(Player):
    def __init__(self, name, location, life, healing):
        super().__init__(name, location, life)
        self.healing = healing

    def get_power(self):
        self.power = (self.life * 2) + (self.healing * 0.1)
        return self.power