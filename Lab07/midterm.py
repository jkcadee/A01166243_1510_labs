import random


def list_tagger(batch):
    batch.insert(0, len(batch))
    return batch


# print(list_tagger([0, 1, 2]))


def cutoff(int_list, int2):
    counter = 0
    for v in int_list:
        if v % int2 == 0:
            counter += 1
    return counter


# print(cutoff([0, 1, 2], 2))


def prepender(l_string, string2):
    for v in range(0, len(l_string)):
        l_string[v] = string2 + l_string[v]


# a_string = ['cool', 'yes', 'a']
# prepender(a_string, 'a')
# print(a_string)


def name_list():
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


# print(sorted(name_list().items()))


def multiples_of_3(upper_bound):
    return sum([x for x in range(0, upper_bound) if x % 3 == 0])


# print(multiples_of_3(10))


def roll_the_die():
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


print(roll_the_die())