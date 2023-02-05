"""Kafka - the adventure game you cannot win."""
from kafka_game.actions import go_north, go_east, go_south, go_west, look, quit_game


def play():

    position = (0, 0)
    alive = True

    while position:
        location = {
            (0, 0): lambda: print("You are in a maze of twisty passages, all alike."),
            (1, 0): lambda: print("You are on a road in a dark forest. To the north you can see a tower."),
            (1, 1): lambda: print("There is a tall tower here, with no obvious door. A path leads east."),

        }

        try:
            location_action = location[position]
        except KeyError:
            print("There is nothing here.")
        else:
            location_action()

        # if position == (0, 0):
        #     print("You are in a maze of twisty passages, all alike.")
        # elif position == (1, 0):
        #     print("You are on a road in a dark forest. To the north you can see a tower.")
        # elif position == (1, 1):
        #     print("There is a tall tower here, with no obvious door. A path leads east.")
        # else:
        #     print("There is nothing here.")

        command = input()



        move_dict = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0), "L": (0, 0), "Q": None}
        if command in move_dict:
            position = (i + move_dict[command][0], j + move_dict[command][1])
        else:
            print("I don't understand")

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

        # i, j = position
        # if command == "N":
        #     position = (i, j + 1)
        # elif command == "E":
        #     position = (i + 1, j)
        # elif command == "S":
        #     position = (i, j - 1)
        # elif command == "W":
        #     position = (i - 1, j)
        # elif command == "L":
        #     pass
        # elif command == "Q":
        #     position = None
        # else:
        #     print("I don't understand")

    print("Game over")

if __name__ == '__main__':
    play()