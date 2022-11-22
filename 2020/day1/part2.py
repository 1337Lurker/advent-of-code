import fileinput
import math


def main():
    print("hello world")
    expenses = [expense for expense in fileinput.input()]
    print(expenses)

    magic_expenses = []

    for i, expense1 in enumerate(expenses):
        for j, expense2 in enumerate(expenses):
            if j <= i:
                continue

            for k, expense3 in enumerate(expenses):
                if k <= j:
                    continue

                e1 = int(expense1)
                e2 = int(expense2)
                e3 = int(expense3)

                if e1 + e2 + e3 == 2020:
                    magic_expenses.append((e1, e2, e3, e1 * e2 * e3))

    return magic_expenses


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
