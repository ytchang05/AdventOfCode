from collections import defaultdict
from copy import copy

from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=10,
    example_2=36,
    input_parse_line=lambda i: i.split("-"),
    input_parse_overall=lambda i: i
)


# Puzzle 1
def puzzle_1(p_input: list):
    system: defaultdict = defaultdict(list)
    for connection in p_input:
        system[connection[0]].append(connection[1])
        system[connection[1]].append(connection[0])

    def find_possible_next(path: str) -> list:
        possible: list = []
        for c in system[path[-1]]:
            if ((c.lower() == c) and c not in path) or c.upper() == c:
                possible.append(c)
        return possible

    all_paths: list = [["start"]]
    while any([path[-1] != "end" for path in all_paths]):
        new_paths: list = []
        for path in all_paths:
            if path[-1] == "end":
                new_paths.append(path)
            else:
                possible_next: list = find_possible_next(path)
                for cave in possible_next:
                    new_paths.append(path+[cave])
        all_paths: list = copy(new_paths)

    return len(all_paths)


# Puzzle 2
def puzzle_2(p_input: list):
    system: defaultdict = defaultdict(list)
    for connection in p_input:
        system[connection[0]].append(connection[1])
        system[connection[1]].append(connection[0])

    def find_possible_next(path: str) -> list:
        possible: list = []
        for c in system[path[-1]]:
            if (
                    (c.lower() == c) and (
                        (c not in path) or all([path.count(ca) == 1 for ca in path if ca.lower() == ca])
                    ) and c != "start"
            ) or c.upper() == c:
                possible.append(c)
        return possible

    all_paths: list = [["start"]]
    while any([path[-1] != "end" for path in all_paths]):
        new_paths: list = []
        for path in all_paths:
            if path[-1] == "end":
                new_paths.append(path)
            else:
                possible_next: list = find_possible_next(path)
                for cave in possible_next:
                    new_paths.append(path + [cave])
        all_paths: list = copy(new_paths)

    return len([path for path in all_paths if path[-1] == "end"])


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
