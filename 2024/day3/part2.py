import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    arguments = []
    enabled = True
    for row in raw_input:
        matches = re.findall(r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))", row)
        for match in matches:
            instruction, multiplier, multiplicand = match
            if instruction.startswith("mul(") and enabled is True:
                arguments.append((int(multiplier), int(multiplicand)))
                continue
            elif instruction == "do()":
                enabled = True
                continue
            elif instruction == "don't()":
                enabled = False
                continue

    print(f"Sum of multiplications: {sum([a*b for a,b in arguments])}")
    return


if __name__ == "__main__":
    print(main())
