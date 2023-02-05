"""Kafka - the adventure game you cannot win."""
from kafka_game.actions import go_north, go_east, go_south, go_west, look, quit_game
from kafka_game.location import labyrinth, dark_forest_road, tall_tower, rabbit_hole, lava_pit


def play():
    position = (0, 0)
    alive = True

    while position:
        location = {
            (0, 0): labyrinth,
            (1, 0): dark_forest_road,
            (1, 1): tall_tower,
            (2, 1): rabbit_hole,
            (1, 2): lava_pit,
        }

        try:
            location_action = location[position]
        except KeyError:
            print("There is nothing here.")
        else:
            position, alive = location_action(position, alive)

        if not alive:
            print('You are dead')
            break

        command = input()

        actions = {
            "N": go_north,
            "E": go_east,
            "S": go_south,
            "W": go_west,
            "L": look,
            "Q": quit_game,
        }

        try:
            command_action = actions[command]
        except KeyError:
            print("I don't understand")
        else:
            position = command_action(position)

    else:
        print('You have chosen to leave the game')

    print("Game over")


class STupleTM(tuple):

    def __add__(self, other):
        shorter = self if len(self) <= len(other) else other
        longer = self if len(self) > len(other) else other
        return tuple([x + longer[idx] for idx, x in enumerate(shorter)] + list(longer[len(shorter):]))


# print(STupleTM((1, 2, 3, 4, 5, 'ala')) + STupleTM((3, 5, 6)))
