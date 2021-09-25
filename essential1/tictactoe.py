from random import choices

def display_board(board):
    separator = "+---" * 3 + "+"
    for r in range(3):
        print(separator)
        for c in range(3):
            print("|", board[r][c], "", end="")
        print("|")
    print(separator)
    
def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    free_fields = make_list_of_free_fields(board)
    moved = False
    while not moved:
        move = int(input("Enter a square number: "))
        for r, c, v in free_fields:
            if(move == v):
                board[r][c] = "O"
                moved = True

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            if board[r][c] not in ["X", "O"]:
                free_fields.append((r, c, board[r][c]))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    # checks rows
    for x, y, z in board:
        if (x == y and y == z and z == sign):
            return True
            
    # check columns
    for c in range(3):
        x, y, z = board[0][c], board[1][c], board[2][c]
        if (x == y and y == z and z == sign):
            return True
            
    # check cross
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == sign):
        return True
    elif (board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == sign):
        return True
        
    return False
    
def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    r, c, v = choices(free_fields)[0]
    board[r][c] = "X"
    
board = [[3 * r + c for c in range(1, 4)] for r in range(3)]
board[1][1] = "X"
display_board(board)

#print(make_list_of_free_fields(board))

winner = None
while winner is None:
    enter_move(board)
    
    if victory_for(board, "O"):
        winner = "O"
    else: 
        draw_move(board)
        if victory_for(board, "X"):
            winner = "X"

    display_board(board)
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) == 0:
        winner = "T"
    
if winner == "O":
    print("O usuário ganhou.")
elif winner == "X":
    print("O computador ganhou.")
else: 
    print("Empate.")

