import fileinput
import re
import numpy
from copy import deepcopy


class Trailhead:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

    def __init__(self, start: tuple[int, int]):
        self.start = start
        self.trails = []
        self.score = 0
        self.peaks_reached=set()

    def map_trail(self, topo_map: list[int, int], trail: list[tuple[int, int]]) -> None:
        last_position = trail[-1]
        available_paths = []
        for direction in self.DIRECTIONS:
            next_position = tuple(numpy.add(last_position, direction))
            if (
                next_position[0] >= 0
                and next_position[0] < len(topo_map)
                and next_position[1] >= 0
                and next_position[1] < len(topo_map[0])
            ):
                current_altitude = topo_map[last_position[0]][last_position[1]]
                next_altitude = topo_map[next_position[0]][next_position[1]]
                if next_altitude.isdigit():
                    altitude_gained = int(next_altitude) - int(current_altitude)
                    if altitude_gained == 1:
                        available_paths.append(next_position)
                        if next_altitude=="9":
                            self.peaks_reached.add((next_position))
                            self.update_score()

        if not available_paths:
            self.trails.append(trail)

        for path in available_paths:
            self.map_trail(topo_map=topo_map, trail=(trail + [(path)]))

    def update_score(self):
        self.score = len(self.peaks_reached)

def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    topo_map = [[column for column in list(row)] for row in raw_input]

    trailheads = []
    peaks = []
    for i in range(len(topo_map)):
        for j in range(len(topo_map[i])):
            if topo_map[i][j] == '0':
                trailheads.append(Trailhead(start=(i, j)))
            if topo_map[i][j] == '9':
                peaks.append((i, j))

    for trailhead in trailheads:
        trailhead.map_trail(topo_map, [trailhead.start])
    
    return sum([len([trail for trail in trailhead.trails if trail[-1] in peaks]) for trailhead in trailheads])


if __name__ == "__main__":
    print(main())
