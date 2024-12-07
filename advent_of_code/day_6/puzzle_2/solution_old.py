"""The solution for puzzle 2."""

from typing import List, Tuple

import polars as pl


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_6/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def preprocess_data(data: str) -> Tuple[pl.DataFrame, int, int, str]:
    """Preprocess the data."""
    # Create a DataFrame for the guard map
    row_data_list: List = data.split("\n")
    df = pl.DataFrame([list(rule) for rule in row_data_list], schema=[str(i) for i in range(len(row_data_list[0]))])

    # Determine the starting position and direction
    positions = [(i, j) for i, row in enumerate(df.rows()) for j, val in enumerate(row) if val == "^"]
    dir = "up"

    return df, positions[0][0], positions[0][1], dir


def determine_path(df: pl.DataFrame, pos_y: int, pos_x: int, dir: str) -> List[Tuple[int, int]]:
    all_locs = [(pos_x, pos_y, dir)]
    viable_objects = []
    while pos_x >= 0 and pos_x < len(df.columns) and pos_y >= 0 and pos_y < len(df.rows()):
        move_x, move_y = determine_direction(dir)
        pos_x += move_x
        pos_y += move_y
        if pos_x < 0 or pos_x >= len(df.columns) or pos_y < 0 or pos_y >= len(df.rows()):
            break
        if df[str(pos_y)][pos_x] == "#":
            dir = change_dir(dir)
            pos_x -= move_x
            pos_y -= move_y
        else:
            all_locs.append((pos_x, pos_y, dir))

        # Check if we place an object in front, if it will go onto a path that was already visited
        if not (pos_x + move_x, pos_y + move_y) == all_locs[0][0:2]:  # in [(x, y) for x, y, _ in all_locs]:
            if determine_place_object(df, all_locs, pos_x, pos_y, dir):
                viable_objects.append((pos_x + move_x, pos_y + move_y))
                print(pos_x + move_x, pos_y + move_y)
    return viable_objects


def determine_direction(dir: str) -> Tuple[int, int]:
    if dir == "up":
        return 0, -1
    elif dir == "down":
        return 0, 1
    elif dir == "left":
        return -1, 0
    return 1, 0


def change_dir(dir: str) -> str:
    """Change the direction."""
    if dir == "up":
        return "right"
    elif dir == "right":
        return "down"
    elif dir == "down":
        return "left"
    return "up"


def determine_place_object(
    df: pl.DataFrame, all_locs: List[Tuple[int, int, str]], pos_x: int, pos_y: int, dir: str
) -> bool:
    """Determine if we can place an object in front."""
    dir2 = change_dir(dir)
    while pos_x >= 0 and pos_x < len(df.columns) and pos_y >= 0 and pos_y < len(df.rows()):
        move_x, move_y = determine_direction(dir2)
        pos_x += move_x
        pos_y += move_y
        if pos_x < 0 or pos_x >= len(df.columns) or pos_y < 0 or pos_y >= len(df.rows()):
            return False
        if df[str(pos_y)][pos_x] == "#":
            dir2 = change_dir(dir2)
            pos_x -= move_x
            pos_y -= move_y

        if (pos_x, pos_y, dir2) in all_locs:
            return True
    return False


def count_distinct_places(all_locs: List[Tuple[int, int]]) -> int:
    """Count the distinct places."""
    return len(list(set(all_locs)))


def main():
    """The main function."""
    data = load_data()

    df, pos_x, pos_y, dir = preprocess_data(data)

    all_locs = determine_path(df, pos_y, pos_x, dir)

    return count_distinct_places(all_locs)


if __name__ == "__main__":
    res = main()
    print(res)
