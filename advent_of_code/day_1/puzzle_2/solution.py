"""The solution for puzzle 2."""

from typing import List


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_1/puzzle_1/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str):
    """Process the data."""
    data_1, data_2 = [], []
    for line in data.split("\n"):
        part1, part2 = line.split("   ")
        data_1.append(int(part1))
        data_2.append(int(part2))
    return data_1, data_2


def check_multiply_frequency(list_1: List[int], list_2: List[int]):
    """Check the frequency in list 2 and multiply by the value of list 1."""
    multiple = 0
    for i in range(len(list_1)):
        frequency = list_2.count(list_1[i])
        multiple += list_1[i] * frequency
    return multiple


def main():
    """The main function."""
    data = load_data()

    list_1, list_2 = process_data(data)

    return check_multiply_frequency(list_1, list_2)


if __name__ == "__main__":
    res = main()
    print(res)
