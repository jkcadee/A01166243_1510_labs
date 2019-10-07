import random


def roll_die(number_of_rolls, number_of_sides):
    result = random.randint(number_of_rolls, number_of_sides * number_of_rolls)
    return result


def main():
    print(roll_die(3, 6))


if __name__ == "__main__":
    main()