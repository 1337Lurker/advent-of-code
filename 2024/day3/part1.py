import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    arguments = []
    for row in raw_input:
        matches = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\))", row)
        for match in matches:
            _instruction, multiplier, multiplicand = match
            arguments.append((int(multiplier), int(multiplicand)))
            continue

    print(f"Sum of multiplications: {sum([a*b for a,b in arguments])}")
    return


if __name__ == "__main__":
    print(main())
