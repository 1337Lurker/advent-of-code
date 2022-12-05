import fileinput
import re


def main():
    input_data = []
    with fileinput.input() as file:
        input_data = [line.rstrip("\n") for line in file]

    stack_index = 0
    move_index = 0
    for line_index, line in enumerate(input_data):
        if line.startswith(" 1 "):
            stack_index = line_index
        if line.startswith("move"):
            move_index = line_index
            break

    number_of_stacks = max(
        [int(stack) for stack in input_data[stack_index].split(" ") if stack]
    )

    supply_stacks = [[] for _i in range(number_of_stacks)]
    for line_index in range(stack_index, 0, -1):
        line_index = line_index - 1
        stacks = re.findall(r"(?<=\[)([A-Z])(?=\])| {3} ?", input_data[line_index])
        for i, stack in enumerate(stacks):
            if stack:
                supply_stacks[i].append(stack)

    for line in range(move_index, len(input_data)):
        match = re.match(r"move (\d+) from (\d+) to (\d+)", input_data[line])
        if not match:
            raise Exception("Something has gone terribly wrong.")
        quantity, source, destination = match.groups()
        for i in range(int(quantity)):
            box = supply_stacks[int(source) - 1].pop()
            supply_stacks[int(destination) - 1].append(box)
        pass

    top_crates = ""
    for stack in supply_stacks:
        top_crates += stack.pop()

    return top_crates


if __name__ == "__main__":
    print(main())
