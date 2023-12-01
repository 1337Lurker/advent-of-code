import fileinput
import re

NUMBERS = [
    ("one", "o1e"),
    ("two", "t2o"),
    ("three", "t3e"),
    ("four", "f4r"),
    ("five", "f5e"),
    ("six", "s6x"),
    ("seven", "s7n"),
    ("eight", "e8t"),
    ("nine", "n9e"),
]


def main():
    raw_calibrations = [
        re.sub("\n", "", calibration) for calibration in fileinput.input()
    ]
    cleaned_calibrations = [
        re.sub("[A-Za-z]", "", replace_string_numbers(calibration))
        for calibration in raw_calibrations
    ]

    calibrations = [int(cal[0] + cal[-1]) for cal in cleaned_calibrations]

    calibration_sum = 0
    for calibration in calibrations:
        calibration_sum += calibration

    print(f"The sum of the calibration values is {calibration_sum}.")
    return calibration_sum


def replace_string_numbers(string: str) -> str:
    for number in NUMBERS:
        string = string.replace(*number)
    return string


if __name__ == "__main__":
    print(main())
