# Puzzle answers
a1 = 0
a2 = 0


# Load input file
with open(f"{__file__[:-3]}.txt") as file:
    A: list = [int(line.strip()) for line in file]


# Setup
N: int = len(A)
print(f"N = {N}")

print(A[:10])
print("\n")


# Puzzle 1
for i in range(N-1):
    if int(A[i+1]) > int(A[i]):
        a1 += 1


# Puzzle 2
for i in range(N-3):
    if (
            int(A[i]) + int(A[i+1]) + int(A[i+2])
    ) < (
            int(A[i+1]) + int(A[i+2]) + int(A[i+3])
    ):
        a2 += 1


# Print final answers
print(f"Puzzle 1 Answer:\n{a1}")
print()
print(f"Puzzle 2 Answer:\n{a2}")
