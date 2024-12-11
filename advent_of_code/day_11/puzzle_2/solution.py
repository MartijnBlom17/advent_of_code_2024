"""The solution for puzzle 2."""

from typing import List, Tuple

BLINKS = 75


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_11/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> List[int]:
    """Process the data."""
    result = data.split(" ")
    split_data = [int(char) for char in result if char.isdigit()]
    return split_data


def loop_over_data(data: List[int]) -> int:
    """Loop over the data."""
    count = [1] * len(data)
    for i in range(BLINKS):
        print("Blink:", i, "Length:", len(data))
        new_data, new_count = get_count_data(data, count)
        data, count = count_and_set_data(new_data, new_count)
    return sum(count)


def get_count_data(data: List[int], count: List[int]) -> Tuple[List[int], List[int]]:
    new_data = []
    new_count = []
    for j, c in zip(data, count):
        if j == 0:
            new_data.append(1)
            new_count.append(c)
        elif len(str(j)) % 2 == 0:
            half_len = len(str(j)) // 2
            new_data.append(int(str(j)[:half_len]))
            new_data.append(int(str(j)[half_len:]))
            new_count.append(c)
            new_count.append(c)
        else:
            new_data.append(j * 2024)
            new_count.append(c)
    return new_data, new_count


def count_and_set_data(data: List[int], count: List[int]) -> Tuple[List[int], List[int]]:
    """Count the frequency of the data and create unique data."""
    count_set = []
    data_set = list(set(data))
    for val in data_set:
        indexes = [index for index, value in enumerate(data) if value == val]
        count_set.append(sum(count[index] for index in indexes))
    return data_set, count_set


def main():
    """The main function."""
    data = load_data()

    proc_data = process_data(data)

    return loop_over_data(proc_data)


if __name__ == "__main__":
    res = main()
    print(res)
