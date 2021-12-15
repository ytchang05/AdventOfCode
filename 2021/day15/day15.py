from heapq import heappush, heappop

import numpy as np

from utilities.utils import Puzzle


# Create Puzzle object
PUZZLE: Puzzle = Puzzle(
    example_1=40,
    example_2=315,
    input_parse_line=lambda i: [int(j) for j in list(i)],
    input_parse_overall=lambda i: i
)


# Puzzle 1
def puzzle_1(p_input: list):
    nodes: dict = {(x, y): [False, 1e100, p_input[y][x]] for y in range(len(p_input)) for x in range(len(p_input[0]))}
    nodes.update({(0, 0): [False, 0, p_input[0][0]]})

    priority_queue: list = []

    current: tuple = (0, 0)

    def unvisited_neighbors(coords: tuple) -> list:
        n: list = []
        if coords[0] < len(p_input[0])-1 and not nodes[(p := (coords[0]+1, coords[1]))][0]:
            n.append(p)
        if coords[0] > 0 and not nodes[(p := (coords[0]-1, coords[1]))][0]:
            n.append(p)
        if coords[1] < len(p_input[0])-1 and not nodes[(p := (coords[0], coords[1]+1))][0]:
            n.append(p)
        if coords[1] > 0 and not nodes[(p := (coords[0], coords[1]-1))][0]:
            n.append(p)
        return n

    while current != (len(p_input[0]), len(p_input)):
        neighbors: list = unvisited_neighbors(current)

        for ne in neighbors:
            if (m := nodes[current][1] + nodes[ne][2]) < nodes[ne][1]:
                nodes[ne] = [nodes[ne][0], m, nodes[ne][2]]
                heappush(priority_queue, (m, ne))

        nodes[current][0] = True

        try:
            current = heappop(priority_queue)[1]
        except IndexError:
            break

    return nodes[(len(p_input[0])-1, len(p_input)-1)][1]


# Puzzle 2
def puzzle_2(p_input: list):
    def expand(array: np.ndarray, add: int) -> np.ndarray:
        e: np.ndarray = array + add
        e[e > 9] = e[e > 9] % 9
        return e

    expanded: np.ndarray = np.concatenate(tuple(expand(np.array(p_input), j) for j in range(5)), axis=1)

    for i in range(1, 5):
        expanded: np.ndarray = np.concatenate((expanded, np.concatenate(tuple(expand(np.array(p_input), i+j) for j in range(5)), axis=1)), axis=0)

    return puzzle_1(expanded.tolist())


# Print final answers
print(f"Puzzle 1 Answer:\n{PUZZLE.solve(1, puzzle_1)}")
print()
print(f"Puzzle 2 Answer:\n{PUZZLE.solve(2, puzzle_2)}")
