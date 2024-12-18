import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    stones = raw_input[0].split()

    # print(" ".join(stones))
    for i in range(25):
        stones = blink(stones)
        # print(" ".join(stones))

    return len(stones)

def apply_rules(stone: str) -> list[str]:
    digits = len(stone)
    if stone == "0":
        return ["1"]
    elif len(stone) % 2 == 0:
        return [stone[0:int(digits/2)], str(int(stone[int(digits/2):digits]))]
    else:
        return[str(int(stone)*2024)]

def blink(stones: list[str])-> list[str]:
    new_stones = []
    for stone in stones:
        new_stones.extend(apply_rules(stone))
    return new_stones

if __name__ == "__main__":
    print(main())
