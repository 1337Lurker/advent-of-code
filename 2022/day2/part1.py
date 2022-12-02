import fileinput

OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"

RESPONSE_ROCK = "X"
RESPONSE_PAPER = "Y"
RESPONSE_SCISSORS = "Z"

DRAW = [
    (OPPONENT_ROCK, RESPONSE_ROCK),
    (OPPONENT_PAPER, RESPONSE_PAPER),
    (OPPONENT_SCISSORS, RESPONSE_SCISSORS),
]
WIN = [
    (OPPONENT_ROCK, RESPONSE_PAPER),
    (OPPONENT_PAPER, RESPONSE_SCISSORS),
    (OPPONENT_SCISSORS, RESPONSE_ROCK),
]


def score_response(response):
    if response == RESPONSE_ROCK:
        return 1
    elif response == RESPONSE_PAPER:
        return 2
    else:
        return 3


def score_game_round(opponent, response) -> int:
    if (opponent, response) in DRAW:
        return score_response(response) + 3
    elif (opponent, response) in WIN:
        return score_response(response) + 6
    else:
        return score_response(response)


def main():
    score = 0
    with fileinput.input() as game_rounds:
        for game_round in game_rounds:
            score += score_game_round(*game_round.strip().split(" "))

    return score


if __name__ == "__main__":
    print(main())
