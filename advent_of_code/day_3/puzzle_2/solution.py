"""The solution for puzzle 2."""

import re
from typing import List


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_3/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def preprocess_data(data: str) -> str:
    """Preprocess the data."""
    data = data.replace("\n", "")
    return data


def find_matches(data: str) -> List[str]:
    """Apply the regex to the data to find all matches."""
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
    res = re.findall(pattern, data)
    return res


def multiply_matches_with_do(matches: List[str]) -> int:
    """Multiply the digits of the matches."""
    res = 0
    do = True
    for match in matches:
        if match == "do()":
            do = True
        elif match == "don't()":
            do = False
        else:
            if do:
                nums = match.split("(")[1].split(")")[0].split(",")
                res += int(nums[0]) * int(nums[1])
    return res


def main():
    """The main function."""
    data = load_data()
    data = preprocess_data(data)

    matches = find_matches(data)

    return multiply_matches_with_do(matches)


if __name__ == "__main__":
    res = main()
    print(res)
