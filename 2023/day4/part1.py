import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    cards = []
    for line in raw_input:
        match = re.fullmatch(
            r"^Card +(?P<card_number>\d+)\:(?P<winning_numbers>( +\d+)+) \|(?P<played_numbers>( +\d+)+)",
            line,
        )
        cards.append(
            Card(
                card_number=match["card_number"],
                winning_numbers=match["winning_numbers"],
                played_numbers=match["played_numbers"],
            )
        )

    point_values = [card.point_value() for card in cards]
    return sum(point_values)


class Card:
    def __init__(self, card_number: int, winning_numbers: str, played_numbers: str):
        self.number = card_number
        wn = [int(number) for number in winning_numbers.strip().split(" ") if number]
        pn = [int(number) for number in played_numbers.strip().split(" ") if number]

        self.winning_numbers = wn
        self.played_numbers = pn

    def point_value(self):
        wins = -1
        for number in self.played_numbers:
            if number in self.winning_numbers:
                wins += 1
        if wins < 0:
            return 0

        point_value = 2**wins
        return point_value


if __name__ == "__main__":
    print(main())
