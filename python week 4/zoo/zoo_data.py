from the_zoo import Zoo
from mammal import Mammal
from bird import Bird
from reptile import Reptile

class ZooData:
    """This class reads the zoo data from a text file
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        zoo = Zoo()
        with open(self.file_path) as f:
            line = f.readline()
            while line:
                fields = line.split()

                #get the common attributes
                name, animal_type, species, mass = fields[:4]

                #read the additional attributes according to the animal
                if animal_type == "Mammal":
                    litter_size = int(fields[-1])
                    animal = Mammal(name, animal_type, species, mass, litter_size)

                elif animal_type == "Reptile":
                    venomous = (fields[-1] == "Venomous")     #converts to Boolean to return T/F
                    animal = Reptile(name, animal_type, species, mass, venomous)

                elif animal_type == "Bird":
                    wing_span = int(fields[-2])
                    talks = (fields[-1] == "Talks")
                    if talks:
                        phrase = f.readline()
                    else:
                        phrase = ""
                    animal = Bird(name, animal_type, species, mass, wing_span, talks, phrase)

                #add the animal to the zoo 
                zoo.add_animal(animal)
                line = f.readline()
                
        return zoo
