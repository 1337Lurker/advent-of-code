import fileinput
import re

NUM_1 = "one"
NUM_2 = "two"
NUM_3 = "three"
NUM_4 = "four"
NUM_5 = "five"
NUM_6 = "six"
NUM_7 = "seven"
NUM_8 = "eight"
NUM_9 = "nine"


def main():
    raw_calibrations = [
        re.sub("\n", "", calibration) for calibration in fileinput.input()
    ]
    cleaned_calibrations = [
        re.sub("[A-Za-z]", "", replace_number(calibration))
        for calibration in raw_calibrations
    ]

    calibrations = [int(cal[0] + cal[-1]) for cal in cleaned_calibrations]

    calibration_sum = 0
    for calibration in calibrations:
        calibration_sum += calibration

    print(f"The sum of the calibration values is {calibration_sum}.")
    return calibration_sum


def replace_string_number(string: str) -> str:
    string = string.replace(NUM_1, "o1e", 1)
    string = string.replace(NUM_2, "t2o", 1)
    string = string.replace(NUM_3, "t3", 1)
    string = string.replace(NUM_4, "4", 1)
    string = string.replace(NUM_5, "5e", 1)
    string = string.replace(NUM_6, "6", 1)
    string = string.replace(NUM_7, "7n", 1)
    string = string.replace(NUM_8, "e8t", 1)
    string = string.replace(NUM_9, "n9e", 1)
    return string


def number_in_string(string: str) -> bool:
    if (
        NUM_1 in string
        or NUM_2 in string
        or NUM_3 in string
        or NUM_4 in string
        or NUM_5 in string
        or NUM_6 in string
        or NUM_7 in string
        or NUM_8 in string
        or NUM_9 in string
    ):
        return True
    return False


def replace_number(string: str) -> str:
    if not number_in_string(string):
        return string

    for i in range(3, len(string)+1):
        if number_in_string(string[:i]):
            string = replace_string_number(string[:i]) + string[i:]
            break

    return replace_number(string)


if __name__ == "__main__":
    print(main())
