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
    inventory = []
