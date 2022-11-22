import fileinput
import math


def main():
    instructions = [ instruction.strip().split() for instruction in fileinput.input()]

    position = {"horizontal": 0, "depth": 0}

    for direction, magnitude in instructions:
        magnitude = int(magnitude)

        if direction == "forward":
            position["horizontal"] = position["horizontal"] + magnitude
        elif direction == "down":
            position["depth"] = position["depth"] + magnitude
        elif direction == "up":
            position["depth"] = position["depth"] - magnitude
        else:
            raise Exception

    print(position)

    return position["horizontal"] * position["depth"]

if __name__ == "__main__":
    # execute only if run as a script
    print(main())
