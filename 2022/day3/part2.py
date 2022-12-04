import fileinput
import string

ITEM_TYPES=[''] + list(string.ascii_lowercase) + list(string.ascii_uppercase)

class Rucksack:
    def __init__(self, contents) -> None:
        self.full_contents = set(contents.strip())

def main():
    priority_sums = 0
    elf_rucksacks=[]
    with fileinput.input() as rucksacks:
        for rucksack in rucksacks:
            elf_rucksacks.append(Rucksack(rucksack))

    for i in range(int(len(elf_rucksacks)/3)):
        badge = elf_rucksacks[i*3].full_contents & elf_rucksacks[i*3+1].full_contents & elf_rucksacks[i*3+2].full_contents
        priority_sums += ITEM_TYPES.index(badge.pop())

    return priority_sums

if __name__ == "__main__":
    print(main())
