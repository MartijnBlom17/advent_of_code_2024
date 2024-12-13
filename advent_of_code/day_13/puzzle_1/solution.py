"""The solution for puzzle 1."""

from typing import List, Tuple

A = 3
B = 1


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_13/puzzle_1/data.txt") as f:
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
        result_list.append((int(result2[0]), int(result2[1])))

    return a_list, b_list, result_list


def find_all_solutions(
    a_list: List[Tuple[int, int]], b_list: List[Tuple[int, int]], result_list: List[Tuple[int, int]]
) -> List[List[Tuple[int, int]]]:
    """Find all the solutions."""
    all_solutions = []
    for a, b, res in zip(a_list, b_list, result_list):
        max_a = min(res[0] // a[0], res[1] // a[1], 100)
        max_b = min(res[0] // b[0], res[1] // b[1], 100)
        solutions = []
        for i in range(max_a):
            for j in range(max_b):
                if a[0] * i + b[0] * j == res[0] and a[1] * i + b[1] * j == res[1]:
                    solutions.append((i, j))
        all_solutions.append(solutions)
    return all_solutions


def find_best_solution(all_solutions: List[List[Tuple[int, int]]]) -> int:
    """Find the best solution."""
    best_solution = 0
    for solution in all_solutions:
        best = 0
        for sol in solution:
            if best == 0:
                best = sol[0] * A + sol[1] * B
            elif sol[0] * A + sol[1] * B < best:
                best = sol[0] * A + sol[1] * B
        best_solution += best
    return best_solution


def main():
    """The main function."""
    data = load_data()

    a_data, b_data, result_data = process_data(data)

    all_solutions = find_all_solutions(a_data, b_data, result_data)

    return find_best_solution(all_solutions)


if __name__ == "__main__":
    res = main()
    print(res)
