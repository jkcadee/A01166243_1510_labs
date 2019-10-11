from A01166243_1510_labs.Lab05.Lab05 import choose_inventory, create_character, print_character

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
    print("\n")
    print(f"Welcome to the shop! Here is our selection: \n {inventory}")

    print("\n")

    my_inventory = choose_inventory(inventory, 5)
    print(f"From our selection you've chosen: {my_inventory}")

    print("\n")
    my_character = create_character(2)
    my_character.append(my_inventory)
    print_character(my_character)


if __name__ == "__main__":
    main()
