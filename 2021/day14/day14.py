from collections import defaultdict

from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=1588,
    example_2=2188189693529,
    input_parse_line=lambda i: i.split(" -> ") if ">" in i else i,
    input_parse_overall=lambda i: [i[0], i[2:]]
)


# Puzzle 1
def puzzle_1(p_input: list):
    polymer: str = p_input[0]

    insertions: dict = defaultdict(str)
    for i in p_input[1]:
        if isinstance(i, list):
            insertions[i[0]] = i[1]

    for _ in range(10):
        new_polymer: str = polymer[0]
        for i in range(1, len(polymer)):
            new_polymer += insertions[polymer[i-1]+polymer[i]] + polymer[i]
        polymer = new_polymer

    amounts: dict = {}
    for letter in set(polymer):
        amounts[letter] = polymer.count(letter)

    return amounts[max(amounts, key=amounts.get)] - amounts[min(amounts, key=amounts.get)]


# Puzzle 2
def puzzle_2(p_input: list):
    combinations = defaultdict(int)
    for i in range(1, len(p_input[0])):
        combinations[p_input[0][i-1] + p_input[0][i]] += 1

    insertions: dict = defaultdict(str)
    for i in p_input[1]:
        if isinstance(i, list):
            insertions[i[0]] = i[1]

    for _ in range(40):
        new_combinations: dict = defaultdict(int)
        for c in combinations:
            if i := insertions[c]:
                new_combinations[c[0]+i] += combinations[c]
                new_combinations[i+c[1]] += combinations[c]
        combinations = new_combinations

    amounts: dict = {}
    for letter in set([y for x in [list(c) for c in combinations] for y in x]):
        amounts[letter] = sum([v for k, v in combinations.items() if letter == k[0]])
    amounts[p_input[0][-1]] += 1

    return amounts[max(amounts, key=amounts.get)] - amounts[min(amounts, key=amounts.get)]


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
