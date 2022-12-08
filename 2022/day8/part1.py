import fileinput
from typing import List


class Tree:
    def __init__(self, height: str, row_number, column_number) -> None:
        self._height = int(height)
        self._row_number = row_number
        self._column_number = column_number
    def height(self):
        return self._height

    def row(self):
        return self._row_number

    def column(self):
        return self._column_number

    def is_neighbor(self, row: int, column: int):
        neighbor_addresses = [
            (row, column - 1),  # Left
            (row, column + 1),  # Right
            (row - 1, column),  # Down
            (row + 1, column),  # Up
        ]
        if (self.row(), self.column()) in neighbor_addresses:
            return True
        return False


class Forest:
    def __init__(self, forest: List[List[str]]) -> None:
        self.trees = [
            Tree(column, row_number, column_number)
            for row_number, row in enumerate(forest)
            for column_number, column in enumerate(row)
        ]

    def row_count(self):
        return max(self.trees, key=Tree.row)

    def column_count(self):
        return max(self.trees, key=Tree.column)

    def edge_rows(self):
        return [0, self.row_count]

    def edge_columns(self):
        return [0, self.column_count]

    def tree_neighbors(self, tree: Tree) -> List[Tree]:
        neighbor_addresses = [
            (tree.row() + i, tree.column() + j)
            for i in range(-1, 2, 2)
            for j in range(-1, 2, 2)
            if (tree.row() + i) >= 0 and (tree.column() + j) >= 0
        ]

        return [
            neighbor_tree
            for neighbor_tree in self.trees
            if (neighbor_tree.row(), neighbor_tree.column()) in neighbor_addresses
        ]

    def tree_is_visible(self, tree: Tree):
        if tree.row() in self.edge_rows or tree.column() in self.edge_columns:
            return True
        if tree.height() > min(self.tree_neighbors(tree), key=Tree.height):
            return False


def main():
    input_data = []
    with fileinput.input() as file:
        input_data = [line.rstrip("\n") for line in file]

    return


if __name__ == "__main__":
    print(main())
