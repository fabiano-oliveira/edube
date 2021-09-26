"""
As you probably know, Sudoku is a number-placing puzzle played on a 9x9 board. The player has to fill the board in a very specific way:

each row of the board must contain all digits from 0 to 9 (the order doesn't matter)
each column of the board must contain all digits from 0 to 9 (again, the order doesn't matter)
each of the nine 3x3 "tiles" (we will name them "sub-squares") of the table must contain all digits from 0 to 9.
If you need more details, you can find them here.

Your task is to write a program which:

reads 9 rows of the Sudoku, each containing 9 digits (check carefully if the data entered are valid)
outputs Yes if the Sudoku is valid, and No otherwise.
"""


def split_into_subsquares(sudoku):
    sudoku = sudoku.strip().split()
    subsquares = [[] for i in range(9)]

    for line in range(9):
        for column in range(9):
            square_index = (line // 3) * 3 + (column // 3)
            subsquares[square_index].append(sudoku[line][column])

    return subsquares


def has_unique_elements(subsquare):
    return all([subsquare.count(element) == 1 for element in subsquare])

def validate_subsquares(subsquares):
    """Returns TRUE if all sudoku sub-squares are valid"""    
    return all([has_unique_elements(s) for s in subsquares])


def print_validation(sudoku):
    subsquares = split_into_subsquares(sudoku)
    if(validate_subsquares(subsquares)):
        print("Is Sudoku valid? YES!")
    else:
        print("Is Sudoku valid? NO!")

sudoku1 = """
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
"""

sudoku2 = """
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
"""

print_validation(sudoku1)
print_validation(sudoku2)