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

    similarity_scores = []

    for value in first_list:
        similarity_score = value * second_list.count(value)
        similarity_scores.append(similarity_score)

    print(f"Total distance: {sum(similarity_scores)}")


if __name__ == "__main__":
    print(main())
