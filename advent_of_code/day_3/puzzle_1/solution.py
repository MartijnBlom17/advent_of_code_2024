"""The solution for puzzle 1."""

import re
from typing import List


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_3/puzzle_1/data.txt") as f:
        data = f.read()
    return data


def preprocess_data(data: str) -> str:
    """Preprocess the data."""
    data = data.replace("\n", "")
    return data


def find_matches(data: str) -> List[str]:
    """Apply the regex to the data to find all matches."""
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    res = re.findall(pattern, data)
    return res


def multiply_matches(matches: List[str]) -> int:
    """Multiply the digits of the matches."""
    res = 0
    for match in matches:
        nums = match.split("(")[1].split(")")[0].split(",")
        res += int(nums[0]) * int(nums[1])
    return res


def main():
    """The main function."""
    data = load_data()
    data = preprocess_data(data)

    matches = find_matches(data)

    return multiply_matches(matches)


if __name__ == "__main__":
    res = main()
    print(res)
