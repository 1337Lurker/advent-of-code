import fileinput
import math


def main():
    instructions = [ instruction.strip().split() for instruction in fileinput.input()]

    position = {"horizontal": 0, "depth": 0, "aim": 0}

    for direction, magnitude in instructions:
        magnitude = int(magnitude)

        if direction == "forward":
            position["horizontal"] = position["horizontal"] + magnitude
            position["depth"] = position["depth"] + (position["aim"] * magnitude)
        elif direction == "down":
            position["aim"] = position["aim"] + magnitude
        elif direction == "up":
            position["aim"] = position["aim"] - magnitude
        else:
            raise Exception

    print(position)

    return position["horizontal"] * position["depth"]

if __name__ == "__main__":
    # execute only if run as a script
    print(main())
