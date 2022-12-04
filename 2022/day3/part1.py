import fileinput
import string

ITEM_TYPES = [""] + list(string.ascii_lowercase) + list(string.ascii_uppercase)


class Rucksack:
    def __init__(self, contents) -> None:
        list_of_contents = list(contents.strip())
        item_count = len(list_of_contents)
        self.first_container = set(list_of_contents[0 : int(item_count / 2)])
        self.second_container = set(list_of_contents[int(item_count / 2) : item_count])

    def shared_items(self):
        return self.first_container & self.second_container


def main():
    priority_sums = 0
    elf_rucksacks = []
    with fileinput.input() as rucksacks:
        for rucksack in rucksacks:
            elf_rucksack = Rucksack(rucksack)
            for shared_item in elf_rucksack.shared_items():
                priority_sums += ITEM_TYPES.index(shared_item)

    return priority_sums


if __name__ == "__main__":
    print(main())
