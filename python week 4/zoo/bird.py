from animal import Animal

class Bird(Animal):
    """Represents a bird
    """
    def __init__(self, name, animal_type, species, mass, wing, talk, phrase = ""):
        super().__init__(name, animal_type, species, mass)
        self.wing = wing
        self.talk = talk
        self.phrase = phrase

    # def get_wingspan(self):
    #     return self.wing

    # def get_talk(self):
    #     return self.talk
    
    # def get_species(self):
    #     return self.species

    # def get_mass(self):
    #     return self.mass

    def __str__(self):
        return super().__str__() + f'{self.wing} {self.talk} {self.get_words()}'
        