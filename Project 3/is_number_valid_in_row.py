def numberInColumn(board, target_column, target_value):
    # copied from project2/sudoku.py
    for i in range(len(board)):
        if board[i][target_column] == target_value:
            return True
    return False


def numberInLocalSquare(board, target_square, target_value):
    # copied from project2/sudoku.py
    indices = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    target_list = indices[target_square // 3]
    target_index = indices[target_square % 3]
    for i in target_list:
        for j in target_index:
            if board[i][j] == target_value:
                return True
    return False


def is_number_valid_in_row(board, solution_list, row_number):
    solution_iter = iter(solution_list)
    for index, number in enumerate(board[row_number]):
        if number == 0:
            next_solution = next(solution_iter)
            if numberInColumn(board, index, next_solution) or numberInLocalSquare(
                board, ((row_number // 3) * 3 + index // 3), next_solution
            ):
                return False
            else:
                board[row_number][index] = next_solution
    return True


inp = input()  # reads in the board
inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
myBoard = [
    list(map(float, t.split(","))) for t in inp_strip.split(";")
]  # creates a board for input
row = int(input("Enter the row number in which you're testing (integer from 0-8): "))
solutions = [
    int(num)
    for num in input(
        "Enter the numbers you're trying to insert into the board (separated by spaces): "
    ).split()
]
print(is_number_valid_in_row(myBoard, solutions, row))
