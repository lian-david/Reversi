from medic import Medic

class MedicWarrior(Medic):
    def __init__(self, name, location, life, healing, sword):
        super().__init__(name, location, life, healing)
        self.sword = sword

    def get_power(self):
        warrior = self.life * 3
        medic = (self.life * 2) + (self.healing * 0.1)
        if warrior > medic:
            self.power = warrior
        elif medic > warrior:
            self.power = medic
        return self.power