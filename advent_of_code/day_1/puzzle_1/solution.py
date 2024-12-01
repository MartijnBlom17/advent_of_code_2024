"""The solution for puzzle 1."""

from typing import List


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_1/puzzle_1/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str):
    """Process the data."""
    data_1 = []
    data_2 = []
    for line in data.split("\n"):
        part1, part2 = line.split("   ")
        data_1.append(int(part1))
        data_2.append(int(part2))
    return data_1, data_2


def sort_data(data_list: List[int]):
    """Sort the data."""
    return sorted(data_list)


def subtract_data(list_1: List[int], list_2: List[int]):
    """Subtract the data."""
    difference = 0
    for i in range(len(list_1)):
        difference += abs(list_1[i] - list_2[i])
    return difference


def main():
    """The main function."""
    data = load_data()

    list_1, list_2 = process_data(data)

    list_1 = sort_data(list_1)
    list_2 = sort_data(list_2)

    return subtract_data(list_1, list_2)


if __name__ == "__main__":
    res = main()
    print(res)
