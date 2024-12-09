"""The solution for puzzle 2."""

from typing import List, Tuple


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_9/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def get_id_from_string(data: str) -> Tuple[List[str], List[Tuple[int, int]], List[Tuple[int, int]]]:
    """Get the ID from the string."""
    block = 0
    new_data: List = []
    loc_nums: List = []
    loc_dots: List = []
    for i in range(len(data)):
        if i % 2 == 0:
            loc_nums.append((int(data[i]), len(new_data)))
            for _ in range(int(data[i])):
                new_data.append(str(block))
            block += 1
        else:
            loc_dots.append((int(data[i]), len(new_data)))
            for _ in range(int(data[i])):
                new_data.append(".")
    return new_data, loc_nums, loc_dots


def move_blocks_to_left(data: List[str], loc_nums: List[Tuple[int, int]], loc_dots: List[Tuple[int, int]]) -> List[str]:
    """Move the blocks to the left."""
    was_moved = True
    while was_moved:
        was_moved = False
        for i in range(len(loc_nums) - 1, -1, -1):
            for j in range(len(loc_dots)):
                if loc_nums[i][0] <= loc_dots[j][0]:
                    if loc_nums[i][1] > loc_dots[j][1]:
                        for k in range(loc_nums[i][0]):
                            data[loc_dots[j][1] + k] = data[loc_nums[i][1] + k]
                            data[loc_nums[i][1] + k] = "."
                        loc_nums[i] = (loc_nums[i][0], loc_dots[j][1])
                        loc_dots[j] = (loc_dots[j][0] - loc_nums[i][0], loc_dots[j][1] + loc_nums[i][0])
                        if loc_dots[j][0] == 0:
                            loc_dots.pop(j)
                        was_moved = True
                        break
    return data


def sum_blocks(data: str) -> int:
    """Sum the blocks."""
    return sum([int(block) * i for i, block in enumerate(data) if block != "."])


def main():
    """The main function."""
    data = load_data()

    new_data, loc_nums, loc_dots = get_id_from_string(data)

    moved_data = move_blocks_to_left(new_data, loc_nums, loc_dots)

    return sum_blocks(moved_data)


if __name__ == "__main__":
    res = main()
    print(res)
