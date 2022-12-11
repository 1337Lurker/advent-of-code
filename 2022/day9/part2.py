import fileinput
import re

UP, DOWN, LEFT, RIGHT = "U", "D", "L", "R"
MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT = (0, 1), (0, -1), (-1, 0), (1, 0)
LINEAR_MOVEMENTS = [MOVE_UP, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT]
DIAGONAL_MOVEMENTS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


class Rope:
    def __init__(self) -> None:
        self.rope_segments: list[tuple[int, int]] = [(0, 0)] * 10
        self.tail_history: set[tuple[int, int]] = {(0, 0)}

    def adjacent_positions(self, position: tuple[int, int] | None):
        if not position:
            return {}

        adjacent_positions = {
            (position[0] + i, position[1] + j)
            for i in range(-1, 2)
            for j in range(-1, 2)
        }

        return adjacent_positions

    def move(self, direction):
        if direction == UP:
            self._move(*MOVE_UP)
        elif direction == DOWN:
            self._move(*MOVE_DOWN)
        elif direction == LEFT:
            self._move(*MOVE_LEFT)
        elif direction == RIGHT:
            self._move(*MOVE_RIGHT)
        else:
            raise Exception("Unknown direction.")

    def _move(
        self,
        x_movement,
        y_movement,
        index=0,
        lead_position: tuple[int, int] | None = None,
    ):
        if index >= len(self.rope_segments):
            return
        old_position = self.rope_segments[index]
        new_position = self.rope_segments[index]

        if not lead_position:
            new_position = (
                old_position[0] + x_movement,
                old_position[1] + y_movement,
            )
        elif old_position not in self.adjacent_positions(lead_position):
            if (
                old_position[0] == lead_position[0]
                or old_position[1] == lead_position[1]
            ):
                for movement in LINEAR_MOVEMENTS:
                    position = (
                        old_position[0] + movement[0],
                        old_position[1] + movement[1],
                    )
                    if position in self.adjacent_positions(lead_position):
                        new_position = position
                        break
            else:
                for movement in DIAGONAL_MOVEMENTS:
                    position = (
                        old_position[0] + movement[0],
                        old_position[1] + movement[1],
                    )
                    if position in self.adjacent_positions(lead_position):
                        new_position = position
                        break

        self.rope_segments[index] = new_position
        if index + 1 == len(self.rope_segments):
            self.tail_history.add(new_position)

            output = [[], [], [], [], [], [], [], [], []]
            i = 0
            for x_pos in range(9):
                for y_pos in range(9):
                    if (x_pos, y_pos) in self.rope_segments:
                        output[i].append(str(self.rope_segments.index((x_pos, y_pos))))
                    elif (x_pos, y_pos) in self.tail_history:
                        output[i].append("#")
                    else:
                        output[i].append(".")
                i += 1
            for x_pos in range(-1, -10, -1):
                print(" ".join(output[x_pos]) + "\n")
            print("---------")

        self._move(
            x_movement=x_movement,
            y_movement=y_movement,
            index=index + 1,
            lead_position=new_position,
        )


def main():
    input_data = []
    with fileinput.input() as file:
        input_data = [line.rstrip("\n") for line in file]

    instructions = [line.split(" ") for line in input_data]

    rope = Rope()
    for instruction in instructions:
        direction, quantity = instruction
        for i in range(0, int(quantity)):
            rope.move(direction)
    return len(rope.tail_history)


if __name__ == "__main__":
    print(main())
