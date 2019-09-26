import random


def roll_dice(number_of_rolls, number_of_sides):
    """Creates a number between the first parameter and the product of the two parameters"""
    return random.randint(number_of_rolls, (number_of_rolls * number_of_sides))


"""
Return a number between the first parameter and the first and second parameter multiplied together.

:param number_of_rolls: int
:param number_of_sides: int
:precondition: Both parameters must be ints 
:postcondition: A number between the first parameter and the product of the two parameters
:return: A random number between the first parameter and the product of the two parameters 
"""


def create_name(length):
    """Creates a string as long as the number in the parameter"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    selected_letters = random.sample(letters, length)
    selected_letters = selected_letters[0] + selected_letters[1] + selected_letters[2]
    return selected_letters.capitalize()


"""
Return a string the length of the parameter.

:param: int
:precondition: The parameter must be an int
:postcondition: A string the length of the parameter
:return: A string made of random characters the length of the parameter
"""


def main():
    """Executes the program"""
    print(roll_dice(3, 6))
    print(create_name(3))
    return


if __name__ == "__main__":
    main()
