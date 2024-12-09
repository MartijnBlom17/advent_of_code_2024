"""The solution for puzzle 1."""


def load_data() -> str:
    """Load the data."""
    with open("advent_of_code/day_9/puzzle_1/data.txt") as f:
        data = f.read()
    return data


def get_id_from_string(data: str) -> str:
    """Get the ID from the string."""
    block = 0
    new_data = ""
    for i in range(len(data)):
        if i % 2 == 0:
            new_data += str(block) * int(data[i])
            block += 1
        else:
            new_data += "." * int(data[i])
    return new_data


def move_blocks_to_left(data: str) -> str:
    """Move the blocks to the left."""
    i = 0
    while i < len(data):
        if data[i] == ".":
            while data[-1] == ".":
                data = data[:-1]
            # fmt: off
            data = data[:i] + data[-1] + data[i + 1:-1]
            # fmt: on
        i += 1
        if i >= len(data):
            break
    return data


def sum_blocks(data: str) -> int:
    """Sum the blocks."""
    return sum([int(block) * i for i, block in enumerate(data)])


def main():
    """The main function."""
    data = load_data()

    new_data = get_id_from_string(data)

    moved_data = move_blocks_to_left(new_data)

    return sum_blocks(moved_data)


if __name__ == "__main__":
    res = main()
    print(res)
