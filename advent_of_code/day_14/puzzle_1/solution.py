"""The solution for puzzle 1."""

from typing import List, Tuple

TIME = 100
SIZE_X = 101
SIZE_Y = 103


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_14/puzzle_1/data.txt") as f:
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


def determine_position(position: List[List[int]], velocity: List[List[int]]) -> List[List[int]]:
    """Determine the position after TIME."""
    final_positions = []
    for pos, vel in zip(position, velocity):
        new_pos = [pos[0] + vel[0] * TIME, pos[1] + vel[1] * TIME]
        final_positions.append([new_pos[0] % SIZE_X, new_pos[1] % SIZE_Y])
    return final_positions


def divide_and_multiply(final_positions: List[List[int]]) -> int:
    """Divide and multiply the final positions."""
    quad_1 = []
    quad_2 = []
    quad_3 = []
    quad_4 = []

    for pos in final_positions:
        if pos[0] <= SIZE_X // 2 - 1 and pos[1] <= SIZE_Y // 2 - 1:
            quad_1.append(pos)
        elif pos[0] <= SIZE_X // 2 - 1 and pos[1] > SIZE_Y // 2:
            quad_2.append(pos)
        elif pos[0] > SIZE_X // 2 and pos[1] <= SIZE_Y // 2 - 1:
            quad_3.append(pos)
        elif pos[0] > SIZE_X // 2 and pos[1] > SIZE_Y // 2:
            quad_4.append(pos)

    return len(quad_1) * len(quad_2) * len(quad_3) * len(quad_4)


def main():
    """The main function."""
    data = load_data()

    position, velocity = process_data(data)

    final_positions = determine_position(position, velocity)

    return divide_and_multiply(final_positions)


if __name__ == "__main__":
    res = main()
    print(res)
