"""The solution for puzzle 2."""

from typing import List, Optional, Tuple

import numpy as np
import pandas as pd


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_8/puzzle_2/data.txt") as f:
        data = f.read()
    return data


def preprocess_data(data: str) -> Tuple[pd.DataFrame, List[str]]:
    """Preprocess the data."""
    unique_values = set(data) - {"."} - {"\n"}
    result = data.split("\n")
    df = pd.DataFrame([list(line) for line in result if line])
    return df, list(unique_values)


def add_node(df: pd.DataFrame, anti_node: Tuple[int, int]) -> Optional[Tuple[int, int]]:
    if anti_node[0] >= 0 and anti_node[0] < df.shape[0] and anti_node[1] >= 0 and anti_node[1] < df.shape[1]:
        return anti_node
    return None


def determine_all_potential_antinodes(df, locations_coor, i, j):
    """Determine all potential antinodes."""
    x_dist = locations_coor[i][0] - locations_coor[j][0]
    y_dist = locations_coor[i][1] - locations_coor[j][1]

    anti_nodes_1 = [locations_coor[i]]
    anti_nodes_2 = [locations_coor[j]]
    max_dist = df.shape[0] + df.shape[1]
    max_nodes = max(abs(np.ceil(max_dist / x_dist)), abs(np.ceil(max_dist / y_dist)))

    for x in range(int(max_nodes)):
        anti_nodes_1.append((locations_coor[i][0] + (x_dist * (x + 1)), locations_coor[i][1] + (y_dist * (x + 1))))
        anti_nodes_2.append((locations_coor[j][0] - (x_dist * (x + 1)), locations_coor[j][1] - (y_dist * (x + 1))))
    return anti_nodes_1, anti_nodes_2


def antinode_locs(
    df: pd.DataFrame, all_antinodes: List[Tuple[int, int]], locations_coor: List[Tuple[int, int]], i: int, j: int
) -> List[Tuple[int, int]]:
    """Find the antinodes."""
    anti_nodes_1, anti_nodes_2 = determine_all_potential_antinodes(df, locations_coor, i, j)

    for anti_node1 in anti_nodes_1:
        node1 = add_node(df, anti_node1)
        if node1 is not None:
            all_antinodes.append(node1)
    for anti_node2 in anti_nodes_2:
        node2 = add_node(df, anti_node2)
        if node2 is not None:
            all_antinodes.append(node2)
    return all_antinodes


def check_antinodes(df: pd.DataFrame, values: List[str]) -> List[Tuple[int, int]]:
    """Check the antinodes."""
    all_antinodes: List = []
    for value in values:
        # Find all locations of the value in the dataframe
        locations = df.apply(lambda x: x == value)
        # Get the column names and row number of the locations
        locations_coor = locations.stack()[locations.stack()].index.tolist()

        for i in range(len(locations_coor) - 1):
            for j in range(i + 1, len(locations_coor)):
                all_antinodes = antinode_locs(df, all_antinodes, locations_coor, i, j)

    return all_antinodes


def unique_nodes(all_nodes: List) -> int:
    """Find the unique nodes."""
    return len({node for node in all_nodes if node is not None})


def main():
    """The main function."""
    data = load_data()

    df, values = preprocess_data(data)

    all_nodes = check_antinodes(df, values)

    return unique_nodes(all_nodes)


if __name__ == "__main__":
    res = main()
    print(res)
