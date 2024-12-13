import fileinput
import re
import numpy
from math import inf


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    city_map = [[column for column in row] for row in raw_input]
    antenna_locations = {}
    for i, row in enumerate(city_map):
        for j, column in enumerate(row):
            if re.search(r"\w", column):
                locations = antenna_locations.get(column, [])
                locations.append((i, j))
                antenna_locations |= {column: locations}
            continue
        continue

    antipode_locations = set()
    for i, row in enumerate(city_map):
        for j, column in enumerate(row):
            for frequency, locations in antenna_locations.items():
                for first_location in locations:
                    first_distance = (i - first_location[0], j - first_location[1])
                    for second_location in [location for location in locations if location != first_location]:
                        second_distance = (i - second_location[0], j - second_location[1])
                        distance_ratio = numpy.divide(first_distance, second_distance)
                        if distance_ratio[0] == distance_ratio[1]: 
                            # in line!
                            antenna_distance_ratio = numpy.divide(first_distance, numpy.subtract(first_location, second_location))
                            if (antenna_distance_ratio[0] in [inf, -inf] or int(antenna_distance_ratio[0]) == antenna_distance_ratio[0]):
                                antipode_locations.add((i,j))
                            continue
                        continue
                    continue
                continue
            continue
        continue

    for line in city_map:
        print("".join(line))
    for i, row in enumerate(city_map):
        for j, column in enumerate(row):
            if (i, j) in antipode_locations:
                city_map[i][j] = "#"
            continue
        continue

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for line in city_map:
        print("".join(line))

    return len(antipode_locations)


if __name__ == "__main__":
    print(main())
