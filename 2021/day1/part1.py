import fileinput
import math


def main():
    depths = [int(depth.strip()) for depth in fileinput.input()]

    prev, current = None, None
    increments = 0
    for depth in depths:
        prev = current
        current = depth
        if prev is None:
            continue
        elif current > prev:
            increments +=1
            print(f"depth: {0} {1}", current, "(increased)" )
        else:
            print(f"depth: {0} {1}", current, "(decreased)" )

    print(increments)


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
