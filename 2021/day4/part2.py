import fileinput


class BingoBoard(object):
    def __init__(self, input):
        self.bingo = False
        self.board_values = {}
        self.board = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
        ]

        for row_index, row in enumerate(input):
            for column_index, value in enumerate(row.split()):
                self.board_values[int(value)] = (row_index, column_index)

    def number_drawn(self, number) -> bool:
        number_location = self.board_values.get(number)
        if number_location is not None:
            row, column = number_location
            self.board[row][column] = True

        self.bingo = self.is_bingo()
        self.winning_number = number

    def is_bingo(self):
        for i in range(5):
            row = True
            column = True
            for j in range(5):
                row = row and self.board[i][j]
                column = column and self.board[j][i]
                if not (row or column):
                    break
            if row or column:
                return True

        return False

    def score(self) -> int:
        board_score = 0
        for key, number_location in self.board_values.items():
            row, column = number_location
            if not self.board[row][column]:
                board_score += int(key)

        final_score = board_score * self.winning_number
        return final_score


def main():
    bingo_game = [bit_string.strip() for bit_string in fileinput.input()]
    game_numbers = bingo_game.pop(0).split(",")

    bingo_boards = []
    while len(bingo_game) > 0:
        bingo_game.pop(0)
        board_input = [
            bingo_game.pop(0),
            bingo_game.pop(0),
            bingo_game.pop(0),
            bingo_game.pop(0),
            bingo_game.pop(0),
        ]
        bingo_board = BingoBoard(board_input)
        bingo_boards.append(bingo_board)

    winners = set()
    for game_number in game_numbers:
        game_number = int(game_number)
        print(f"And the number drawn is... {game_number}.")
        for index, bingo_board in enumerate(bingo_boards):
            bingo_board.number_drawn(game_number)

            if bingo_board.bingo and index not in winners:
                winners.add(index)
                print(f"BINGO!!! - player {index}")
                print(f"Score: {bingo_board.score()}")
            else:
                None


if __name__ == "__main__":
    # execute only if run as a script
    print(main())
