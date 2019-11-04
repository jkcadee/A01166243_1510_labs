def make_board(row_size: int, column_size: int) -> list:
    space = 'x'
    board = []
    for r in range(row_size):  # Creates a list for each row.
        row = []
        for c in range(column_size):  # Populates the list with a pair of coords for each row.
            row.append(space)
        board.append(row)
    return board


def make_character():
    character = []
    return character


def user_choice():
    move = input('Where would you like to move? (Use N, S, E, W to move North, South, East or West.) \n')
    return move.capitalize()


# def move_character(board, character_coords):


# def validate_move(board, character, direction):


def game():
    board = make_board(5, 5)
    for x in board:
        print(x)


def main():
    game()


if __name__ == "__main__":
    main()
