def solve_puzzle_1():
    solutions = []
    for a_knight in [False, True]:
        for b_knight in [False, True]:
            # A says “We are both knaves.”
            a_says = (a_knight, not (a_knight and b_knight))

            if a_says[0] == a_knight and a_says[1] == b_knight:
                solutions.append((a_knight, b_knight))
    return solutions


def solve_puzzle_2():
    solutions = []
    for a_knight in [False, True]:
        for b_knight in [False, True]:
            # A says “We are the same kind.” B says “We are of different kinds.”
            a_says = (a_knight, a_knight == b_knight)
            b_says = (b_knight, a_knight != b_knight)

            # Don't know how to do the logic for this one
            solutions.append((a_knight, b_knight))
    return solutions


# this one doesn't work. I'm not sure why
def solve_puzzle_3():
    solutions = []
    for a_knight in [False, True]:
        for b_knight in [False, True]:
            # A says "B is a knight" and B says "I am a knight."
            a_says = (a_knight, b_knight)
            b_says = (b_knight, b_knight)

            if (
                a_says[0] == a_knight
                and a_says[1] == b_knight
                and b_says[0] == b_knight
                and b_says[1] == b_knight
            ):
                solutions.append((a_knight, b_knight))
    return solutions


# Solve Puzzle 1
solutions_1 = solve_puzzle_1()
print("Puzzle 1 Solutions:")
for solution in solutions_1:
    print(solution)

# # Solve Puzzle 2
# solutions_2 = solve_puzzle_2()
# print("\nPuzzle 2 Solutions:")
# for solution in solutions_2:
#     print(solution)

# Solve Puzzle 3
solutions_3 = solve_puzzle_3()
print("\nPuzzle 3 Solutions:")
for solution in solutions_3:
    print(solution)
