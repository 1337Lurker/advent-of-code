import fileinput
import re


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
    antipode_locations = {}
    for i, row in enumerate(city_map):
        for j, column in enumerate(row):
            for frequency, locations in antenna_locations.items():
                distances = []
                for location in locations:
                    horizontal_offset = i - location[0]
                    vertical_offset = j - location[1]
                    if horizontal_offset!=0 and vertical_offset!=0:
                        distances.append((vertical_offset, horizontal_offset))
                for distance in distances:
                    doubled_distance = tuple(2 * d for d in distance)
                    if doubled_distance in distances:
                        locations = antipode_locations.get(frequency, [])
                        locations.append((i, j))
                        antipode_locations |= {frequency: locations}
                    continue
                continue
            continue
        continue

    for line in city_map:
        print(line)
    for i, row in enumerate(city_map):
        for j, column in enumerate(row):
            for locations in antipode_locations.values():
                if (i,j) in locations:
                    city_map[i][j] = "#"
                    break
                continue
            continue
        continue

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for line in city_map:
        print(line)

    distinct_antipodes = set(location 
                          for antipodes in antipode_locations.values()
                          for location in antipodes)
    
    return len(distinct_antipodes)


if __name__ == "__main__":
    print(main())
