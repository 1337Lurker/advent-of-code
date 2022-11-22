import fileinput
import math


def main():
    depths = [int(depth.strip()) for depth in fileinput.input()]

    third_preceding, second_preceding, first_preceding, current = None, None, None, None
    increments = 0
    for depth in depths:
        third_preceding = second_preceding
        second_preceding = first_preceding
        first_preceding = current
        current = depth
        if first_preceding is None or second_preceding is None or third_preceding is None:
            continue

        preceding_triplet = third_preceding + second_preceding + first_preceding
        current_triplet = second_preceding + first_preceding + current

        if current_triplet > preceding_triplet:
            increments +=1
            print(f"depth: {0} {1}", current, "(increased)" )
        elif current_triplet == preceding_triplet:
            print(f"depth: {0} {1}", current, "(no change)" )
        else:
            print(f"depth: {0} {1}", current, "(decreased)" )

    print(increments)


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
