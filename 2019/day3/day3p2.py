import fileinput
import datetime
from sympy import intersection
from sympy.geometry import Point, Segment, Polygon

ORIGIN = Point(0, 0)


def main():
    line_paths = [paths.split(",") for paths in fileinput.input()]
    lines = [map_line(line_path) for line_path in line_paths]

    first_path = lines[0]
    second_path = lines[1]

    intersections = []
    for i, first_line in enumerate(first_path):
        for j, second_line in enumerate(second_path):
            intersection_points = intersection(first_line, second_line)
            if len(intersection_points) > 0:
                intersection_point = intersection_points.pop()
                if intersection_point.is_nonzero:
                    intersections.append(((i, j), intersection_point))

    shortest_steps = 0
    for indices, point in intersections:
        first_path_distance, second_path_distance = 0, 0
        for index, segment in enumerate(first_path):
            if index < indices[0]:
                first_path_distance += int(segment.length)
        for index, segment in enumerate(second_path):
            if index < indices[1]:
                second_path_distance += int(segment.length)

        first_path_distance = int(first_path_distance) + int(point.distance(first_path[indices[0]].p1))
        second_path_distance = int(second_path_distance) + int(point.distance(second_path[indices[1]].p1))

        total_distance = first_path_distance + second_path_distance

        if shortest_steps == 0 or shortest_steps > total_distance:
            shortest_steps = total_distance

    print(shortest_steps)


def map_line(line_path):
    origin_point = ORIGIN
    line = []

    for path in line_path:
        if path[0] == "U":
            new_point = (origin_point[0], origin_point[1] + int(path[1:]))
            line.append(Segment(origin_point, new_point))
            origin_point = new_point
        elif path[0] == "D":
            new_point = (origin_point[0], origin_point[1] - int(path[1:]))
            line.append(Segment(origin_point, new_point))
            origin_point = new_point
        elif path[0] == "L":
            new_point = (origin_point[0] - int(path[1:]), origin_point[1])
            line.append(Segment(origin_point, new_point))
            origin_point = new_point
        elif path[0] == "R":
            new_point = (origin_point[0] + int(path[1:]), origin_point[1])
            line.append(Segment(origin_point, new_point))
            origin_point = new_point
        else:
            raise Exception("wut")

    return line


if __name__ == "__main__":
    # execute only if run as a script
    main()
