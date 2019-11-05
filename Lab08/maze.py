def make_board(row_size: int, column_size: int) -> list:
    board = []
    for r in range(row_size):  # Creates a list for each row.
        row = []
        for c in range(column_size):  # Populates the list with a pair of coords for each row.
            row.append((c, r))
        board.append(row)
    return board


def make_character(x_coord, y_coord):
    character = [x_coord, y_coord]
    return character


def user_choice():
    move = input('Where would you like to move? (Use N, S, E, W to move North, South, East or West.) \n')
    return move.capitalize()


def move_character(character_coords, maximum, pos, direction):
    if direction == ('N' or 'W'):
        if character_coords[pos] != 0:
            character_coords[pos] -= 1
    elif direction == ('S' or 'E'):
        if character_coords[pos] != maximum:
            character_coords[pos] += 1


def validate_move(maximum, character, direction):
    if direction == ('N' or 'S'):
        move_character(character, maximum, 0, direction)
    elif direction == ('E' or 'W'):
        move_character(character, maximum, 1, direction)


def display_board(board, character):
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
    character_list = make_character(0, 0)
    board = make_board(5, 5)
    while True:
        display_board(board, character_list)
        character_list = validate_move(5, character_list, user_choice())



def main():
    game()


if __name__ == "__main__":
    main()
