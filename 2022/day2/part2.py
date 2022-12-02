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
    game_rounds=[]
    with fileinput.input() as file:
        game_rounds = [line.strip().split(" ") for line in file]

    return sum([OUTCOME_SCORE[desired_outcome][opponent_choice] for opponent_choice, desired_outcome in game_rounds ])


if __name__ == "__main__":
    print(main())
