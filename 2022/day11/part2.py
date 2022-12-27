import fileinput
from collections import namedtuple
import re


ThrownItem = namedtuple("ThrownItem", ["monkey_id", "worry_level"])


class Troop:
    def __init__(self) -> None:
        self.monkeys: list[Monkey] = []

    def common_modulo(self):
        modulo = 1
        for monkey in self.monkeys:
            modulo *= monkey.test_modulo
        return modulo

    def inspect_and_throw_items(self):
        for monkey in self.monkeys:
            while monkey.items:
                item = monkey.items[0]
                self.inspect_and_throw_item(monkey.id, item)

    def inspect_and_throw_item(self, monkey_id, item):
        monkey = self.monkeys[monkey_id]
        new_worry_level = monkey.operation(item)
        new_worry_level = new_worry_level % self.common_modulo()

        monkey.items.remove(item)
        monkey.items_inspected += 1
        if monkey.test(new_worry_level):
            catching_monkey = self.monkeys[monkey.test_true_monkey_id]
            catching_monkey.items.append(new_worry_level)
        else:
            catching_monkey = self.monkeys[monkey.test_false_monkey_id]
            catching_monkey.items.append(new_worry_level)


class Monkey:
    def __init__(
        self,
        monkey_id: str,
        items: str,
        operation: str,
        test: str,
        test_true_monkey_id: str,
        test_false_monkey_id: str,
    ) -> None:
        self.id = int(monkey_id)
        self.items = [int(item) for item in items.split(", ")]
        self.items_inspected = 0

        operations = operation.split(" ")
        if operations[1] == "*":
            if operations[2] == "old":
                self.operation = lambda worry: worry * worry
            else:
                self.operation = lambda worry: worry * int(operations[2])
        elif operations[1] == "+":
            if operations[2] == "old":
                self.operation = lambda worry: worry + worry
            else:
                self.operation = lambda worry: worry + int(operations[2])
        else:
            raise Exception("Unknown operator.")

        self.test_modulo = int(test)
        self.test = lambda worry: (worry % self.test_modulo) == 0
        self.test_true_monkey_id = int(test_true_monkey_id)
        self.test_false_monkey_id = int(test_false_monkey_id)


def inventory_monkeys(input_data):
    troop = Troop()
    monkey = []
    for line in input_data:
        monkey_match = re.fullmatch(r"Monkey (?P<monkey_id>\d+):", line)
        if monkey_match:
            monkey.append(monkey_match.group("monkey_id"))
            continue
        starting_items = re.fullmatch(r"  Starting items: (?P<items>.+)", line)
        if starting_items:
            monkey.append(starting_items.groupdict("items")["items"])
            continue
        operation = re.fullmatch(r"  Operation: new = (?P<operation>.+)", line)
        if operation:
            monkey.append(operation.group("operation"))
            continue
        test = re.fullmatch(r"  Test: divisible by (?P<test>\d+)", line)
        if test:
            monkey.append(test.group("test"))
            continue
        test_true = re.fullmatch(
            r"    If true: throw to monkey (?P<monkey_id>\d+)", line
        )
        if test_true:
            monkey.append(test_true.group("monkey_id"))
            continue
        test_false = re.fullmatch(
            r"    If false: throw to monkey (?P<monkey_id>\d+)", line
        )
        if test_false:
            monkey.append(test_false.group("monkey_id"))
            troop.monkeys.append(Monkey(*monkey))
            monkey = []

    return troop


def main():
    input_data = []
    with fileinput.input() as file:
        input_data = [line.rstrip("\n") for line in file]
    troop = inventory_monkeys(input_data)

    for round_number in range(10_000):
        troop.inspect_and_throw_items()
        # if round_number in [0, 19] or (round_number + 1) % 1_000 == 0:
        if (round_number + 1) % 1_000 == 0:
            print(f"== After round {(round_number+1):,} ==")
            for monkey in troop.monkeys:
                print(
                    f"Monkey {monkey.id} inspected items {monkey.items_inspected:,} times."
                )
            print()

    monkey_business = [monkey.items_inspected for monkey in troop.monkeys]
    monkey_business.sort()
    monkey_business.reverse()
    return monkey_business[0] * monkey_business[1]


if __name__ == "__main__":
    print(main())
