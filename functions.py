import random


def roll_dice(number_of_rolls, number_of_sides):
    return random.randint(number_of_rolls, (number_of_rolls * number_of_sides))


def create_name(length):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    selected_letters = random.sample(letters, length)
    selected_letters = selected_letters[0] + selected_letters[1] + selected_letters[2]
    return selected_letters.capitalize()


def main():
    print(roll_dice(3, 6))
    print(create_name(3))
    return


if __name__ == "__main__":
    main()
