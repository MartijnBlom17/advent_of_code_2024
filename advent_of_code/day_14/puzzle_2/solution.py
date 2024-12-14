"""The solution for puzzle 2."""

from typing import List, Tuple

import numpy as np

SIZE_X = 101
SIZE_Y = 103


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_14/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> Tuple[List[List[int]], List[List[int]]]:
    """Process the data."""
    split_data = data.split("\n")

    position = []
    velocity = []
    for line in split_data:
        position_data, velocity_data = line.split(" ")

        pos = position_data.split("=")[1].split(",")
        vel = velocity_data.split("=")[1].split(",")

        position.append([int(posi) for posi in pos])
        velocity.append([int(veli) for veli in vel])

    return position, velocity


def determine_position(position: List[List[int]], velocity: List[List[int]]) -> int:
    """Determine the position after TIME."""
    condition = True
    seconds = 0

    while condition:
        seconds += 1
        grid = np.full((SIZE_X, SIZE_Y), ".")
        for pos, vel in zip(position, velocity):
            new_pos = [pos[0] + vel[0] * seconds, pos[1] + vel[1] * seconds]
            act_pos = [new_pos[0] % SIZE_X, new_pos[1] % SIZE_Y]
            grid[act_pos[0], act_pos[1]] = "#"

        if determine_max_area(grid) > 50:
            grid_str = "\n".join("".join(row) for row in grid)
            print(grid_str)
            break
        if seconds == 10000:
            break

    return seconds


def determine_max_area(grid: np.ndarray) -> int:
    """Determine the max area."""
    max_area = 0
    seen: set = set()
    for i in range(SIZE_X):
        for j in range(SIZE_Y):
            if grid[i, j] == "#" and (i, j) not in seen:
                area, seen = determine_area(grid, seen, i, j)
                if area > max_area:
                    max_area = area
    return max_area


def determine_area(grid: np.ndarray, seen: set, i: int, j: int) -> Tuple[int, set]:
    """Determine the area."""
    area = 0
    cur_area = [(i, j)]
    seen.add((i, j))
    while cur_area:
        x, y = cur_area.pop()
        area += 1
        cur_area, seen = determine_total_area(grid, cur_area, seen, x, y)

    return area, seen


def determine_total_area(grid: np.ndarray, cur_area: List, seen: set, x: int, y: int) -> Tuple[List, set]:
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x = x + dx
        new_y = y + dy
        if new_x >= 0 and new_x < SIZE_X and new_y >= 0 and new_y < SIZE_Y:
            if (new_x, new_y) not in seen and grid[new_x, new_y] == "#":
                seen.add((new_x, new_y))
                cur_area.append((new_x, new_y))
    return cur_area, seen


def main():
    """The main function."""
    data = load_data()

    position, velocity = process_data(data)

    return determine_position(position, velocity)


if __name__ == "__main__":
    res = main()
    print(res)
