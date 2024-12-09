import fileinput
import re
import sys
from copy import deepcopy


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    floorplan = [[column for column in row] for row in raw_input]

    sys.setrecursionlimit(100_000)

    guard_facing, guard_position = get_guard_position(floorplan)
    floorplan[guard_position[0]][guard_position[1]] = "G"
    positions_visited = []
    walk(floorplan, deepcopy(guard_facing), deepcopy(guard_position), positions_visited)

    viable_obstructions = set()
    distinct_locations_visited = set([values[1] for values in positions_visited])
    for location in distinct_locations_visited:
        floorplan_copy = deepcopy(floorplan)
        try:
            floorplan_copy[location[0]][location[1]] = "O"
            path = []
            walk(floorplan_copy, deepcopy(guard_facing), deepcopy(guard_position), path)
            continue
        except IndexError:
            continue
        except LoopException:
            viable_obstructions.add(location)

    return len(set(viable_obstructions))


def get_guard_position(lab_floorplan: list[str]) -> tuple[str, tuple[int, int]]:
    for row_index, row in enumerate(lab_floorplan):
        if "^" in row:
            return ("up", (row_index, row.index("^")))
        elif ">" in row:
            return ("right", (row_index, row.index(">")))
        elif "v" in row:
            return ("down", (row_index, row.index("v")))
        elif "<" in row:
            return ("left", (row_index, row.index("<")))
    raise Exception("Guard not found.")


def next_step(guard_facing: str, guard_position: tuple[int, int]) -> tuple[int, int]:
    movement = (0, 0)
    match guard_facing:
        case "up":
            movement = (-1, 0)
        case "right":
            movement = (0, 1)
        case "down":
            movement = (1, 0)
        case "left":
            movement = (0, -1)

    next_guard_position = (
        guard_position[0] + movement[0],
        guard_position[1] + movement[1],
    )
    return next_guard_position


def step_is_unobstructed(
    lab_floorplan: list[str], next_guard_position: tuple[int, int]
) -> tuple[str, tuple[int, int]]:
    if lab_floorplan[next_guard_position[0]][next_guard_position[1]] not in ["#", "O"]:
        return True
    return False


def turn_right(guard_facing: str) -> tuple[int, int]:
    match guard_facing:
        case "up":
            return "right"
        case "right":
            return "down"
        case "down":
            return "left"
        case "left":
            return "up"


def inside_lab(lab_floorplan: list[str], guard_position: tuple[int, int]) -> bool:
    position = ()
    try:
        if guard_position[0] < 0 or guard_position[1] < 0:
            raise Exception("Guard left the lab.")
        position = lab_floorplan[guard_position[0]][guard_position[1]]
    except:
        return False

    return True


class LoopException(Exception):
    pass


def walk(
    lab_floorplan: list[str],
    guard_facing: str,
    guard_position: tuple[int, int],
    positions_visited: list[str, tuple[int, int]],
):
    positions_visited.append((guard_facing, guard_position))
    next_guard_position = next_step(guard_facing, guard_position)
    if inside_lab(lab_floorplan, next_guard_position):
        if step_is_unobstructed(lab_floorplan, next_guard_position):
            if (guard_facing, next_guard_position) in positions_visited:
                raise LoopException()
            lab_floorplan[guard_position[0]][guard_position[1]] = "x"
            guard_position = next_guard_position
            lab_floorplan[guard_position[0]][guard_position[1]] = "G"
        else:
            guard_facing = turn_right(guard_facing)
        walk(lab_floorplan, guard_facing, guard_position, positions_visited)


if __name__ == "__main__":
    print(main())
