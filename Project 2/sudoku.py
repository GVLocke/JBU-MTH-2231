def numberInColumn(board, target_column, target_value):
    """Determines whether a target integer is in a target column of the sudoku board.
    - `board` should be a list of 9 lists of 9 integers from 1 to 9 (A 9x9 sudoku board).
    - `target_column` should be an integer between 1 and 9.
    - `target_value` should be an integer between 1 and 9.
    - Returns a boolean value that's `True` when the number is in the column."""
    for i in range(len(board)):
        if board[i][target_column] == target_value:
            return True
    return False


def numberInLocalSquare(board, target_square, target_value):
    """Determines whether a target integer is in a target local square of the sudoku board.
    - `board` should be a list of 9 lists of 9 integers from 1 to 9 (A 9x9 sudoku board).
    - `target_square` should be an integer between 1 and 9.
    - `target_value` should be an integer between 1 and 9.
    - Returns a boolean value that's `True` when the number is in the column."""
    # These are the indices for the local squares:
    # 0 | - - - | - - - | - - -
    # 1 | - 0 - | - 1 - | - 2 -
    # 2 | - - - | - - - | - - -
    #   | ~~~~~~~~~~~~~~~~~~~~~
    # 3 | - - - | - - - | - - -
    # 4 | - 3 - | - 4 - | - 5 -
    # 5 | - - - | - - - | - - -
    #   | ~~~~~~~~~~~~~~~~~~~~~
    # 6 | - - - | - - - | - - -
    # 7 | - 6 - | - 7 - | - 8 -
    # 8 | - - - | - - - | - - -

    # if the target square is 5
    # 1 < (5 / 3) < 2, which means that I need to check the lists at index 3, 4, and 5 (which are all 1 < (n / 3) < 2)
    # 5 mod 3 is 2. This tells me that I need to check the last three elements of the target lists.
    indices = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]

    target_list = indices[target_square // 3]
    target_index = indices[target_square % 3]
    # if target square is 5, then target_list = (3,4,5) because 5 // 3 = 1
    # same target square will make target_index = (6,7,8) because 5 % 2 = 2

    for i in target_list:
        for j in target_index:
            if board[i][j] == target_value:
                return True
    return False


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(int(board[i][j]), end=" ")
        print("  " + str(i))
    print()
    print("0 1 2 | 3 4 5 | 6 7 8")


inp = input()  # reads in the board
inp_strip = inp.strip("(),[] ")  # removes brackets or parantheses and spaces
myBoard = [
    list(map(float, t.split(","))) for t in inp_strip.split(";")
]  # creates a board for input

# print the board
print_board(myBoard)

target = int(input("Enter a number to search for (0-8): "))
target_column = int(input("Enter a column to search in (0-8): "))
target_square = int(input("Enter a local square to search in (0-8): "))

if numberInColumn(myBoard, target_column, target):
    print(f"{target} is in column {target_column}.")
else:
    print(f"{target} is not in column {target_column}.")

if numberInLocalSquare(myBoard, target_square, target):
    print(f"{target} is in local square {target_square}.")
else:
    print(f"{target} is not in local square {target_square}.")
