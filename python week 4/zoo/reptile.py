from animal import Animal

class Reptile(Animal):
    """Represents a reptile
    """
    def __init__(self, name, animal_type, species, mass, venomous):
        super().__init__(name, animal_type, species, mass)
        self.venomous = venomous

    # def get_venom(self):
    #     return self.venomous

    # def get_species(self):
    #     return self.species

    # def get_mass(self):
    #     return self.mass

    def __str__(self):
        return super().__str__() + f'{self.venomous}'