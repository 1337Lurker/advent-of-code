import fileinput
import re
from re import Match

PART_NUMBER_RE = re.compile("(\d+)")
SYMBOL_RE = re.compile("[^\.\d]")


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    part_numbers = []
    not_part_numbers = []
    for index, line in enumerate(raw_input):
        matches = PART_NUMBER_RE.finditer(line)
        for match in matches:
            if is_part_number(index=index, match=match, input=raw_input):
                part_numbers.append(int(match.group(0)))
            else:
                not_part_numbers.append(int(match.group(0)))

    print(f"The sum of part numbers is {sum(part_numbers)}")


def is_part_number(index: int, match: Match, input: list[str]) -> bool:
    return (
        symbol_present(index=index - 1, input=input, match=match)
        or symbol_present(index=index, input=input, match=match)
        or symbol_present(index=index + 1, input=input, match=match)
    )


def symbol_present(index: int, input: str, match: Match):
    if index < 0 or index >= len(input):
        return False

    line = input[index]
    start = max(0, match.start() - 1)
    end = min(len(line), match.end() + 1)
    if SYMBOL_RE.search(input[index][start:end]):
        return True


if __name__ == "__main__":
    print(main())
