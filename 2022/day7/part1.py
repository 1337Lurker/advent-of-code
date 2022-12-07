import fileinput
import re


class File:
    def __init__(self, file_size: str, file_name: str) -> None:
        self.file_size = int(file_size)
        self.file_name = file_name


class Directory:
    def __init__(self, name: str) -> None:
        self.name = name
        self.directories = []
        self.files = []

    def all_directories(self):
        directories = []
        for directory in self.directories:
            directories.extend(directory.all_directories())
        directories.append(self)

        return directories

    def size(self):
        nested_folders_size = sum([directory.size() for directory in self.directories])
        nested_files_size = sum( [file.file_size for file in self.files])
        return nested_folders_size + nested_files_size


def main():
    input_data = []
    with fileinput.input() as file:
        input_data = [line.rstrip("\n") for line in file]

    root_directory = Directory("/")
    pwd = [root_directory]
    current_directory = pwd[-1]

    for line in input_data:
        if line == "$ cd /":
            continue
        if line == "$ ls":
            continue

        if line == "$ cd .." and len(pwd) > 1:
            pwd.pop()
            current_directory = pwd[-1]
            continue

        cd_in = re.match(r"\$ cd (?P<directory_name>.+)", line)
        if cd_in:
            for directory in current_directory.directories:
                if directory.name == cd_in.group("directory_name"):
                    current_directory = directory
                    pwd.append(current_directory)
                    print("/".join([d.name for d in pwd]))
            continue

        ls_directory = re.match(r"dir (?P<directory_name>.+)", line)
        if ls_directory:
            current_directory.directories.append(
                Directory(ls_directory.group("directory_name"))
            )
            continue
        ls_file = re.match(r"(?P<file_size>\d+) (?P<file_name>.+)", line)
        if ls_file:
            current_directory.files.append(
                File(ls_file.group("file_size"), ls_file.group("file_name"))
            )
            continue

    directories = []
    for directory in root_directory.all_directories():
        if directory.size() <= 100000:
            directories.append(directory)

    return sum([directory.size() for directory in directories])


if __name__ == "__main__":
    print(main())
