"""The solution for puzzle 1."""

from typing import List

import pandas as pd


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_10/puzzle_1/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> pd.DataFrame:
    """Process the data."""
    result = data.split("\n")
    df = pd.DataFrame([[int(char) for char in line if char.isdigit()] for line in result if line])
    return df


def loop_over_data(data: pd.DataFrame) -> List[int]:
    """Loop over the data."""
    mountain_tops = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data.iloc[i, j] == 0:
                mountain_tops.append(search_mountain_top(data, i, j))
    return mountain_tops


def search_mountain_top(data: pd.DataFrame, i: int, j: int) -> int:
    """Search the mountain top."""
    values_list = [(i, j)]
    for k in range(1, 10):
        values_list = search_digit_in_neighbours(data, k, values_list)

        if not values_list:
            return 0
    return len(set(values_list))


def search_digit_in_neighbours(data: pd.DataFrame, k: int, values_list: List) -> List:
    """Search for a digit in the neighbours."""
    new_list = []
    for val in values_list:
        if val[0] - 1 >= 0 and data.iloc[val[0] - 1, val[1]] == k:
            new_list.append((val[0] - 1, val[1]))
        if val[0] + 1 < data.shape[0] and data.iloc[val[0] + 1, val[1]] == k:
            new_list.append((val[0] + 1, val[1]))
        if val[1] - 1 >= 0 and data.iloc[val[0], val[1] - 1] == k:
            new_list.append((val[0], val[1] - 1))
        if val[1] + 1 < data.shape[1] and data.iloc[val[0], val[1] + 1] == k:
            new_list.append((val[0], val[1] + 1))
    return list(set(new_list))


def main():
    """The main function."""
    data = load_data()

    proc_data = process_data(data)

    mountain_tops = loop_over_data(proc_data)

    return sum(mountain_tops)


if __name__ == "__main__":
    res = main()
    print(res)
