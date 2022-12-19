import fileinput


class Computer:
    def __init__(self) -> None:
        self.clock = 0
        self.register = {"X": 1}
        self.signal_strengths = {}
        self.screen = []

    def draw(self):
        sprite_positions = [self.register["X"] + i for i in range(-1,2)]

        # print(f"sprite: {''.join(['#' if i in sprite_positions else '.' for i in range(40)])}")
        # print(f"cursor: {''.join(['#' if i == self.clock else '.' for i in range(40)])}")

        self.screen.append("#" if self.clock % 40 in sprite_positions else ".")

    def increment_clock(self):
        self.draw()
        self.clock += 1

    def add_to_register(self, value, register_name="X"):
        self.register[register_name] += value


def main():
    input_data = []
    with fileinput.input() as file:
        input_data = [line.rstrip("\n") for line in file]

    instructions = [line.split(" ") for line in input_data]

    computer = Computer()
    for instruction in instructions:
        command = instruction[0]
        if command == "noop":
            computer.increment_clock()
        elif command == "addx":
            for i in range(2):
                computer.increment_clock()
                if i == 1:
                    computer.add_to_register(value=int(instruction[1]))
        else:
            raise Exception("Unknown command.")

    for i in range(int(len(computer.screen)/240)):
        print("".join(computer.screen[0:39]))
        print("".join(computer.screen[40:79]))
        print("".join(computer.screen[80:119]))
        print("".join(computer.screen[120:159]))
        print("".join(computer.screen[160:199]))
        print("".join(computer.screen[200:239]))

    return


if __name__ == "__main__":
    print(main())
