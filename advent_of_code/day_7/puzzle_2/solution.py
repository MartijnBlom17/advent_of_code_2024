"""The solution for puzzle 2."""

from typing import List, Tuple


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_7/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def preprocess_data(data: str) -> Tuple[List[int], List[List[int]]]:
    """Preprocess the data."""
    rows = data.strip().split("\n")
    result, values = zip(*(row.split(":") for row in rows))
    values2 = [[int(val) for val in line.split(" ") if val != ""] for line in values]
    result2 = [int(res) for res in result]
    return result2, values2


def create_total(values: List[int], choice: str) -> int:
    """Create the total based on the choice."""
    total = values[0]
    for i in range(len(choice)):
        if choice[i] == "0":
            total += values[i + 1]
        elif choice[i] == "1":
            total = int(str(total) + str(values[i + 1]))
        else:
            total *= values[i + 1]
    return total


def to_ternary(n: int) -> str:
    """Convert to ternary (binary with 3 possible digits per outcome)."""
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(str(n % 3))
        n //= 3
    return "".join(digits[::-1])


def determine_if_valid(result: List[int], values: List[List[int]]) -> int:
    """Determine if the result is valid."""
    total = 0
    for i in range(len(result)):
        options = 3 ** (len(values[i]) - 1)
        for j in range(options):
            choice = to_ternary(j).zfill(len(values[i]) - 1)
            created_total = create_total(values[i], choice)
            if created_total == result[i]:
                total += result[i]
                break
    return total


def main():
    """The main function."""
    data = load_data()

    result, values = preprocess_data(data)

    return determine_if_valid(result, values)


if __name__ == "__main__":
    res = main()
    print(res)
