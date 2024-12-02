"""The solution for puzzle 2."""

from typing import List


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_2/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def process_data(data: str) -> List[List[int]]:
    """Process the data."""
    data_list = []
    for line in data.split("\n"):
        line_list = [int(x) for x in line.split(" ")]
        data_list.append(line_list)
    return data_list


def subtract_and_check(single_list: List[int]) -> int:
    """Subtract each consecutive digit in the list and check the result."""
    check_sign = single_list[0] - single_list[1] > 0
    failed_check = False
    for i in range(len(single_list) - 1):
        if (single_list[i] - single_list[i + 1] > 0) != check_sign:
            failed_check = True
        if (abs(single_list[i] - single_list[i + 1]) < 1) or (abs(single_list[i] - single_list[i + 1]) > 3):
            failed_check = True
    if failed_check:
        for i in range(len(single_list)):
            minus_one_list = single_list.copy()
            minus_one_list.pop(i)
            check_passed = subtract_and_check_minus_one(minus_one_list)
            if check_passed:
                return True
    else:
        return True
    return False


def subtract_and_check_minus_one(my_list: List[int]) -> int:
    """Pop the failed check from the list and check the result again."""
    check_sign = my_list[0] - my_list[1] > 0
    for i in range(len(my_list) - 1):
        if (my_list[i] - my_list[i + 1] > 0) != check_sign:
            return False
        if (abs(my_list[i] - my_list[i + 1]) < 1) or (abs(my_list[i] - my_list[i + 1]) > 3):
            return False
    return True


def loop_over_list(data_list: List[List[int]]) -> int:
    """Loop over the list."""
    total = 0
    for line in data_list:
        total += subtract_and_check(line)
    return total


def main():
    """The main function."""
    data = load_data()

    data_list = process_data(data)

    total = loop_over_list(data_list)

    return total


if __name__ == "__main__":
    res = main()
    print(res)
