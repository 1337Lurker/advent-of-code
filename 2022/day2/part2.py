import fileinput

ROCK, PAPER, SCISSORS, LOSE, DRAW, WIN = "A", "B", "C", "X", "Y", "Z"
SCORE = {ROCK: 1, PAPER: 2, SCISSORS: 3, WIN: 6, LOSE: 0, DRAW: 3}
OUTCOME_SCORE = {
    WIN: {
        ROCK: SCORE[PAPER] + SCORE[WIN],
        PAPER: SCORE[SCISSORS] + SCORE[WIN],
        SCISSORS: SCORE[ROCK] + SCORE[WIN],
    },
    LOSE: {
        ROCK: SCORE[SCISSORS] + SCORE[LOSE],
        PAPER: SCORE[ROCK] + SCORE[LOSE],
        SCISSORS: SCORE[PAPER] + SCORE[LOSE],
    },
    DRAW: {
        ROCK: SCORE[ROCK] + SCORE[DRAW],
        PAPER: SCORE[PAPER] + SCORE[DRAW],
        SCISSORS: SCORE[SCISSORS] + SCORE[DRAW],
    },
}


def main():
    score = 0
    with fileinput.input() as game_rounds:
        for game_round in game_rounds:
            opponent_play, desired_outcome = game_round.strip().split(" ")
            score += OUTCOME_SCORE[desired_outcome][opponent_play]

    return score


if __name__ == "__main__":
    print(main())
