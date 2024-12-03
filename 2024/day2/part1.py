import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    safe_levels = 0
    for report in raw_input:
        levels = report.split()
        if is_safe(levels=levels):
            safe_levels += 1
            print(f"Level '{levels}' is Safe")
        else:
            print(f"Level '{levels}' is Unsafe")
        continue

    print(f"There are {safe_levels} safe reports.")


def is_safe(levels: list):
    ascends = values_ascend(levels=levels)
    descends = values_descend(levels=levels)
    if ascends or descends:
        return True
    return False


def values_ascend(levels: list) -> bool:
    for index, level in enumerate(levels):
        if index == 0:
            continue
        current_level = int(level)
        previous_level = int(levels[index - 1])
        if current_level <= previous_level or (current_level - previous_level > 3):
            return False
    return True


def values_descend(levels: list) -> bool:
    levels.reverse()
    reversed_level_ascends = values_ascend(levels)
    levels.reverse()
    return reversed_level_ascends


if __name__ == "__main__":
    print(main())
