import random


def roll_die(number_of_rolls, number_of_sides):
    """Rolls a die with an inputted amount of rolls and sides."""
    number = 0
    if number_of_rolls < 1 or number_of_sides <= 1:
        return 0
    for x in range(1, number_of_rolls + 1):
        number += random.randint(1, number_of_sides)
    return number


# print(roll_die(3, 6))


def choose_inventory(inventory, selection):
    """Chooses an amount of items from a list depending on the number inputted."""
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


# print(choose_inventory(['Sword', 'Dagger', 'Bow', 'Arrows', 'Leather Armour', 'Chainmail', 'Shield', 'Potions'], 4))
# 'Sword', 'Dagger', 'Bow', 'Arrows', 'Leather Armour', 'Chainmail', 'Shield', 'Potions'

def generate_consonant():
    """Generates a consonant."""
    consonant = "BCDFGHJKLMNPQRSTVWXYZ"
    return random.sample(consonant, 1)


def generate_vowel():
    """Generates a vowel."""
    vowel = "AEIOUY"
    return random.sample(vowel, 1)


def generate_syllable():
    """Generates a syllable using the consonant and vowel."""
    syllable = generate_consonant() + generate_vowel()
    return syllable


def generate_name(syllables):
    """Generates name from amount of syllables inputted."""
    name = generate_syllable() * syllables
    result = ''.join(name).capitalize()
    return result


# print(generate_name(2))

def create_character(name_length):
    """Creates a list with a character's name and stats."""
    if name_length < 0:
        return "No strength of magic can make a name have less than zero characters."
    strength = ['Strength:', roll_die(3, 6)]
    dexterity = ['Dexterity:', roll_die(3, 6)]
    constitution = ['Constitution:', roll_die(3, 6)]
    intelligence = ['Intelligence:', roll_die(3, 6)]
    wisdom = ['Wisdom:', roll_die(3, 6)]
    charisma = ['Charisma:', roll_die(3, 6)]
    character_list = [generate_name(name_length), strength, dexterity, constitution, intelligence, wisdom, charisma]
    return character_list


# print(create_character(1))

def print_character(character):
    """Prints character."""
    print(create_character(character))


# print_character(2)
