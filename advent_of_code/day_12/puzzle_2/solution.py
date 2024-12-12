"""The solution for puzzle 2."""

from typing import List, Tuple

import numpy as np


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_12/puzzle_2/data.txt") as f:
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
    all_garden = []
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
        sides = find_sides(garden)
        unique_sides = divide_sides(sides)
        total += area * unique_sides

    return total


def find_sides(garden: List[Tuple[int, int]]) -> List[Tuple[int, int, int]]:
    """Find the sides of the garden."""

    sides = []
    for x, y in garden:
        for i, (dx, dy) in enumerate([(0, 1), (1, 0), (0, -1), (-1, 0)]):
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) not in garden:
                sides.append((x, y, i))
    return sides


def divide_sides(sides: List[Tuple[int, int, int]]) -> int:
    """Divide the sides."""
    sides.sort(key=lambda x: (x[0], x[1]))
    divided_sides: List = []
    for side in sides:
        if divided_sides:
            added = False
            for i, divided_side in enumerate(divided_sides):
                for j, single_side in enumerate(divided_side):
                    if side[2] == single_side[2]:
                        if (side[0] == single_side[0] - 1 or side[0] == single_side[0] + 1) and side[1] == single_side[
                            1
                        ]:
                            divided_sides[i].append(side)
                            added = True
                            break
                        if (side[1] == single_side[1] - 1 or side[1] == single_side[1] + 1) and side[0] == single_side[
                            0
                        ]:
                            divided_sides[i].append(side)
                            added = True
                            break
            if not added:
                divided_sides.append([side])

        else:
            divided_sides.append([side])
    return len(divided_sides)


def main():
    """The main function."""
    data = load_data()

    proc_data = process_data(data)

    gardens = loop_over_data(proc_data)

    return create_total(gardens)


if __name__ == "__main__":
    res = main()
    print(res)
