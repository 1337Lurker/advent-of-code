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
        replace_string_numbers(
            "".join(
                re.findall(
                    "(?=([1-9]|one|two|three|four|five|six|seven|eight|nine))",
                    calibration,
                )
            )
        )
        for calibration in raw_calibrations
    ]

    calibrations = [int(cal[0] + cal[-1]) for cal in calibrations]

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
