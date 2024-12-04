"""The solution for puzzle 2."""

from typing import List, Tuple


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_4/puzzle_1/data.txt") as f:
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


def preprocess_data(data: str) -> Tuple[List[str], List[str], List[str], List[str]]:
    """Preprocess the data."""
    # Horizontal data set
    data_hor = data.split("\n")
    # Vertical data set
    data_ver = get_ver_data(data_hor)
    # Get the left to right diagonal data set
    data_diag1 = get_diag_data_1(data_hor)
    # Get the right to left diagonal data set
    data_diag2 = get_diag_data_2(data_hor)
    return data_hor, data_ver, data_diag1, data_diag2


def get_matches(data: List[str]) -> int:
    """Get the matches."""
    matches = 0
    for row in data:
        for i in range(len(row) - 3):
            # fmt: off
            if row[i:i + 4] in ["XMAS", "SAMX"]:
                # fmt: on
                matches += 1
    return matches


def main():
    """The main function."""
    data = load_data()

    dat_hor, dat_ver, data_diag1, data_diag2 = preprocess_data(data)

    hor_matches = get_matches(dat_hor)
    ver_matches = get_matches(dat_ver)
    diag1_matches = get_matches(data_diag1)
    diag2_matches = get_matches(data_diag2)

    return hor_matches + ver_matches + diag1_matches + diag2_matches


if __name__ == "__main__":
    res = main()
    print(res)
