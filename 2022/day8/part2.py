import fileinput


class Forest:
    NORTH = -1
    SOUTH = 1
    EAST = 1
    WEST = -1

    def __init__(self, data: list[str]) -> None:
        self.trees = [[height for height in list(row)] for row in data]

        self.north_edge = 0
        self.south_edge = len(self.trees) - 1
        self.east_edge = max([len(row) for row in self.trees]) - 1
        self.west_edge = 0

        self.edge_rows = (self.north_edge, self.south_edge)
        self.edge_columns = (self.east_edge, self.west_edge)

    def scenic_score(self, tree_row, tree_column):
        if tree_row in self.edge_rows or tree_column in self.edge_columns:
            return 0

        scenic_tree_height = self.trees[tree_row][tree_column]

        visibility_north = 0
        for row in range(tree_row, self.north_edge, self.NORTH):
            visibility_north += 1
            if scenic_tree_height <= self.trees[row + self.NORTH][tree_column]:
                break

        visibility_south = 0
        for row in range(tree_row, self.south_edge, self.SOUTH):
            visibility_south += 1
            if scenic_tree_height <= self.trees[row + self.SOUTH][tree_column]:
                break

        visibility_east = 0
        for column in range(tree_column, self.east_edge, self.EAST):
            visibility_east += 1
            if scenic_tree_height <= self.trees[tree_row][column + self.EAST]:
                break

        visibility_west = 0
        for column in range(tree_column, self.west_edge, self.WEST):
            visibility_west += 1
            if scenic_tree_height <= self.trees[tree_row][column + self.WEST]:
                break

        return visibility_north * visibility_south * visibility_east * visibility_west


def main():
    input_data = []
    with fileinput.input() as file:
        input_data = [line.rstrip("\n") for line in file]
    forest = Forest(input_data)

    bottom_row = len(forest.trees)
    right_column = max([len(row) for row in forest.trees])
    edge_rows = (0, bottom_row)
    edge_columns = (0, right_column)

    return max(
        [
            forest.scenic_score(row, column)
            for row in range(*edge_rows)
            for column in range(*edge_columns)
        ]
    )


if __name__ == "__main__":
    print(main())
