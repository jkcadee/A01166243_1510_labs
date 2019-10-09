import random


def roll_die(number_of_rolls, number_of_sides):
    number = 0
    if number_of_rolls < 1 or number_of_sides <= 1:
        return 0
    for x in range(1, number_of_rolls + 1):
        number += random.randint(1, number_of_sides)
    return number


# print(roll_die(3, 6))


def choose_inventory(inventory, selection):
    if inventory == [] and selection == 0:
        return []
    elif selection < 0:
        print("Hey! You can't have negative items!")
        return []
    elif selection > len(inventory):
        print("You are over encumbered.")
        return sorted(inventory).copy()
    elif selection == len(inventory):
        return sorted(inventory).copy()
    else:
        result = random.choices(inventory, k=selection)
        return sorted(result)


print(choose_inventory(['Sword', 'Dagger', 'Bow', 'Arrows', 'Leather Armour', 'Chainmail', 'Shield', 'Potions'], 4))


# 'Sword', 'Dagger', 'Bow', 'Arrows', 'Leather Armour', 'Chainmail', 'Shield', 'Potions'
