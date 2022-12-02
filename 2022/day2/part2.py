import fileinput

ROCK, PAPER, SCISSORS, LOSE, DRAW, WIN = "A", "B", "C", "X", "Y", "Z"

RESPONSE = {
    WIN: {ROCK: 8, PAPER: 9, SCISSORS: 7},
    LOSE: {ROCK: 3, PAPER: 1, SCISSORS: 2},
    DRAW: {ROCK: 4, PAPER: 5, SCISSORS: 6},
}


def main():
    score = 0
    with fileinput.input() as game_rounds:
        for game_round in game_rounds:
            opponent, response = game_round.strip().split(" ")
            score += RESPONSE[response][opponent]

    return score


if __name__ == "__main__":
    print(main())
