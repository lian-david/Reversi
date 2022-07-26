from the_zoo import Zoo

class ZooUserInterface:
    def __init__(self, zoo: Zoo):
        self.zoo = zoo
    
    EXIT_OPTION = "e"   #class attribute can be accessed using self
    def start(self):
        query_text = "Query animal species[s], mass[m], litter[l], venom [v], wingspan[w], talk[t] or exit session[e]? "
        choice = input(query_text)
        while choice != self.EXIT_OPTION:
            name = input("Animal Name? ")
            animal = self.zoo.get_animal(name)
            if not animal:
                print("Animal does not exist in the zoo")
            else:
                self.answer_query(animal, choice)

            choice = input(query_text)
    
    def answer_query(self, animal, choice):
        if choice == "s":
            print(f'{animal.name} species is {animal.species}')
        elif choice == "t":
            if animal.talks:
                print(f'{animal.name} talks.')
                print(animal.phrase)
            else:
                print(f'{animal.name} does not talk.')
            

