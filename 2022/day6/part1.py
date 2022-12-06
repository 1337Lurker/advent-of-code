import fileinput
import re


def main():
    input_data = []
    with fileinput.input() as file:
        input_data = [line.rstrip("\n") for line in file]

    signal = input_data[0]
    for i in range(len(signal)):
        header = set(signal[i:i+4])
        if len(header) == 4:
            return i+4


if __name__ == "__main__":
    print(main())
