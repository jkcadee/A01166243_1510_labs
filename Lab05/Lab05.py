import random


def roll_die(number_of_rolls, number_of_sides):
    """Rolls a die with an inputted amount of rolls and sides."""
    number = 0
    if number_of_rolls < 1 or number_of_sides <= 1:
        return 0
    for x in range(1, number_of_rolls + 1):
        number += random.randint(1, number_of_sides)
    return number


"""
Return the sum of a integer created from a set of random numbers based on the number of rolls and the die's sides.

:param number_of_rolls: positive integer, must be more than 1.
:param number_of_sides: positive integer, must be more than 0.
:precondition: Both parameters must be positive integers and rolls must be more than 1.
:postcondition: Receive an integer equivalent to the sum of a "die" created by the number_of_sides and rolled however
                many times as specified by number_of_rolls.
:return: An integer equal to the sum of a die created by number_of_sides rolled by number_of_rolls times.
"""


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
        over_encumbered_list = inventory.copy()
        return sorted(over_encumbered_list)
    elif selection == len(inventory):
        equal_list = inventory.copy()
        return sorted(equal_list)
    else:
        result = random.choices(inventory, k=selection)
        return sorted(result)


"""
Return a list, with your chosen number of items as how many elements are in the list.

:param inventory: A list with at least one element in it.
:param selection: A positive integer.
:precondition: List must hae at least one element in it, and integer must be positive.
:postcondition: Create a list with the same amount of elements as what is specified in the parameter.
:return: A list with the chosen amount of elements (determined by parameter) in it. 
"""


# print(choose_inventory(['Sword', 'Dagger', 'Bow', 'Arrows', 'Leather Armour', 'Chainmail', 'Shield', 'Potions'], 4))
# 'Sword', 'Dagger', 'Bow', 'Arrows', 'Leather Armour', 'Chainmail', 'Shield', 'Potions'

def generate_consonant():
    """Generates a consonant."""
    consonant = "BCDFGHJKLMNPQRSTVWXYZ"
    return random.sample(consonant, 1)


"""
Return a list of one character selected randomly from the string of consonants

:postcondition: Return a list of one character selected randomly from the string.
:return: A list with a single character. 
"""


def generate_vowel():
    """Generates a vowel."""
    vowel = "AEIOUY"
    return random.sample(vowel, 1)


"""
Return a list of one character randomly selected from the string of vowels.

:postcondition: Return a list of one character selected randomly from the string.
:return: A list with a single character.
"""


def generate_syllable():
    """Generates a syllable using a consonant and a vowel."""
    syllable = generate_consonant() + generate_vowel()
    return syllable


"""
Return a list with two characters, one generated by generate_consonant and the other by generate_vowel

:postcondition: Create a list of two characters, generated by the helper functions.
:return: A list with two characters.
"""


def generate_name(syllables):
    """Generates a name from the amount of syllables inputted."""
    syllable = ''
    for x in range(1, syllables + 1):
        name = ''.join(generate_syllable())
        syllable += name
    return syllable.capitalize()


"""
Return a string created by calling generate_syllable the amount of times syllables is called

:param syllables: A positive integer.
:precondition: Syllables must be a positive integer.
:postcondition: Creating a string with however many syllables as specified by the parameter.  
:return: A string with however many syllables as specified by the parameter.
"""


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


"""
Return a list with the name of the character and their stats.

:param name_length: A positive integer.
:precondition: Parameter must be a positive integer over 0.
:postcondition: Create a list with the name and stats of the character.
:return: A list with a name and stats.
"""

# print(create_character(1))


def print_character(character, i, s):
    """Prints character."""
    character_list = create_character(character)
    inventory_list = choose_inventory(i, s)
    character_list.append(inventory_list)
    print(character_list)


"""
Print a list with a name the length of the parameter and the stats.

:param character: A positive integer over 0.
:precondition: Parameter must be positive and over 0.
:postcondition: Print created list from create_character.
:return: Print a list with a name and stats.
"""

# print_character(2)
