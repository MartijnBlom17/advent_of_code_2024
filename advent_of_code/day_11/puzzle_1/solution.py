"""The solution for puzzle 1."""

from typing import List

BLINKS = 25


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_11/puzzle_1/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> List[int]:
    """Process the data."""
    result = data.split(" ")
    split_data = [int(char) for char in result if char.isdigit()]
    return split_data


def loop_over_data(data: List[int]) -> List[int]:
    """Loop over the data."""
    for _ in range(BLINKS):
        new_data = []
        for j in range(len(data)):
            if data[j] == 0:
                new_data.append(1)
            elif len(str(data[j])) % 2 == 0:
                new_data.append(int(str(data[j])[: len(str(data[j])) // 2]))
                new_data.append(int(str(data[j])[len(str(data[j])) // 2 :]))
            else:
                new_data.append(data[j] * 2024)
        data = new_data.copy()
    return data


def main():
    """The main function."""
    data = load_data()

    proc_data = process_data(data)

    result = loop_over_data(proc_data)

    return len(result)


if __name__ == "__main__":
    res = main()
    print(res)
