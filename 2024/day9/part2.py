import fileinput
import re
import math
from copy import deepcopy


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    disk_map = [int(character) for character in list(raw_input[0])]

    files = []
    layout_length = math.ceil(len(disk_map) / 2.0)
    for file_id in range(layout_length):
        file_index = 2 * file_id
        free_space_index = file_index + 1
        if free_space_index < len(disk_map):
            files.append(
                File(
                    id=file_id,
                    files=disk_map[file_index],
                    free_space=disk_map[free_space_index],
                )
            )
        else:
            files.append(File(id=file_id, files=disk_map[file_index]))
        continue

    # print(
    #     "".join([str(file.id) * file.files + "." * file.free_space for file in files])
    # )

    unsorted_files = deepcopy(files)
    sorted_files = []
    while unsorted_files:
        moving_file = files[files.index(unsorted_files.pop())]
        moving_file_index = files.index(moving_file)
        files = [file for file in files if file.id != moving_file.id]
        for index, file in enumerate(files):
            if file.free_space >= moving_file.files and index < moving_file_index:
                files[moving_file_index - 1].free_space += (
                    moving_file.files + moving_file.free_space
                )
                moving_file.free_space = file.free_space - moving_file.files
                file.free_space = 0
                files.insert(files.index(file) + 1, moving_file)
                break
            continue
        if moving_file.id not in [file.id for file in files]:
            if moving_file_index >= len(files):
                files.append(moving_file)
            else:
                files.insert(moving_file_index, moving_file)
        sorted_files.append(moving_file)
        # print(
        #     "".join(
        #         [str(file.id) * file.files + "." * file.free_space for file in files]
        #     )
        # )
        continue

    file_system = []
    for file in files:
        for file_id in range(file.files):
            file_system.append(file.id)
        for file_id in range(file.free_space):
            file_system += "."

    checksum_values = []
    for index, value in enumerate(file_system):
        if value == ".":
            continue
        checksum_values.append(index * int(value))
        continue
    return sum(checksum_values)


class File:
    def __init__(self, id: int, files: int, free_space: int = 0):
        self.id = id
        self.files = files
        self.free_space = free_space

    def __eq__(self, value):
        return self.id == value.id


if __name__ == "__main__":
    print(main())
