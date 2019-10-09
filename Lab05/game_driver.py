from A01166243_1510_labs.Lab05.Lab05 import roll_die, choose_inventory, generate_consonant, generate_vowel, \
    generate_syllable, generate_name, create_character, print_character

inventory = ["Mango's Smashing Steel-Toed Boots",
             "The Swedish Sniper Longbow",
             "Crown of the Mews",
             "Engraved APEX: MMXV Cloak",
             "The Bottomless Hungrypouch",
             "Plup's Sensational Pulper",
             "Zain's Crimson Falchion",
             "Lightning's Summit Axe",
             "The Godslayer's Tome",
             "Cody's Convenient ice Blasting Dragon Wand"]


def main():
    print(roll_die(3, 6))
    print("Welcome! From our selection you've chosen:", choose_inventory(inventory, 3))
    print(generate_consonant())
    print(generate_vowel())
    print(generate_syllable())
    print(generate_name(2))
    print(create_character(2))
    print_character(2)


if __name__ == "__main__":
    main()
