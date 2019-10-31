import random
import doctest


def list_tagger(batch):
    """Returns a list with an added value which is the length of the whole list.

    :precondition: List must have more than 0 values.
    :postcondition: Inserts a new value into the list at index 0 which is the length of the list.
    :return: A list with an inserted value at index 0 which is the length of the list.

    >>> list_tagger([0, 3, 7])
    [3, 0, 3, 7]
    >>> list_tagger([8])
    [1, 8]
    """
    batch.insert(0, len(batch))
    return batch


def cutoff(int_list, int2):
    """Returns an integer of the amount of values that are a multiple of the parameter int2.

    :param int_list: A list.
    :precondition: Must be a list with more than 0 values.
    :param int2: An integer.
    :precondition: Must be an integer over 0.
    :postcondition: Adds 1 to a counter that indicates how many numbers are multiples of the parameter int2.
    :return: An integer that signifies how many numbers in int_list are multiples of int2.

    >>> cutoff([4], 4)
    1
    >>> cutoff([2, 5, 6, 9, 10], 5)
    2
    >>> cutoff([0], 1)
    1
    """
    counter = 0
    for v in int_list:
        if v % int2 == 0:
            counter += 1
    return counter


def prepender(l_string, string2):
    """Returns a list of strings with the parameter string2 concatenated in the front.

    :param l_string: A list.
    :precondition: Must be a list with only strings and have more than 0 values.
    :param string2: A string.
    :precondition: Must be a string with at least 1 character in it.
    :postcondition: Concatenates string2 in front of each string in the list.
    :return: A list with the parameter string2 concatenated to the front of each string in it.
    """
    for v in range(0, len(l_string)):
        l_string[v] = string2 + l_string[v]


def name_list():
    """Returns a dictionary of names, with the keys the length of the names.

    :precondition: Dictionary must have at least 1 name in it with a length of over 1.
    :postcondition: Creates a dictionary with the keys as the length of the names and the values a sublist with names
    that are the same length as the key.
    :return: A dictionary that has keys that are the length of the names, and the values a sublist of names that are
    that length.
    """
    name_dict = {}
    while True:
        names = input('Input names here: \nType quit to exit. \n')
        if names == 'quit':
            break
        if len(names) not in name_dict:
            name_dict[len(names)] = [names]
        else:
            name_dict[len(names)].append(names)
    return name_dict


def multiples_of_3(upper_bound):
    """Returns an integer which is the sum of a list with only numbers that are multiples of three and under the
    parameter upper_bound.

    :param upper_bound: An integer.
    :precondition: Must be an integer higher than 0.
    :postcondition: Returns an integer that is equal to the sum of values that are multiples of three and under the
    parameter.
    :return: An integer that represents the sum of the values underneath the parameter.

    >>> multiples_of_3(10)
    18
    >>> multiples_of_3(2)
    0
    """
    return sum([x for x in range(0, upper_bound) if x % 3 == 0])


def roll_the_die():
    """Prints a dictionary that signifies how many times a particular side has been rolled.

    :precondition: The inputted values for number_of_sides and number_of_rolls must be over 0.
    :postcondition: Roll a die until it has been rolled the specified amount of times and store each time a side is
    rolled as a counted value in the dictionary
    :return: Print a dictionary that signifies how many times a side has been rolled.
    """
    number_of_sides = int(input('Number of sides: '))
    number_of_rolls = int(input('Number of rolls: '))
    counter = 0
    die_dict = {k: 0 for k in range(1, number_of_sides + 1)}
    while counter < number_of_rolls:
        rolling_die = random.randint(1, number_of_sides)
        if rolling_die in die_dict:
            die_dict[rolling_die] += 1
        counter += 1
    for side, rolls in die_dict.items():
        print(f'{side}: {rolls}')


def main():
    """Runs the functions inside of the block."""
    print(list_tagger([0, 1, 2]))
    print(cutoff([0, 1, 2], 2))
    a_string = ['cool', 'yes', 'a']
    prepender(a_string, 'a')
    print(a_string)
    print(sorted(name_list().items()))
    print(multiples_of_3(10))
    print(roll_the_die())


if __name__ == "__main__":
    main()
    doctest.testmod()
