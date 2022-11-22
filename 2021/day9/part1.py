import fileinput


def main():

    input_lines = [line.strip() for line in fileinput.input()]

    line_count = len(input_lines)
    line_length = len(input_lines[0])
    blank_map = [[0 for i in range(line_length)] for j in range(line_count)]
    lava_map = blank_map
    for i, line in enumerate(input_lines):
        for j, char in enumerate(line):
            lava_map[i][j] = int(char)

    local_minima = []
    for i in range(line_count):
        for j in range(line_length):
            point = lava_map[i][j]
            if i > 0:  # up
                up = lava_map[i - 1][j]
                if point >= up:
                    continue
            if j < line_length - 1:  # right
                right = lava_map[i][j + 1]
                if point >= right:
                    continue
            if i < line_count - 1:  # down
                down = lava_map[i + 1][j]
                if point >= down:
                    continue
            if j > 0:  # left
                left = lava_map[i][j - 1]
                if point >= left:
                    continue
            local_minima.append((i, j))

    risk_level = 0
    for point in local_minima:
        i, j = point
        risk_level += lava_map[i][j] + 1

    print(risk_level)


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
