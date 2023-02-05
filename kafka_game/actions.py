def go_north(position):
    i, j = position
    new_position = (i, j + 1)
    return new_position


def go_east(position):
    i, j = position
    new_position = (i + 1, j)
    return new_position


def go_south(position):
    i, j = position
    new_position = (i, j - 1)
    return new_position


def go_west(position):
    i, j = position
    new_position = (i - 1, j)
    return new_position


def look(position):
    return position


def quit_game(position):
    return None
