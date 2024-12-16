"""The solution for puzzle 1."""

from typing import List, Tuple

import pandas as pd

MOVE_X = 1
MOVE_Y = 100


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_15/puzzle_1/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> Tuple[List[List[int]], List[List[int]]]:
    """Process the data."""
    split_data = data.split("\n\n")

    movement = split_data[1].replace("\n", "")

    result = split_data[0].split("\n")
    grid = pd.DataFrame([list(line) for line in result if line])

    return grid, movement


def move_on_grid(grid: pd.DataFrame, movement: str) -> None:
    """Move on the grid."""
    pos = grid.stack().eq("@").idxmax()
    for move in movement:
        dir = move_dir(move)
        can_move, dist = check_if_move_possible(grid, pos, dir)
        if can_move:
            grid.iloc[pos[0], pos[1]] = "."
            grid = move_boxes(grid, pos, dir, dist)
            pos = (pos[0] + dir[0], pos[1] + dir[1])
            grid.iloc[pos[0], pos[1]] = "@"
    return grid


def check_if_move_possible(grid: pd.DataFrame, pos: Tuple[int, int], dir: Tuple[int, int]) -> Tuple[bool, int]:
    """Check if the move is possible."""
    pos_wall = find_next_wall(grid, pos, dir)
    
    order_x = sorted([pos[0], pos_wall[0]])
    order_y = sorted([pos[1], pos_wall[1]])
    dist = max(abs(pos[0] - pos_wall[0]), abs(pos[1] - pos_wall[1]))

    df = grid.iloc[order_x[0]:order_x[1] + 1, order_y[0]:order_y[1] + 1] == "."
    return df.values.any(), dist


def find_next_wall(grid: pd.DataFrame, pos: Tuple[int, int], dir: Tuple[int, int]) -> Tuple[int, int]:
    """Find the next wall."""
    for i in range(1, max(grid.shape)):
        if grid.iloc[pos[0] + dir[0] * i, pos[1] + dir[1] * i] == "#":
            return pos[0] + dir[0] * i, pos[1] + dir[1] * i


def move_boxes(grid: pd.DataFrame, pos: Tuple[int, int], dir: Tuple[int, int], dist: int) -> pd.DataFrame:
    """Move the boxes."""
    # Return the normal grid if there is no box in front
    if grid.iloc[pos[0] + dir[0], pos[1] + dir[1]] == ".":
        return grid

    # Loop over the walking path and move the boxes until it reaches the wall or empty space
    for i in range(1, dist):
        if grid.iloc[pos[0] + dir[0] * i, pos[1] + dir[1] * i] == ".":
            grid.iloc[pos[0] + dir[0] * i, pos[1] + dir[1] * i] = "O"
            break
        elif grid.iloc[pos[0] + dir[0] * i, pos[1] + dir[1] * i] == "#":
            break
        else:
            grid.iloc[pos[0] + dir[0] * i, pos[1] + dir[1] * i] = "O"
    return grid


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
    all_pos = grid.stack().eq("O")
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
