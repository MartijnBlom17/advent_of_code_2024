"""The solution for puzzle 2."""

from typing import List, Tuple

import pandas as pd

MOVE_X = 1
MOVE_Y = 100


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_15/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> Tuple[List[List[int]], List[List[int]]]:
    """Process the data."""
    split_data = data.split("\n\n")

    movement = split_data[1].replace("\n", "")

    result = split_data[0].split("\n")
    grid = pd.DataFrame([list(line) for line in result if line])

    new_grid = increase_size(grid)
    print(new_grid)

    hashtags = new_grid.stack().eq("#")
    hashtags = hashtags[hashtags].index.tolist()
    left_box = new_grid.stack().eq("[")
    left_box = left_box[left_box].index.tolist()
    right_box = new_grid.stack().eq("]")
    right_box = right_box[right_box].index.tolist()
    at_pos = new_grid.stack().eq("@").idxmax()

    return hashtags, left_box, right_box, at_pos, movement


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


def determine_distance(left_box: List[Tuple[int, int]]) -> int:
    """Determine the distance."""
    total = 0
    for coord in left_box:
        total += coord[1] * MOVE_X + coord[0] * MOVE_Y
    return total


def move_in_grid(hashtags: List[Tuple[int, int]], left_box: List[Tuple[int, int]], right_box: List[Tuple[int, int]], at_pos: Tuple[int, int], movement: str) -> None:
    """Move in the grid."""
    for move in movement:
        dir = move_dir(move)
        new_pos = (at_pos[0] + dir[0], at_pos[1] + dir[1])
        # print("Move: ", move)
        if new_pos in hashtags:
            continue
        elif new_pos in left_box or new_pos in right_box:
            left_box, right_box, at_pos = check_to_move_boxes(at_pos, dir, hashtags, left_box, right_box)
            
        else:
            at_pos = new_pos
    show_final_grid(hashtags, left_box, right_box, at_pos)
    
    return left_box


def check_to_move_boxes(at_pos: Tuple[int, int], dir: Tuple[int, int], hashtags: List[Tuple[int, int]], left_box: List[Tuple[int, int]], right_box: List[Tuple[int, int]]) -> None:
    """Check if it is possible to move the boxes."""
    potential_movers = []
    new_pos = (at_pos[0] + dir[0], at_pos[1] + dir[1])
    new_movers = [new_pos]
    if dir[1] == 0:
        if new_pos in left_box:
            new_movers.append((new_pos[0], new_pos[1] + 1))
        else:
            new_movers.append((new_pos[0], new_pos[1] - 1))
    while True:
        if any(item in new_movers for item in hashtags):
            return left_box, right_box, (new_pos[0] - dir[0], new_pos[1] - dir[1])
        elif not any(item in new_movers for item in left_box) and not any(item in new_movers for item in right_box):
            return move_items(list(set(potential_movers)), dir, left_box, right_box, new_pos)
        else:
            potential_movers.extend(new_movers)
            next_movers = []
            for move in new_movers:
                move_dir = (move[0] + dir[0], move[1] + dir[1])
                if move_dir in left_box:
                    next_movers.append(move_dir)
                    if dir[1] == 0:
                        next_movers.append((move[0] + dir[0], move[1] + dir[1] + 1))

                elif move_dir in right_box:
                    next_movers.append(move_dir)
                    if dir[1] == 0:
                        next_movers.append((move[0] + dir[0], move[1] + dir[1] - 1))
            if not next_movers:
                next_movers = [(nex_pos[0] + dir[0], nex_pos[1] + dir[1]) for nex_pos in new_movers]

            new_movers = list(set(next_movers))


def move_items(potential_movers: List[List[Tuple[int, int]]], dir: Tuple[int, int], left_box, right_box, at_pos) -> None:
    """Move the items."""
    new_moves = [(move[0] + dir[0], move[1] + dir[1]) for move in potential_movers]
    
    new_left_box = left_box.copy()
    new_right_box = right_box.copy()
    for old_pos, new_pos in zip(potential_movers, new_moves):
        if old_pos in left_box:
            new_left_box.remove(old_pos)
            new_left_box.append(new_pos)
        elif old_pos in right_box:
            new_right_box.remove(old_pos)
            new_right_box.append(new_pos) 
    return new_left_box, new_right_box, at_pos


def show_final_grid(hashtags, left_box, right_box, at_pos) -> None:
    """Show the final grid."""
    find_max_x = max([coord[1] for coord in hashtags])
    find_max_y = max([coord[0] for coord in hashtags])
    grid = pd.DataFrame([["." for _ in range(find_max_x + 1)] for _ in range(find_max_y + 1)])
    for coord in hashtags:
        grid.iloc[coord[0], coord[1]] = "#"
    for coord in left_box:
        grid.iloc[coord[0], coord[1]] = "["
    for coord in right_box:
        grid.iloc[coord[0], coord[1]] = "]"
    grid.iloc[at_pos[0], at_pos[1]] = "@"
    print(grid)
    with open("advent_of_code/day_15/puzzle_2/final_grid.txt", "w") as f:
        for row in grid.values:
            f.write("".join(row) + "\n")


def main():
    """The main function."""
    data = load_data()

    hashtags, left_box, right_box, at_pos, movement = process_data(data)
    
    left_box = move_in_grid(hashtags, left_box, right_box, at_pos, movement)

    return determine_distance(left_box)


if __name__ == "__main__":
    res = main()
    print(res)
