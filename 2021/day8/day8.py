from itertools import permutations

from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=26,
    example_2=61229,
    input_parse_line=lambda i: tuple([j.split() for j in i.split(" | ")]),
    input_parse_overall=lambda i: i
)


# Puzzle 1
def puzzle_1(p_input: list):
    p_input = [[len(j) for j in i[1]] for i in p_input]
    return sum([i.count(2) + i.count(4) + i.count(3) + i.count(7) for i in p_input])


# Puzzle 2
def puzzle_2(p_input: list):
    values: int = 0

    correct_digit_segments: dict = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg"
    }
    correct_digit_segments_backwards: dict = {v: k for k, v in correct_digit_segments.items()}

    letters: str = "abcdefg"

    def string(ltrs: list) -> str:
        return "".join(sorted(ltrs))

    for signals, digits in p_input:
        signals = sorted([string(s) for s in signals])

        for p in permutations(letters):

            mapping: dict = {letters[i]: p[i] for i in range(len(p))}

            if signals == sorted([
                string([
                    mapping[ltr] for ltr in correct_digit_segments[n]
                ]) for n in correct_digit_segments.keys()
            ]):
                break

        mapping_backwards = {v: k for k, v in mapping.items()}

        values += int("".join([
            str(correct_digit_segments_backwards[string([
                mapping_backwards[i] for i in d
            ])]) for d in digits
        ]))

    return values


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
