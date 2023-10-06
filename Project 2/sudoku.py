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


myBoard = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    #   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    [0, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]
print(numberInColumn(myBoard, 0, 9))
print(numberInLocalSquare(myBoard, 4, 2))
