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

            e1 = int(expense1)
            e2 = int(expense2)

            if e1 + e2 == 2020:
                magic_expenses.append((e1, e2, e1 * e2))

    return magic_expenses


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
