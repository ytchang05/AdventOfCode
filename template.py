# Puzzle answers
a1 = 0
a2 = 0


# Load input file
with open(f"{__file__[:-3]}.txt") as file:
    # A: list = [line.strip() for line in file]
    A: list = [int(line.strip()) for line in file]


# Setup
N: int = len(A)
print(f"N = {N}")

M: int = len(A[0])

print(A[:10])
print("\n")


# Puzzle 1
for i in range(N):
    pass


# Puzzle 2
for i in range(N):
    pass


# Print final answers
print(f"Puzzle 1 Answer:\n{a1}")
print()
print(f"Puzzle 2 Answer:\n{a2}")
