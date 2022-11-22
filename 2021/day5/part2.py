import fileinput
from os import X_OK
from sympy import Segment, Point, oo
from sympy.geometry.point import Point2D


def main():
    hydrothermal_vents = [bit_string.strip() for bit_string in fileinput.input()]

    vents = []
    for hydrothermal_vent in hydrothermal_vents:
        point_1, point_2 = [
            tuple(int(number) for number in address.split(","))
            for address in hydrothermal_vent.split(" -> ")
        ]
        x1, y1 = point_1
        x2, y2 = point_2
        vent = None
        if x1 < x2:
            vents.append(Segment(point_1, point_2))
        elif x1 == x2:
            if y1 < y2:
                vents.append(Segment(point_1, point_2))
            else:
                vents.append(Segment(point_2, point_1))
        else:
            vents.append(Segment(point_2, point_1))

    outer_bounds = 0
    for vent in vents:
        vent_max = max(vent.bounds)
        if vent_max > outer_bounds:
            outer_bounds = vent_max + 1

    map_of_vents = [[0] * outer_bounds for i in range(outer_bounds)]
    for index, vent in enumerate(vents):
        x, y = vent.p1
        while True:
            if vent.contains((x, y)):
                map_of_vents[y][x] += 1  # backwards for visual purposes
            if Point(x, y) == vent.p2:
                break
            if vent.slope != oo:
                x += 1
                y += vent.slope
            else:
                y += 1

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
