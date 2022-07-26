from warrior import Warrior
from medic import Medic
from warlock import Warlock
from medic_warrior import MedicWarrior

def get_total_power(characters):
    total_power = 0
    for player in characters:
        total_power += player.get_power()

    return total_power

max = Warrior("max", 1, 5, 8)
jenn = Medic("jenn", 2, 3, 80)
bob = Warlock("bob", 3, 2, 90)
gum = MedicWarrior("gum", 4, 4, 80, 9)

characters = [max, jenn, bob, gum]

print(get_total_power(characters))

