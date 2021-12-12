import itertools
import math
import statistics
from collections import defaultdict
from copy import copy

import numpy as np

from utilities.logger import Logger as log
from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=None,
    example_2=None,
    input_parse_line=lambda i: i,
    input_parse_overall=lambda i: i
)


# Puzzle 1
def puzzle_1(p_input: list):
    ...


# Puzzle 2
def puzzle_2(p_input: list):
    ...


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
