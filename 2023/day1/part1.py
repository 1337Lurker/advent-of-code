import fileinput
import re

NUMBERS = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]


def main():
    raw_calibrations = [
        re.sub("\n", "", calibration) for calibration in fileinput.input()
    ]

    calibrations = [
        calibration_to_int(
            re.findall(
                "(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))",
                calibration,
            )
        )
        for calibration in raw_calibrations
    ]

    print(f"The sum of the calibration values is {sum(calibrations)}.")
    return sum(calibrations)


def calibration_to_int(matches: list) -> int:
    return int(replace_string_numbers(matches[0] + matches[-1]))


def replace_string_numbers(string: str) -> str:
    for number in NUMBERS:
        string = string.replace(*number)
    return string


if __name__ == "__main__":
    print(main())
