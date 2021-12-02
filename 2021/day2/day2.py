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


# Puzzle 1
h, d = 0, 0
for i in A:
    num = int(i.split()[-1])
    if i.startswith("forward"):
        h += num
    if i.startswith("down"):
        d += num
    if i.startswith("up"):
        d -= num

a1 = h * d


# Puzzle 2
h, d = 0, 0
aim = 0
for i in A:
    num = int(i.split()[-1])
    if i.startswith("forward"):
        h += num
        d += aim * num
    if i.startswith("down"):
        aim += num
    if i.startswith("up"):
        aim -= num

a2 = h * d


# Print final answers
print(f"Puzzle 1 Answer:\n{a1}")
print()
print(f"Puzzle 2 Answer:\n{a2}")
