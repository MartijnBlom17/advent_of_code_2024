"""The solution for puzzle 1."""

from typing import List, Tuple

import polars as pl


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_5/puzzle_1/data.txt") as f:
        data = f.read()
    return data


def preprocess_data(data: str) -> Tuple[pl.DataFrame, List[List[int]]]:
    """Preprocess the data."""
    split_data: List = data.split("\n\n")
    page_rules_str: str = split_data[0]
    page_ordering_str: str = split_data[1]

    # Create a DataFrame for the page rules
    page_rules_list: List = page_rules_str.split("\n")
    page_rules = pl.DataFrame([rule.split("|") for rule in page_rules_list], schema=["first", "after"])
    page_rules = page_rules.with_columns([pl.col("first").cast(pl.Int32), pl.col("after").cast(pl.Int32)])

    # Create a list lists for the page ordering
    page_ordering_list: List = page_ordering_str.split("\n")
    page_ordering = [[int(unit) for unit in page.split(",")] for page in page_ordering_list]

    return page_rules, page_ordering


def check_wrong_ordering(filtered_rules: pl.DataFrame, page: List[int], i: int) -> bool:
    """Check if the ordering is wrong."""

    for j in range(i, len(page)):
        if page[j] in filtered_rules["first"]:
            return True
    return False


def check_page_ordering(page_rules: pl.DataFrame, page_ordering: List[List[int]]) -> List[List[int]]:
    """Check the page ordering."""
    correct_ordering = []
    for page in page_ordering:
        wrong_order = False
        for i in range(len(page) - 1):
            filtered_rules = page_rules.filter(pl.col("after") == page[i])
            if check_wrong_ordering(filtered_rules, page, i):
                wrong_order = True
                break
        if not wrong_order:
            correct_ordering.append(page)
    return correct_ordering


def count_middle_pages(correct_ordering: List[List[int]]) -> int:
    """Count the middle pages."""
    count = 0
    for page in correct_ordering:
        count += page[len(page) // 2]
    return count


def main():
    """The main function."""
    data = load_data()

    page_rules, page_ordering = preprocess_data(data)

    correct_ordering = check_page_ordering(page_rules, page_ordering)

    return count_middle_pages(correct_ordering)


if __name__ == "__main__":
    res = main()
    print(res)
