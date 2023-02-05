def labyrinth(position, alive):
    print("You are in a maze of twisty passages, all alike.")
    return position, alive


def dark_forest_road(position, alive):
    print("You are on a road in a dark forest. To the north you can see a tower.")
    return position, alive


def tall_tower(position, alive):
    print("There is a tall tower here, with no obvious door. A path leads east.")
    return position, alive


def rabbit_hole(position, alive):
    print("You fall down a rabbit hole into a labyrinth.")
    return (0, 0), alive


def lava_pit(position, alive):
    print('You fall into a lava pit')
    return position, False
