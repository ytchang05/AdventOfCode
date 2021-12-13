import itertools
from copy import copy

import numpy as np

from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=17,
    example_2=None,
    input_parse_line=lambda i: [int(j) if "," in i else (i.split()[-1].split("=") if "" != i else i) for j in i.split(",")],
    input_parse_overall=lambda i: [i[:i.index([""])], i[i.index([""])+1:]]
)


# Puzzle 1
def puzzle_1(p_input: list):
    paper: list = [[False for _ in range(max(p_input[0], key=lambda i: i[0])[0]+1)] for _ in range(max(p_input[0], key=lambda i: i[1])[1]+1)]
    p_input[1] = [fold[0] for fold in p_input[1]]

    for dot in p_input[0]:
        paper[dot[1]][dot[0]] = True

    val = int(p_input[1][0][1])

    for y, row in enumerate(paper):
        for x, dot in enumerate(row):

            if not paper[y][x]:
                continue

            if p_input[1][0][0] == "x" and x > val:
                paper[y][2*val-x] = True

            elif p_input[1][0][0] == "y" and y > val:
                paper[2*val-y][x] = True

    if p_input[1][0][0] == "y":
        return list(itertools.chain(*paper[:val])).count(True)
    else:
        return list(itertools.chain(*np.array(paper).T.tolist()[:val])).count(True)


# Puzzle 2
def puzzle_2(p_input: list):
    paper: list = [[False for _ in range(max(p_input[0], key=lambda i: i[0])[0]+1)] for _ in range(max(p_input[0], key=lambda i: i[1])[1]+1)]
    p_input[1] = [fold[0] for fold in p_input[1]]

    for dot in p_input[0]:
        paper[dot[1]][dot[0]] = True

    for fold in p_input[1]:
        val = int(fold[1])

        for y, row in enumerate(paper):
            for x, dot in enumerate(row):

                if not paper[y][x]:
                    continue

                if fold[0] == "x" and x > val:
                    paper[y][2*val-x] = True

                elif fold[0] == "y" and y > val:
                    paper[2*val-y][x] = True

        if fold[0] == "y":
            paper = paper[:val]
        else:
            paper = np.array(np.array(paper).T[:val]).T.tolist()

    for line in paper:
        print("".join(["#" if i else "." for i in line]))


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{puzzle_2(copy(PUZZLE.input))}")  # Answer: RCPLAKHL
