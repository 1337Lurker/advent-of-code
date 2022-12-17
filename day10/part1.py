import fileinput


class Computer:
    def __init__(self) -> None:
        self.clock = 1
        self.register = {"X": 1}
        self.signal_strengths = {}

    def increment_clock(self):
        self.clock += 1
        if self.clock % 20 == 0:
            self.record_signal_strength()

    def record_signal_strength(self):
        self.signal_strengths[self.clock] = self.clock * self.register["X"]

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
                if i == 1:
                    computer.add_to_register(value=int(instruction[1]))
                computer.increment_clock()
        else:
            raise Exception("Unknown command.")

    interesting_clock_cycles = [20, 60, 100, 140, 180, 220]
    signal_strengths = [
        signal_strength
        for clock_cycle, signal_strength in computer.signal_strengths.items()
        if clock_cycle in interesting_clock_cycles
    ]

    return sum(signal_strengths)


if __name__ == "__main__":
    print(main())
