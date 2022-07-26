from abc import ABC
class Animal(ABC):
    """Represents animal 
    """
    def __init__(self, name, animal_type, species, mass):
        """Initializes animal's base attributes
        """
        self.name = name
        self.animal_type = animal_type
        self.species = species
        self.mass = mass

    def __str__(self):
        return f'{self.name} {self.animal_type} {self.species} {self.mass}'

    