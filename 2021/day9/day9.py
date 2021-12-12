import numpy as np

from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=15,
    example_2=1134,
    input_parse_line=lambda i: [int(j) for j in i],
    input_parse_overall=lambda i: i
)


# Puzzle 1
def puzzle_1(p_input: list):
    low_points: list = []
    for r in range(len(p_input)):
        for c in range(len(p_input[r])):
            if (
                    (r == 0 or p_input[r-1][c] > p_input[r][c]) and
                    (c == 0 or p_input[r][c-1] > p_input[r][c]) and
                    (r == len(p_input)-1 or p_input[r+1][c] > p_input[r][c]) and
                    (c == len(p_input[r])-1 or p_input[r][c+1] > p_input[r][c])
            ):
                low_points.append(p_input[r][c])
    return sum([p+1 for p in low_points])


# Puzzle 2
def puzzle_2(p_input: list):
    basins: list = []

    num_rows, num_cols = len(p_input), len(p_input[0])

    def find_adjacent(row: int, col: int) -> list:
        adjacent: list = []
        if row > 0:
            adjacent.append((row-1, col))
        if row < num_rows - 1:
            adjacent.append((row+1, col))
        if col > 0:
            adjacent.append((row, col-1))
        if col < num_cols - 1:
            adjacent.append((row, col+1))

        return adjacent

    def find_basin(row: int, col: int, cur_basin: list) -> set:

        for point in find_adjacent(row, col):
            if point in cur_basin or p_input[point[0]][point[1]] == 9:
                continue

            adjacent_adjacents: list = find_adjacent(*point)
            is_lower: list = [p_input[p[0]][p[1]] < p_input[point[0]][point[1]] for p in adjacent_adjacents]

            if all([adjacent_adjacents[i] in cur_basin for i in range(len(is_lower)) if is_lower[i]]):
                cur_basin.append(point)
                cur_basin += find_basin(point[0], point[1], cur_basin)

        return set(cur_basin)

    for r in range(len(p_input)):
        for c in range(len(p_input[r])):
            if (
                    (r == 0 or p_input[r-1][c] > p_input[r][c]) and
                    (c == 0 or p_input[r][c-1] > p_input[r][c]) and
                    (r == len(p_input)-1 or p_input[r+1][c] > p_input[r][c]) and
                    (c == len(p_input[r])-1 or p_input[r][c+1] > p_input[r][c])
            ):
                basins.append(find_basin(r, c, [(r, c)]))

    return int(np.prod(sorted([len(b) for b in basins], reverse=True)[:3]))


# Print final answers
print(f"\nPuzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"\nPuzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
