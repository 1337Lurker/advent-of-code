import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]


if __name__ == "__main__":
    print(main())
