import fileinput
import re


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    cards = {}
    card_quantities = {}
    for index, line in enumerate(raw_input):
        cards[index + 1] = Card(line=line)
        card_quantities[index + 1] = 1

    for card_number, card in cards.items():
        for i in range(1, card.wins() + 1):
            card_quantities[card_number + i] += 1 * card_quantities[card_number]

            continue

    return sum(card_quantities.values())

    # while card_numbers:
    #     card_number = card_numbers.pop(0)
    #     card_index = card_number - 1
    #     card = Card(line=raw_input[card_index])
    #     cards_won.append(card)
    #     for i in range(card.wins()):
    #         card_won = card.number + i+1
    #         card_numbers.append(card_won)
    #     continue
    # return len(cards_won)


class Card:
    def __init__(self, line: str):
        match = re.fullmatch(
            r"^Card +(?P<card_number>\d+)\:(?P<winning_numbers>( +\d+)+) \|(?P<played_numbers>( +\d+)+)",
            line,
        )

        self.number = int(match["card_number"])
        self.winning_numbers = [
            int(number)
            for number in match["winning_numbers"].strip().split(" ")
            if number
        ]
        self.played_numbers = [
            int(number)
            for number in match["played_numbers"].strip().split(" ")
            if number
        ]

    def wins(self):
        wins = 0
        for number in self.played_numbers:
            if number in self.winning_numbers:
                wins += 1
        return wins

    def point_value(self):
        if self.wins() == 0:
            return 0

        point_value = 2 ** (self.wins() - 1)
        return point_value


if __name__ == "__main__":
    print(main())
