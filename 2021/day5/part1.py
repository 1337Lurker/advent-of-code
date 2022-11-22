import fileinput
from os import X_OK
from sympy import Segment, oo


def main():
    hydrothermal_vents = [bit_string.strip() for bit_string in fileinput.input()]

    vents = []
    for hydrothermal_vent in hydrothermal_vents:
        point_1, point_2 = [
            tuple(int(number) for number in address.split(","))
            for address in hydrothermal_vent.split(" -> ")
        ]
        vent = Segment(point_1, point_2)
        if vent.slope == 0 or vent.slope == oo:
            vents.append(vent)

    outer_bounds = 0
    for vent in vents:
        vent_max = max(vent.bounds)
        if vent_max > outer_bounds:
            outer_bounds = vent_max + 1

    map_of_vents = [[0] * outer_bounds for i in range(outer_bounds)]
    for index, vent in enumerate(vents):
        for x in range(min(vent.p1.x, vent.p2.x), max(vent.p1.x, vent.p2.x) + 1):
            for y in range(min(vent.p1.y, vent.p2.y), max(vent.p1.y, vent.p2.y) + 1):
                if vent.contains((x, y)):
                    map_of_vents[y][x] += 1 # backwards for visual purposes
        print(f"checked vent #{index}")

    danger_areas = 0
    for row in map_of_vents:
        for column in row:
            if column >= 2:
                danger_areas += 1

    return danger_areas


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
