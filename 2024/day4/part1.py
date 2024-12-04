import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]
    input_array = [[letter for letter in row] for row in raw_input]
    row_count = len(raw_input)
    column_count = len(raw_input[0])
    max_count = max(row_count, column_count)

    lines = [row for row in raw_input]

    for i in range(2 * max_count):
        negative_diagonal = ""
        positive_diagonal = ""
        for j in range(2 * max_count):
            if (i - j) in range(row_count) and (j) in range(column_count):
                negative_diagonal += input_array[i - j][j]
            if (row_count - i + j - 1) in range(row_count) and j in range(column_count):
                positive_diagonal += input_array[row_count - i + j - 1][j]

        lines.append(negative_diagonal)
        lines.append(positive_diagonal)

    for i in range(column_count):
        vertical = ""
        for j in range(row_count):
            if i in range(column_count) and j in range(row_count):
                vertical += input_array[j][i]
        lines.append(vertical)

    matches = 0
    for line in lines:
        matches += search(line=line)

    print(f"{matches} were found")


def search(line: list) -> int:
    if len(line) < 4:
        return 0
    matches = re.findall(r"(XMAS)", line)
    matches.extend(re.findall(r"(SAMX)", line))
    return len(matches)


if __name__ == "__main__":
    print(main())
