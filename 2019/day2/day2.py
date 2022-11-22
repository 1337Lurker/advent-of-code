import fileinput
import sys


def main():
    with open(sys.argv[1]) as intcode:
        opcodes = [int(opcode) for opcode in intcode.read().split(",")]
        print(f"before: {opcodes}")
        op_position = 0

        while op_position >= 0:
            op_position = execute(opcodes, op_position)

        print(f"after: {opcodes}")


def execute(opcodes, op_position):
    if opcodes[op_position] == 99:
        return -1

    first_location = opcodes[op_position + 1]
    second_location = opcodes[op_position + 2]
    third_location = opcodes[op_position + 3]

    if opcodes[op_position] == 1:
        opcodes[third_location] = opcodes[first_location] + opcodes[second_location]
        return op_position + 4
    elif opcodes[op_position] == 2:
        opcodes[third_location] = opcodes[first_location] * opcodes[second_location]
        return op_position + 4
    else:
        print("something went wrong!")
        return -1


if __name__ == "__main__":
    # execute only if run as a script
    main()

