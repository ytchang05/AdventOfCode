from collections import defaultdict


# Puzzle answers
a1 = 0
a2 = 0


# Load input file
with open(f"{__file__[:-3]}.txt") as file:
    A: list = [line.strip() for line in file]


# Setup
N: int = len(A)
print(f"N = {N}")

print(A[:10])
print("\n")


A = [(list(map(int, A[i].split()[0].split(","))), list(map(int, A[i].split()[-1].split(",")))) for i in range(N)]


# Puzzle 1
grid1 = defaultdict(int)

for i in A:
    x1, x2 = i[0][0], i[1][0]
    y1, y2 = i[0][1], i[1][1]

    # Vertical line (x same)
    if x1 == x2:
        if y2 >= y1:
            for y in range(y1, y2+1):
                grid1[(x1, y)] += 1
        else:
            for y in range(y2, y1+1):
                grid1[(x1, y)] += 1

    # Horizontal line (y same)
    elif y1 == y2:
        if x2 >= x1:
            for x in range(x1, x2 + 1):
                grid1[(x, y1)] += 1
        else:
            for x in range(x2, x1 + 1):
                grid1[(x, y1)] += 1

a1 = len(list(filter(lambda i: i >= 2, grid1.values())))


# Puzzle 2
grid2 = defaultdict(int)

for i in A:
    x1, x2 = i[0][0], i[1][0]
    y1, y2 = i[0][1], i[1][1]

    # Vertical line (x same)
    if x1 == x2:
        if y2 >= y1:
            for y in range(y1, y2+1):
                grid2[(x1, y)] += 1
        else:
            for y in range(y2, y1+1):
                grid2[(x1, y)] += 1

    # Horizontal line (y same)
    elif y1 == y2:
        if x2 >= x1:
            for x in range(x1, x2 + 1):
                grid2[(x, y1)] += 1
        else:
            for x in range(x2, x1 + 1):
                grid2[(x, y1)] += 1

    # Diagonal line
    elif abs(x1-x2) == abs(y1-y2):
        for d in range(abs(x1-x2) + 1):
            grid2[(x1 + d*(1 if x2 > x1 else -1), y1 + d*(1 if y2 > y1 else -1))] += 1

a2 = len(list(filter(lambda i: i >= 2, grid2.values())))


# Print final answers
print(f"Puzzle 1 Answer:\n{a1}")
print()
print(f"Puzzle 2 Answer:\n{a2}")
