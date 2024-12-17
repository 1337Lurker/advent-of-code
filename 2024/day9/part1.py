import fileinput
import re
import math


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    disk_map = [int(character) for character in list(raw_input[0])]

    files = []
    layout_length = math.ceil(len(disk_map) / 2.0)
    for i in range(layout_length):
        file_index = 2 * i
        free_space_index = file_index + 1
        if free_space_index < len(disk_map):
            files.append(
                File(
                    id=i,
                    files=disk_map[file_index],
                    free_space=disk_map[free_space_index],
                )
            )
        else:
            files.append(File(id=i, files=disk_map[file_index]))
        continue

    file_system = []
    for file in files:
        for i in range(file.files):
            file_system.append(file.id)
        for i in range(file.free_space):
            file_system += "."

    # print("".join(file_system))

    for i in range(len(file_system)-1, 0, -1):
        if file_system[0 : file_system.index(".")] == [
            file for file in file_system if file != "."
        ]:
            break

        if file_system[i] == ".":
            continue

        free_space_index = file_system.index(".", 0, i)

        file_system[free_space_index] = file_system[i]
        file_system[i] = "."
        # print("".join(file_system))

    checksum_values = []
    for index, value in enumerate(file_system):
        if value == ".":
            break
        checksum_values.append(index * int(value))
        continue
    return sum(checksum_values)


class File:
    def __init__(self, id: int, files: int, free_space: int = 0):
        self.id = id
        self.files = files
        self.free_space = free_space


if __name__ == "__main__":
    print(main())
