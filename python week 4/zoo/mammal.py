from animal import Animal

class Mammal(Animal):
    """Represents a mammal
    """
    def __init__(self, name, animal_type, species, mass, litter_size):
        super().__init__(name, animal_type, species, mass)
        self.litter_size = litter_size

    # def get_litter(self):
    #     return self.litter_size

    # def get_species(self):
    #     return self.species

    # def get_mass(self):
    #     return self.mass

    def __str__(self):
        return super().__str__() + f'{self.litter_size}'