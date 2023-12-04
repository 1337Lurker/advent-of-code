import fileinput
import re
from re import Match
import math

PART_NUMBER_RE = re.compile(r"(\d+)")
GEAR_RE = re.compile(r"\*")


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]
    gear_ratios = []
    for index, line in enumerate(raw_input):
        for star in GEAR_RE.finditer(line):
            gear_ratio = gear_ratio_value(index, raw_input, star)
            if gear_ratio:
                gear_ratios.append(gear_ratio)

    gear_ratios = [gear_ratio for gear_ratio in gear_ratios if gear_ratio]
    print(gear_ratios)
    return sum(gear_ratios)


def gear_ratio_value(index: int, raw_input: str, star_match: Match) -> list[int]:
    gear_ratios = []

    for part_number in adjacent_part_numbers(index - 1, raw_input, star_match):
        gear_ratios.append(part_number)
    for part_number in adjacent_part_numbers(index, raw_input, star_match):
        gear_ratios.append(part_number)
    for part_number in adjacent_part_numbers(index + 1, raw_input, star_match):
        gear_ratios.append(part_number)

    gear_ratios = [gear_ratio for gear_ratio in gear_ratios if gear_ratio]
    if len(gear_ratios) < 2:
        return 0

    final_gear_ratio = math.prod(gear_ratios)
    return final_gear_ratio


def adjacent_part_numbers(index: str, raw_input: str, star_match: Match):
    if index < 0:
        return None
    if index >= len(raw_input):
        return None

    gear_start = max(0, star_match.start()-1)
    gear_end = min(len(raw_input[index]), star_match.end()+1)
    gear_set = set(range(gear_start, gear_end))

    part_numbers = []
    for part_number in PART_NUMBER_RE.finditer(raw_input[index]):
        if not gear_set.isdisjoint(set(range(*part_number.span()))):
            part_numbers.append(int(raw_input[index][part_number.start():part_number.end()]))

    return part_numbers


if __name__ == "__main__":
    print(main())
