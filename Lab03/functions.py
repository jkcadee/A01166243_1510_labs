from random import randrange, sample


def roll_dice(number_of_rolls, number_of_sides):
    random_number = randrange((number_of_rolls / number_of_rolls), ((number_of_sides * number_of_rolls) + 1))
    return random_number


def create_name(length):
    sample()
    return


def main():
    print(roll_dice(1, 20))
    return


if __name__ == "__main__":
    main()


