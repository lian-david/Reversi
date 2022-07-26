from zoo_data import ZooData
from zoo_UI import ZooUserInterface

data = ZooData("zoo.txt")
zoo = data.read_file()
ui = ZooUserInterface(zoo)
ui.start()

# from the_zoo import get_animal
# from animal import Animal
# from mammal import Mammal
# from reptile import Reptile
# from bird import Bird
# from bird_talks import BirdTalks

# zoo = get_animal("zoo.txt")

# def handle_option(option):
#     if option == "s":
#         name = input("Animal Name?")
#         if name in zoo:
#             animal = zoo[name]
#             print(f'{name} species is {animal.species}')
#     elif option == "m":
#         name = input("Animal Name?")
#         if name in zoo:
#             animal = zoo[name]
#             print(f'{name} mass is {animal.mass}')
#     elif option == "l":
#         name = input("Animal Name?")
#         if name in zoo:
#             animal = zoo[name]
#             print(f'{name} litter size is {animal.litter_size}')
#     elif option == "v":
#         name = input("Animal Name?")
#         if name in zoo:
#             animal = zoo[name]
#             print(f'{name} is {animal.venomous}')
#     elif option == "w":
#         name = input("Animal Name?")
#         if name in zoo:
#             animal = zoo[name]
#             print(f'{name} has a wingspan of {animal.wing}')
#     elif option == "t":
#         name = input("Animal Name?")
#         if name in zoo:
#             animal = zoo[name]
#             if animal.talk == "Talks":
#                 print(f'{name} {animal.talk}. {name} says {animal.words}')
#             else:
#                 print(f'{name} is {animal.talk}')
    

# query = "Query animal species[s], mass[m], litter[l], venom [v], wingspan[w], talk[t] or exit session[e]?"
# print(query)
# option = input()
# EXIT_OPTION = "e"

# while option != EXIT_OPTION:
#     handle_option(option)
#     print(query)
#     option = input()

# if option == EXIT_OPTION:
#     print("Goodbye!")