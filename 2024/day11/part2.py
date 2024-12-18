import fileinput
import re
from collections import Counter

STONE_RESULT = {}


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    stones = Counter(raw_input[0].split())

    for _ in range(75):
        stones = blink(stones)

    return sum(stones.values())


def blink(stones: Counter) -> Counter:
    new_stones = Counter()
    for stone, count in stones.items():
        digits = len(stone)
        midpoint = int(digits / 2)

        if stone == "0":
            new_stones["1"] += count
        elif digits % 2 == 0:
            left, right = stone[:midpoint], str(int(stone[midpoint:]))
            new_stones[left] += count
            new_stones[right] += count
        else:
            new_stones[str(int(stone) * 2024)] += count

    return new_stones


if __name__ == "__main__":
    print(main())
