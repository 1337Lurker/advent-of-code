import fileinput
import re

UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"


class Rope:
    def __init__(self) -> None:
        self.rope_segments: list[tuple[int, int]] = [(0, 0)]*2
        self.tail_history: set[tuple[int, int]] = {(0, 0)}

    def move(self, direction):
        if direction == UP:
            self.move_up()
        elif direction == DOWN:
            self.move_down()
        elif direction == LEFT:
            self.move_left()
        elif direction == RIGHT:
            self.move_right()
        else:
            raise Exception("Unknown direction.")

    def adjacent_positions(self, position: tuple[int, int]):
        adjacent_positions = {
            (position[0] + i, position[1] + j)
            for i in range(-1, 2)
            for j in range(-1, 2)
        }

        return adjacent_positions

    def _move(self, x_movement, y_movement):
        prior_lead_position = tuple()
        for i in range(0, len(self.rope_segments)):
            if i == 0:
                prior_lead_position = self.rope_segments[i]
                self.rope_segments[i] = (
                    prior_lead_position[0] + x_movement,
                    prior_lead_position[1] + y_movement,
                )
            else:
                if self.rope_segments[i] in self.adjacent_positions(
                    self.rope_segments[i - 1]
                ):
                    continue
                else:
                    position = self.rope_segments[i]
                    self.rope_segments[i] = prior_lead_position
                    prior_lead_position = position
                    if i + 1 == len(self.rope_segments):
                        self.tail_history.add(self.rope_segments[i])

    def move_up(self):
        self._move(0, 1)

    def move_down(self):
        self._move(0, -1)

    def move_left(self):
        self._move(-1, 0)

    def move_right(self):
        self._move(1, 0)


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
