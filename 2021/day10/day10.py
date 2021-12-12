import statistics

from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=26397,
    example_2=288957,
    input_parse_line=str,
    input_parse_overall=lambda i: i
)


# Puzzle 1
def puzzle_1(p_input: list):
    opened: list = ["(", "[", "{", "<"]
    closed: list = [")", "]", "}", ">"]
    points: list = [3, 57, 1197, 25137]

    score: int = 0
    for line in p_input:
        chars: list = []
        for char in line:
            if char in opened:
                chars.append(char)
            else:
                if chars[-1] != opened[closed.index(char)]:
                    score += points[closed.index(char)]
                    break
                else:
                    chars.pop()

    return score


# Puzzle 2
def puzzle_2(p_input: list):
    opened: list = ["(", "[", "{", "<"]
    closed: list = [")", "]", "}", ">"]
    points: list = [1, 2, 3, 4]

    non_corrupted: list = []

    for line in p_input:
        chars: list = []
        for char in line:
            if char in opened:
                chars.append(char)
            else:
                if chars[-1] != opened[closed.index(char)]:
                    break
                else:
                    chars.pop()
        else:
            non_corrupted.append(line)

    scores: list = []
    for line in non_corrupted:

        complete: list = []
        chars: list = []
        for char in line:
            if char in opened:
                chars.append(char)
            else:
                chars.pop()

        for c in chars[::-1]:
            complete.append(closed[opened.index(c)])

        score: int = 0
        for c in complete:
            score *= 5
            score += points[closed.index(c)]
        scores.append(score)

    return statistics.median(scores)


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
