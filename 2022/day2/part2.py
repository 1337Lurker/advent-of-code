import fileinput

ROCK = "A"
PAPER = "B"
SCISSORS = "C"

RESPONSE_LOSE = "X"
RESPONSE_DRAW = "Y"
RESPONSE_WIN = "Z"

DRAW = {
    ROCK: ROCK,
    PAPER: PAPER,
    SCISSORS: SCISSORS,
}
WIN = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}
LOSE={
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}


def score_response(response):
    if response == ROCK:
        return 1
    elif response == PAPER:
        return 2
    else:
        return 3


def score_game_round(opponent, response) -> int:
    if response == RESPONSE_DRAW:
        return score_response(DRAW[opponent]) + 3
    elif response == RESPONSE_WIN:
        return score_response(WIN[opponent]) + 6
    else:
        return score_response(LOSE[opponent])


def main():
    score = 0
    with fileinput.input() as game_rounds:
        for game_round in game_rounds:
            score += score_game_round(*game_round.strip().split(" "))

    return score


if __name__ == "__main__":
    print(main())
