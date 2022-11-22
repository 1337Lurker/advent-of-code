import fileinput


def main():
    lines = [line.split(",") for line in fileinput.input()]

    fish_counter_input = [int(fish_counter) for fish_counter in lines[0]]

    fish_counters = {}
    for i in range(9):
        fish_counters[i] = fish_counter_input.count(i)

    print(f"Initial state:\t\t{fish_counters}")

    for day in range(1, 257):
        zero_fish = fish_counters[0]
        one_fish = fish_counters[1]
        two_fish = fish_counters[2]
        three_fish = fish_counters[3]
        four_fish = fish_counters[4]
        five_fish = fish_counters[5]
        six_fish = fish_counters[6]
        seven_fish = fish_counters[7]
        eight_fish = fish_counters[8]

        fish_counters.clear()
        fish_counters[0] = one_fish
        fish_counters[1] = two_fish
        fish_counters[2] = three_fish
        fish_counters[3] = four_fish
        fish_counters[4] = five_fish
        fish_counters[5] = six_fish
        fish_counters[6] = seven_fish + zero_fish
        fish_counters[7] = eight_fish
        fish_counters[8] = zero_fish

        print(f"After \t{day} days:\t\t{fish_counters}")

    return sum(fish_counters.values())


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
