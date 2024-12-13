"""The solution for puzzle 2."""

from typing import List, Tuple

import pulp as pu

A = 3
B = 1
HIGHER = 10000000000000
HIGHER = 0


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_13/puzzle_2/test_data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]], List[Tuple[int, int]]]:
    """Process the data."""
    split_data = data.split("\n\n")

    a_list = []
    b_list = []
    result_list = []
    for i in range(len(split_data)):
        single_split = split_data[i].split("\n")
        # For the A list
        a_double_split = single_split[0].split("X+")
        a_triple_split = a_double_split[1].split(", Y+")
        a_list.append((int(a_triple_split[0]), int(a_triple_split[1])))

        # For the B list
        b_double_split = single_split[1].split("X+")
        b_triple_split = b_double_split[1].split(", Y+")
        b_list.append((int(b_triple_split[0]), int(b_triple_split[1])))

        # For the result list
        result1 = single_split[2].split("X=")
        result2 = result1[1].split(", Y=")
        result_list.append((int(result2[0]) + HIGHER, int(result2[1]) + HIGHER))

    return a_list, b_list, result_list


def find_all_solutions(
    a_list: List[Tuple[int, int]], b_list: List[Tuple[int, int]], result_list: List[Tuple[int, int]]
) -> int:
    """Find all the solutions."""
    result = 0
    for a, b, res in zip(a_list, b_list, result_list):
        result += pulp_model(a, b, res)
    return result


def pulp_model(a: Tuple[int, int], b: Tuple[int, int], result: Tuple[int, int]) -> int:
    """Create a pulp model."""
    model = pu.LpProblem("claw_machine", pu.LpMinimize)

    x = pu.LpVariable("x", 0, None, pu.LpInteger)
    y = pu.LpVariable("y", 0, None, pu.LpInteger)

    model += pu.lpSum([x * A, y * B])

    model += a[0] * x + b[0] * y == result[0]
    model += a[1] * x + b[1] * y == result[1]

    model.solve(pu.PULP_CBC_CMD(msg=False))

    if model.sol_status:
        return pu.value(model.objective)
    else:
        return 0


def main():
    """The main function."""
    data = load_data()

    a_data, b_data, result_data = process_data(data)

    return find_all_solutions(a_data, b_data, result_data)


if __name__ == "__main__":
    res = main()
    print(res)
