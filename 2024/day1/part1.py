import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    first_list = []
    second_list = []
    for row in raw_input:
        first_str, second_str = row.split()
        first_val = int(first_str)
        second_val = int(second_str)
        first_list.append(first_val)
        second_list.append(second_val)
        continue
    first_list.sort()
    second_list.sort()

    distances = []

    for val1, val2 in zip(first_list, second_list):
        distances.append(abs(val1 - val2))

    print(f"Total distance: {sum(distances)}")


if __name__ == "__main__":
    print(main())
