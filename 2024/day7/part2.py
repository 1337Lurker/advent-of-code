import fileinput
import re
from operator import add, mul
from itertools import product


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    operators = [add, mul, concat]

    equations = []
    for line in raw_input:
        raw_calibration, raw_operands = line.split(":", 1)
        calibration = int(raw_calibration)
        operands = [int(i) for i in raw_operands.strip().split()]
        equations.append((calibration, operands))

        continue

    valid_calibrations = []
    for calibration, operands in equations:
        for operator_product in product(operators, repeat=(len(operands) - 1)):
            calculation = 0
            for index, operand in enumerate(operands):
                if index == 0:
                    calculation += operand
                else:
                    calculation = operator_product[index - 1](calculation, operand)
            if calibration == calculation:
                valid_calibrations.append(calibration)
                break
    return sum(valid_calibrations)


def formula(calibration, operators: list, operands: list[int]) -> bool:
    for operator in operators:
        operator(operands.pop(0), operands.pop(0))

    return False

def concat(first_operand: int, second_operand: int) -> int:
    return int(str(first_operand) + str(second_operand))

if __name__ == "__main__":
    print(main())
