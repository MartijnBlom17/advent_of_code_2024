"""The solution for puzzle 2."""

from typing import List


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_4/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def get_ver_data(data: List[str]) -> List[str]:
    """Get the vertical data."""
    data_ver = []
    for i in range(len(data[0])):
        data_ver.append("".join([data[j][i] for j in range(len(data))]))
    return data_ver


def get_diag_data_1(data: List[str]) -> List[str]:
    """Get the diagonal data."""
    data_diag: List = []
    for i in range(2 * len(data) - 1):
        data_diag.append([])

    for i in range(len(data)):
        for j in range(len(data)):
            data_diag[j + i].append("".join([data[j][i]]))

    # Merge the string in each list to a single string
    for i in range(len(data_diag)):
        data_diag[i] = "".join(data_diag[i])
    return data_diag


def get_diag_data_2(data: List[str]) -> List[str]:
    """Get the diagonal data."""
    reversed_data = [row[::-1] for row in data]
    data_diag = get_diag_data_1(reversed_data)
    return data_diag


def preprocess_data(data: str) -> List[str]:
    """Preprocess the data."""
    return data.split("\n")


def get_matches(data: List[str]) -> int:
    """Get the matches."""
    matches = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data) - 1):
            if data[i][j] == "A":
                if (
                    (data[i - 1][j - 1] == "M" and data[i + 1][j + 1] == "S")
                    or data[i - 1][j - 1] == "S"
                    and data[i + 1][j + 1] == "M"
                ):
                    if (
                        (data[i - 1][j + 1] == "S" and data[i + 1][j - 1] == "M")
                        or data[i - 1][j + 1] == "M"
                        and data[i + 1][j - 1] == "S"
                    ):
                        matches += 1
    return matches


def main():
    """The main function."""
    data = load_data()

    data_prep = preprocess_data(data)

    return get_matches(data_prep)


if __name__ == "__main__":
    res = main()
    print(res)
