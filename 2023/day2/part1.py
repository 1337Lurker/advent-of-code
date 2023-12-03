import fileinput
import re

DICE_RED="red"
DICE_GREEN="green"
DICE_BLUE="blue"

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

    valid_games = []
    for game in games:
        if game.is_valid():
            valid_games.append(game.number)

    return sum(valid_games)

class Game:
    def __init__(self, number: str):
        self.number = int(number)
        self.rounds = []

    def is_valid(self) -> bool:
        dice_count={"red":12, "green": 13, "blue": 14}
        for game_round in self.rounds:
            for color in DICE_COLORS:
                if game_round.get(color, 0) > dice_count[color]:
                    return False

        return True


if __name__ == "__main__":
    print(main())
