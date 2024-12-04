import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]
    puzzle = [[letter for letter in row] for row in raw_input]
    row_count = len(raw_input)
    column_count = len(raw_input[0])

    matches = 0
    for i in range(1, row_count-1):
        for j in range(1,column_count-1):
            if puzzle[i][j] == "A":
                pos_diag = puzzle[i+1][j-1] + puzzle[i][j] + puzzle[i-1][j+1]
                neg_diag = puzzle[i-1][j-1] + puzzle[i][j] + puzzle[i+1][j+1]
                if (pos_diag == "MAS"or pos_diag == "SAM")and (neg_diag =="MAS" or neg_diag=="SAM"):
                    matches +=1

    print(f"{matches} were found")


def search(line: list) -> int:
    if len(line) < 4:
        return 0
    matches = re.findall(r"(XMAS)", line)
    matches.extend(re.findall(r"(SAMX)", line))
    return len(matches)


if __name__ == "__main__":
    print(main())
