import fileinput
import datetime
from sympy import intersection
from sympy.geometry import Point, Segment, Polygon

ORIGIN = Point(0, 0)


def main():
    print(f"starting! {datetime.datetime.now()}")
    line_paths = [paths.split(",") for paths in fileinput.input()]
    lines = [map_line(line_path) for line_path in line_paths]

    print(f"finished importing {datetime.datetime.now()}")

    first_path = lines[0]
    second_path = lines[1]

    print(f"starting intersection search {datetime.datetime.now()}")
    intersections = []
    for first_line in first_path:
        for second_line in second_path:
            intersection_points = intersection(first_line, second_line)
            if len(intersection_points) > 0:
                intersections.append(intersection_points.pop())
    print(f"completed intersection search {datetime.datetime.now()}")


    print(f"starting closest intersection search {datetime.datetime.now()}")
    closest_point = ORIGIN
    for point in intersections:
        if point.is_zero:
            continue

        if closest_point.is_zero:
            closest_point = point

        if point.taxicab_distance(ORIGIN) < closest_point.taxicab_distance(ORIGIN):
            closest_point = point
    print(f"finished closest intersection search {datetime.datetime.now()}")

    print(f"closest intersection: {closest_point} @ {closest_point.taxicab_distance(ORIGIN)} units")


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
