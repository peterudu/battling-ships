from random import randint

game_score = {"player": 0, "computer": 0}

# Board which displays the location of the battleships 
HIDDEN_BOARD = [[" "] * 5 for x in range(5)]
# Board which displays player's shot attempts
GUESS_BOARD = [[" "] * 5 for i in range(5)]

def print_board(board):
    print("  A B C D E")
    print("  +-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

        