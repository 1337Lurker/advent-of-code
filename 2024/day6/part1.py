import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    lab_floorplan = [[column for column in row] for row in raw_input]

    guard_facing, guard_position = get_guard_position(lab_floorplan)
    positions_visited = [guard_position]
    next_guard_position = next_step(guard_facing, guard_position)
    while inside_lab(lab_floorplan, next_guard_position):
        print(f"The guard is facing {guard_facing} at {guard_position}.")
        if step_is_unobstructed(lab_floorplan, next_guard_position):
            guard_position = next_guard_position
            positions_visited.append(next_guard_position)
        else:
            guard_facing = turn_right(guard_facing)
        next_guard_position = next_step(guard_facing, guard_position)

    return len(set(positions_visited))


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
    if lab_floorplan[next_guard_position[0]][next_guard_position[1]] != "#":
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
        if guard_position[0] < 0 or guard_position[1]<0:
            raise Exception("Guard left the lab.")
        position = lab_floorplan[guard_position[0]][guard_position[1]]
    except:
        return False

    return True


if __name__ == "__main__":
    print(main())
