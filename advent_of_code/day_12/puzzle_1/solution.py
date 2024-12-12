"""The solution for puzzle 1."""

from typing import List, Tuple

import numpy as np


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_12/puzzle_1/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> np.array:
    """Process the data."""
    split_data = [list(line) for line in data.split("\n")]
    split_data = np.array(split_data)
    return split_data


def _find_all_neighbours(
    grid: np.array, digit: str, x: int, y: int, garden: List[Tuple[int, int]], already_seen: List[Tuple[int, int]]
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """Find all the neighbours of a given cell."""
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy

        if (
            0 <= new_x < grid.shape[0]
            and 0 <= new_y < grid.shape[1]
            and (new_x, new_y) not in already_seen
            and grid[new_x][new_y] == digit
        ):
            garden.append((new_x, new_y))
            already_seen.append((new_x, new_y))
    return garden, already_seen


def _find_neighbours(
    grid: np.array, i: int, j: int, already_seen
) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
    """Find the neighbours of a given cell."""
    already_seen.append((i, j))
    all_garden: List = []
    garden = [(i, j)]
    digit = grid[i][j]

    while garden:
        all_garden.extend(garden)
        x, y = garden.pop()

        garden, already_seen = _find_all_neighbours(grid, digit, x, y, garden, already_seen)

    all_garden = list(set(all_garden))

    return all_garden, already_seen


def loop_over_data(data: np.array) -> List[List[Tuple[int, int]]]:
    """Loop over the data."""
    already_seen: List = []
    gardens: List = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if (i, j) not in already_seen:
                garden, already_seen = _find_neighbours(data, i, j, already_seen)
                gardens.append(garden)
    return gardens


def create_total(gardens: List[List[Tuple[int, int]]]) -> int:
    """Create the total."""
    total = 0
    for garden in gardens:
        area = len(garden)
        perimeter = 0
        for x, y in garden:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if (new_x, new_y) not in garden:
                    perimeter += 1
        total += area * perimeter
    return total


def main():
    """The main function."""
    data = load_data()

    proc_data = process_data(data)

    gardens = loop_over_data(proc_data)

    return create_total(gardens)


if __name__ == "__main__":
    res = main()
    print(res)
