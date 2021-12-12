import numpy as np

from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=1656,
    example_2=195,
    input_parse_line=lambda i: [int(c) for c in i],
    input_parse_overall=lambda i: i
)


# Puzzle 1
def puzzle_1(p_input: list):
    flashes: list = []

    num_rows, num_cols = len(p_input), len(p_input[0])

    def find_adjacent(row: int, col: int) -> list:
        adj: list = []
        if row > 0:
            adj.append((row-1, col))
        if row < num_rows - 1:
            adj.append((row+1, col))
        if col > 0:
            adj.append((row, col-1))
        if col < num_cols - 1:
            adj.append((row, col+1))
        if row > 0 and col > 0:
            adj.append((row-1, col-1))
        if row > 0 and col < num_cols - 1:
            adj.append((row-1, col+1))
        if row < num_rows - 1 and col > 0:
            adj.append((row+1, col-1))
        if row < num_rows - 1 and col < num_cols - 1:
            adj.append((row+1, col+1))
        return adj

    np_input: np.ndarray = np.array(p_input)

    for _ in range(100):
        flashes.append([])
        np_input += 1

        while (np_input > 9).any():
            to_flash: list = [x for x in np.argwhere(np_input > 9).tolist() if x not in flashes[-1]]
            if not to_flash:
                break
            for loc in to_flash:
                np_input[loc[0]][loc[1]] += 1
                flashes[-1].append(loc)
                adjacent: list = find_adjacent(*loc)
                for pt in adjacent:
                    np_input[pt[0]][pt[1]] += 1

        for loc in flashes[-1]:
            np_input[loc[0]][loc[1]] = 0

    return sum([len(i) for i in flashes])


# Puzzle 2
def puzzle_2(p_input: list):
    flashes: list = []

    num_rows, num_cols = len(p_input), len(p_input[0])

    def find_adjacent(row: int, col: int) -> list:
        adj: list = []
        if row > 0:
            adj.append((row - 1, col))
        if row < num_rows - 1:
            adj.append((row + 1, col))
        if col > 0:
            adj.append((row, col - 1))
        if col < num_cols - 1:
            adj.append((row, col + 1))
        if row > 0 and col > 0:
            adj.append((row - 1, col - 1))
        if row > 0 and col < num_cols - 1:
            adj.append((row - 1, col + 1))
        if row < num_rows - 1 and col > 0:
            adj.append((row + 1, col - 1))
        if row < num_rows - 1 and col < num_cols - 1:
            adj.append((row + 1, col + 1))
        return adj

    np_input: np.ndarray = np.array(p_input)

    for i in range(1000000):
        flashes.append([])
        np_input += 1

        while (np_input > 9).any():
            to_flash: list = [x for x in np.argwhere(np_input > 9).tolist() if x not in flashes[-1]]
            if not to_flash:
                break
            for loc in to_flash:
                np_input[loc[0]][loc[1]] += 1
                flashes[-1].append(loc)
                adjacent: list = find_adjacent(*loc)
                for pt in adjacent:
                    np_input[pt[0]][pt[1]] += 1

        if len(flashes[-1]) == num_rows*num_cols:
            return i+1

        for loc in flashes[-1]:
            np_input[loc[0]][loc[1]] = 0


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
