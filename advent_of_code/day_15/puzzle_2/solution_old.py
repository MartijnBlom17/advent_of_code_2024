"""The solution for puzzle 2."""

from typing import List, Tuple

import pandas as pd

MOVE_X = 1
MOVE_Y = 100


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_15/puzzle_2/test_data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> Tuple[List[List[int]], List[List[int]]]:
    """Process the data."""
    split_data = data.split("\n\n")

    movement = split_data[1].replace("\n", "")

    result = split_data[0].split("\n")
    grid = pd.DataFrame([list(line) for line in result if line])

    new_grid = increase_size(grid)

    return new_grid, movement
    

def increase_size(grid: pd.DataFrame) -> pd.DataFrame:
    """Increase the size of the grid."""
    all_cols = []
    for col in range(grid.shape[1]):
        col_1 = grid[col].copy()
        col_2 = grid[col].copy()
        for row in range(len(col_1)):
            if col_1[row] == "O":
                col_1[row] = "["
                col_2[row] = "]"
            elif col_1[row] == "@":
                col_1[row] = "@"
                col_2[row] = "."
        all_cols.append(col_1)
        all_cols.append(col_2)

    new_grid = pd.DataFrame(all_cols).T
    new_grid.columns = range(new_grid.shape[1])
    return new_grid


def move_on_grid(grid: pd.DataFrame, movement: str) -> None:
    """Move on the grid."""
    pos = grid.stack().eq("@").idxmax()
    print(grid)
    for move in movement:
        dir = move_dir(move)
        print("Move: ", move)
        if dir[1] != 0:
            print("Horizontally")
            grid, pos = move_horizontally(grid, pos, dir)
        else:
            grid, pos = move_vertically(grid, pos, dir)
        print(grid)

    return grid


def move_horizontally(grid: pd.DataFrame, pos: Tuple[int, int], dir: Tuple[int, int]) -> None:
    for i in range(1, max(grid.shape)):
        if grid.iloc[pos[0], pos[1] + dir[1] * i] == ".":
            move_x = sorted([pos[1] + dir[1] * i, pos[1] + dir[1]])

            grid.iloc[pos[0], move_x[0]:move_x[1] + 1] = grid.iloc[pos[0], move_x[0] - dir[1]:move_x[1] - dir[1] + 1].values
            grid.iloc[pos[0], pos[1]] = "."
            return grid, (pos[0] + dir[0], pos[1] + dir[1])

        elif grid.iloc[pos[0], pos[1] + dir[1] * i] == "#":
            return grid, pos


def move_vertically(grid: pd.DataFrame, pos: Tuple[int, int], dir: Tuple[int, int]) -> None:
    start_x = [[pos[1]]]
    for i in range(1, max(grid.shape)):
        range_x = [min(start_x[-1]), max(start_x[-1])]
        add = True
        if (grid.iloc[pos[0] + dir[0] * i, range_x[0]:range_x[1] + 1] == "#").any():
            return grid, pos
        elif all(grid.iloc[pos[0] + dir[0] * i, range_x[0]:range_x[1] + 1] == "."):
            if dir[0] == 1:
                start, end = pos[0] + dir[0] * i, pos[0]
            else:
                start, end = pos[0] + dir[0] * i, pos[0]
            for y in range(start, end, -dir[0]):
                x_range = min(start_x[-1]), max(start_x[-1])
                start_x.pop()

                grid.iloc[y, x_range[0]:x_range[1] + 1] = grid.iloc[y - dir[0], x_range[0]:x_range[1] + 1].values

                grid.iloc[y - dir[0], x_range[0]:x_range[1] + 1] = "."
            
            return grid, (pos[0] + dir[0], pos[1] + dir[1])
        
        if grid.iloc[pos[0] + dir[0] * i, range_x[0]] == "]":
            start_x.append(start_x[-1] + [range_x[0] - 1])
            add = False

        if grid.iloc[pos[0] + dir[0] * i, range_x[1]] == "[":
            start_x.append(start_x[-1] + [range_x[1] + 1])
            add = False
        
        if add:
            start_x.append(start_x[-1])


def move_dir(move: str) -> Tuple[int, int]:
    """Move in a direction."""
    if move == "^":
        return -1, 0
    elif move == "v":
        return 1, 0
    elif move == ">":
        return 0, 1
    elif move == "<":
        return 0, -1
    else:
        return 0, 0


def determine_distance(grid: pd.DataFrame) -> int:
    """Determine the distance."""
    all_pos = grid.stack().eq("[")
    coordinates = all_pos[all_pos].index.tolist()

    total = 0
    for coord in coordinates:
        total += coord[1] * MOVE_X + coord[0] * MOVE_Y
    return total


def main():
    """The main function."""
    data = load_data()

    grid, movement = process_data(data)

    grid = move_on_grid(grid, movement)
    return determine_distance(grid)


if __name__ == "__main__":
    res = main()
    print(res)
