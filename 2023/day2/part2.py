import fileinput
import re
import math

DICE_RED = "red"
DICE_GREEN = "green"
DICE_BLUE = "blue"

DICE_COLORS = [DICE_RED, DICE_GREEN, DICE_BLUE]


def main():
    raw_input = [re.sub("\n", "", line) for line in fileinput.input()]

    games = []
    for line in raw_input:
        game = Game(number=re.search("Game (\d+):", line).group(1))
        for index, game_round in enumerate(re.split(";", line)):
            game.rounds.append({})
            dice_pulled = re.split(",", game_round)
            for dice in dice_pulled:
                quantity, color = re.search("(\d+) (red|green|blue)", dice).groups()
                game.rounds[index][color] = int(quantity)
        games.append(game)

    game_powers = []
    for game in games:
        game_powers.append(game.power())

    return sum(game_powers)


class Game:
    def __init__(self, number: str):
        self.number = int(number)
        self.rounds = []
        self.minimum_dice = {
            DICE_RED: 0,
            DICE_GREEN: 0,
            DICE_BLUE: 0,
        }

    def power(self):
        for game_round in self.rounds:
            for color in DICE_COLORS:
                if game_round.get(color, 0) > self.minimum_dice[color]:
                    self.minimum_dice[color] = game_round.get(color, 0)

        print(self.minimum_dice)
        game_power = math.prod(self.minimum_dice.values())
        print(f"Game {self.number} power: {game_power}")
        return game_power


if __name__ == "__main__":
    print(main())
