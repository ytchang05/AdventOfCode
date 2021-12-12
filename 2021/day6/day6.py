from collections import defaultdict
from copy import copy

from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=5934,
    example_2=26984457539,
    input_parse_line=lambda i: i,
    input_parse_overall=lambda i: [int(j) for j in i[0].split(",")]
)


# Puzzle 1
def puzzle_1(p_input: list):

    for _ in range(80):
        previous_list = copy(p_input)

        for i in range(len(previous_list)):
            p_input[i] -= 1
            if previous_list[i] == 0:
                p_input[i] = 6
                p_input.append(8)

    return len(p_input)


# Puzzle 2
def puzzle_2(p_input: list):

    fish_timers: dict = defaultdict(int)
    for f in sorted(list(set(p_input))):
        fish_timers[f] = p_input.count(f)

    for _ in range(256):
        previous_dict = copy(fish_timers)
        fish_timers: dict = defaultdict(int)
        for k, v in previous_dict.items():
            if k == 0:
                fish_timers[6] += v
                fish_timers[8] += v
            else:
                fish_timers[k-1] += v

    return sum([v for v in fish_timers.values()])


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
