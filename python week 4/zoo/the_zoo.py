from animal import Animal
# from mammal import Mammal
# from reptile import Reptile
# from bird import Bird
# from bird_talks import BirdTalks

class Zoo:
    """This class stores a collection of animals.
    """
    def __init__(self):
        self.animals = {}       #key = name, value = Animal object

    def add_animal(self, animal: Animal):
        self.animals[animal.name] = animal

    def get_animal(self, name):
        if name in self.animals:
            return self.animals[name]
        else:
            return None



    # def get_animal(source_file):
    #     animals = {}
    #     with open(source_file) as f:
    #         for line in f:
    #             animal = line.split()
            
    #             if animal[1] == "Mammal":
    #                 animals[animal[0]] = Mammal(animal[0], animal[1], animal[2], animal[3], animal[4])
    #             elif animal[1] == "Reptile":
    #                 animals[animal[0]] = Reptile(animal[0], animal[1], animal[2], animal[3], animal[4])
    #             elif animal[1] == "Bird" and animal[5] != "Talks":
    #                 animals[animal[0]] = Bird(animal[0], animal[1], animal[2], animal[3], animal[4], animal[5])
    #             elif animal[1] == "Bird" and animal[5] == "Talks":
    #                 speech = f.readline()
    #                 animals[animal[0]] = BirdTalks(animal[0], animal[1], animal[2], animal[3], animal[4], animal[5], speech)

    #     return animals

