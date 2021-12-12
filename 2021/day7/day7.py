from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=37,
    example_2=168,
    input_parse_line=lambda i: str(i),
    input_parse_overall=lambda i: [int(j) for j in i[0].split(",")]
)


# Puzzle 1
def puzzle_1(p_input: list):
    fuels: list = []
    for i in range(min(p_input), max(p_input)+1):
        fuels.append([i, 0])
        for pos in p_input:
            fuels[-1][1] += abs(i - pos)
    return min(fuels, key=lambda x: x[1])[1]


# Puzzle 2
def puzzle_2(p_input: list):
    fuels: list = []
    for i in range(min(p_input), max(p_input) + 1):
        fuels.append([i, 0])
        for pos in p_input:
            fuels[-1][1] += (1+abs(i - pos))*abs(i - pos)/2
    return int(min(fuels, key=lambda x: x[1])[1])


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
