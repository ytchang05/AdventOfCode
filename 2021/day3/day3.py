# Puzzle answers
a1 = 0
a2 = 0


# Load input file
with open(f"{__file__[:-3]}.txt") as file:
    A: list = [line.strip() for line in file]


# Setup
M: int = len(A[0])

print(A[:10])
print("\n")


# Puzzle 1
g, e = "", ""

for i in range(M):
    values = [j[i] for j in A]
    if values.count("0") > values.count("1"):
        g += "0"
        e += "1"
    else:
        g += "1"
        e += "0"

a1 = int(g, 2) * int(e, 2)


# Puzzle 2
A_o, A_c = [], []
o_done, c_done = False, False

for i in range(M):
    values_o = [j[i] for j in A_o or A]
    values_c = [j[i] for j in A_c or A]

    if values_o.count("0") > values_o.count("1") and not o_done:
        A_o = [(A_o or A)[v] for v in range(len(values_o)) if values_o[v] == "0"]
    elif not o_done:
        A_o = [(A_o or A)[v] for v in range(len(values_o)) if values_o[v] == "1"]

    if values_c.count("0") > values_c.count("1") and not c_done:
        A_c = [(A_c or A)[v] for v in range(len(values_c)) if values_c[v] == "1"]
    elif not c_done:
        A_c = [(A_c or A)[v] for v in range(len(values_c)) if values_c[v] == "0"]

    if len(A_o) == 1:
        o_done = True
    if len(A_c) == 1:
        c_done = True

a2 = int(A_o[0], 2) * int(A_c[0], 2)


# Print final answers
print(f"Puzzle 1 Answer:\n{a1}")
print()
print(f"Puzzle 2 Answer:\n{a2}")
