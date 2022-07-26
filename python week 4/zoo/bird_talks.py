from bird import Bird

class BirdTalks(Bird):
    def __init__(self, name, animal_type, species, mass, wing, talk, words):
        super().__init__(name, animal_type, species, mass, wing, talk)
        self.words = words

    # def get_wingspan(self):
    #     return self.wing

    # def get_talk(self):
    #     return self.talk

    # def get_words(self):
    #     return self.words
    
    # def get_species(self):
    #     return self.species

    # def get_mass(self):
    #     return self.mass

    def __str__(self):
        return super().__str__() + f'{self.words}'