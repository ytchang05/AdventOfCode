# Puzzle answers
a1 = 0
a2 = 0


# Load input file
with open(f"{__file__[:-3]}.txt") as file:
    A: list = [line.strip() for line in file]


# Setup
print(A[:10])
print("\n")


nums = [int(i) for i in A[0].split(",")]


def new_boards() -> list:
    boards = []
    for i in A[1:]:
        if i:
            boards[-1].append([[int(j.strip()), False] for j in i.split()])
        else:
            boards.append([])

    return boards


def check_win(board: list) -> bool:
    for row in board:
        if all([j[1] for j in row]):
            return True

    for c in range(len(board[0])):
        if all([j[1] for j in [r[c] for r in board]]):
            return True

    # Turns out in AoC bingo diagonals don't count...
    # if all([j[1] for j in [board[r][r] for r in range(len(board))]]):
    #     return True
    #
    # if all([j[1] for j in [board[r][len(board)-r-1] for r in range(len(board))]]):
    #     return True

    return False


def mark_num(board: list, num: int) -> list:
    for row in board:
        for v in row:
            if v[0] == num:
                v[1] = True
    return board


def score(board: list, num: int) -> int:
    s = 0
    for row in board:
        for v in row:
            if not v[1]:
                s += v[0]
    return s * num


# Puzzle 1
boards1 = new_boards()

for n in nums:
    for b in range(len(boards1)):
        boards1[b] = mark_num(boards1[b], n)
        if check_win(boards1[b]):
            a1 = score(boards1[b], n)
            break
    else:
        continue
    break


# Puzzle 2
boards2 = new_boards()

done = []
for n in nums:
    for b in range(len(boards2)):
        boards2[b] = mark_num(boards2[b], n)
        if check_win(boards2[b]) and b not in done:
            a2 = score(boards2[b], n)
            done.append(b)


# Print final answers
print(f"Puzzle 1 Answer:\n{a1}")
print()
print(f"Puzzle 2 Answer:\n{a2}")
