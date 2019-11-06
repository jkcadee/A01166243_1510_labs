import doctest


def make_board(row_size: int, column_size: int) -> list:
    """
    Returns a game board with rows of lists that contain tuples by index (x, y).

    :param row_size: Int.
    :precondition: Must be an integer.
    :param column_size: Int.
    :precondition: Must be an integer.
    :postcondition: Creates a list with sub-lists containing tuples (x-coord, y-coord)
    :return: A list with (x-coord, y-coord) tuples. (0 - 4)

    >>> make_board(1, 1)
    [[(0, 0)]]
    >>> make_board(2, 2)
    [[(0, 0), (1, 0)], [(0, 1), (1, 1)]]
    """
    board = []
    for r in range(row_size):  # Creates a list for each row.
        row = []
        for c in range(column_size):  # Populates the list with a pair of coords for each row.
            row.append((c, r))
        board.append(row)
    return board


def make_character(x_coord: int, y_coord: int) -> list:
    """
    Returns a character list with an x-coord and a y-coord in it.

    :param x_coord: Int.
    :precondition: Must be an integer >= 0.
    :param y_coord: Int.
    :precondition: Must be an integer >= 0.
    :postcondition: Creates a character object with a list containing the parameters inside of them.
    :return: A list with an x-coord and a y-coord within it.

    >>> make_character(1, 1)
    [1, 1]
    >>> make_character(0, 0)
    [0, 0]
    """
    character = [x_coord, y_coord]
    return character


def user_choice():
    """
    Returns a user input of N, S, E, W.

    :precondition: Input must be N, S, E, W.
    :postcondition: Returns the input capitalized.
    :return: The input capitalized.
    """
    move = input('Where would you like to move? (Use N, S, E, W to move North, South, East or West.) \n')
    return move.capitalize()


def move_character(character_coords: list, maximum: int, pos: int, direction: str) -> list:
    """
    Returns a list of changed character coordinates. The function also checks if the move is valid.

    N and W always subtract 1 from the position, and S and E always add one to the position.

    :param character_coords: A list.
    :precondition: Must be a list.
    :param maximum: An int.
    :precondition: Must be an integer.
    :param pos: An int.
    :precondition: Must be an integer.
    :param direction: A string.
    :precondition: Must be a string.
    :postcondition: Returns the changed character list with either 1 added to x, y or 1 subtracted from x, y positions.
    :return: A list with 1 added to x, y or 1 subtracted from x, y positions. Will not move is coords == 0 or maximum.

    >>> move_character([0, 0], 5, 1, 'S')
    [0, 1]
    >>> move_character([0, 0], 5, 1, 'N')
    [0, 0]
    >>> move_character([0, 0], 5, 1, 'W')
    [0, 0]
    >>> move_character([0, 0], 5, 1, 'E')
    [0, 1]
    """
    if direction in ('N', 'W'):
        if character_coords[pos] != 0:
            character_coords[pos] -= 1
    elif direction in ('S', 'E'):
        if character_coords[pos] != maximum - 1:
            character_coords[pos] += 1
    return character_coords


def validate_move(maximum: int, character: list, direction: str) -> list:
    """
    Returns a list with the modified character list from move_character.

    When direction is N or S, 1 is added or subtracted from the y-coord. When direction is E or W, 1 is added or
    subtracted from the x-coord,

    :param maximum: An int.
    :precondition: Must be an integer.
    :param character: A list.
    :precondition: Must be a list.
    :param direction: A string.
    :precondition: Must be a string.
    :postcondition: Returns the changed character list from move_character depending on which direction was selected.
    :return: A list modified by move_character depending on the direction selected.

    >>> validate_move(5, [0, 0], 'N')
    [0, 0]
    >>> validate_move(5, [0, 0], 'S')
    [1, 0]
    >>> validate_move(5, [0, 0], 'E')
    [0, 1]
    >>> validate_move(5, [0, 0], 'W')
    [0, 0]
    """
    if direction in ('N', 'S'):
        character = move_character(character, maximum, 0, direction)
    elif direction in ('E', 'W'):
        character = move_character(character, maximum, 1, direction)
    return character


def check_exit_reached(minimum: int, maximum: int) -> list:
    """
    Returns a list containing the minimum and maximum coord for the exit.

    :param minimum: An int.
    :precondition: Must be an integer.
    :param maximum: An int.
    :precondition: Must be an integer.
    :postcondition: Stores the coord pair for the exit.
    :return: Returns the coord pair for the exit.

    >>> check_exit_reached(5, 5)
    [4, 4]
    >>> check_exit_reached(4, 4)
    [3, 3]
    """
    the_exit = [minimum - 1, maximum - 1]
    return the_exit


def display_board(board: list, character: list):
    """
    Prints an 'x' for an empty space, and a 'c' for where the character is.

    :param board: A list.
    :precondition: Must be a list.
    :param character: A list.
    :precondition: Must be a list.
    :postcondition: Prints an empty space 'x' and the character's location 'c'.

    >>> display_board([[(0, 0), (1, 0)], [(0, 1), (1, 1)]], [0, 0])
    c x
    x x
    >>> display_board([[(0, 0), (1, 0)], [(0, 1), (1, 1)]], [1, 1])
    x x
    x c
    """
    for index in range(len(board)):
        for index_two in range(len(board[index])):
            current_position = [index, index_two]
            if current_position == character:
                if index_two == len(board[index]) - 1:
                    print('c')
                else:
                    print('c', end=" ")
            else:
                if index_two == len(board[index]) - 1:
                    print('x')
                else:
                    print('x', end=" ")


def game():
    """
    Runs the game functions with the logic to create the scenario.

    :return: When the exit is reached, printing 'You won!' and ending the infinite loop.
    """
    character_list = make_character(0, 0)
    board = make_board(5, 5)
    found_exit = False
    while not found_exit:
        display_board(board, character_list)
        character_list = validate_move(5, character_list, user_choice())
        if character_list == check_exit_reached(5, 5):
            display_board(board, character_list)
            print('\n You won!')
            found_exit = True


def main():
    """Runs the functions."""
    game()
    doctest.testmod()


if __name__ == "__main__":
    main()
