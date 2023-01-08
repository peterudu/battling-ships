from random import randint

class GameBoard:
    def __init__(self, board):
        self.board = board


    def convert_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    def print_board(self):
        print("  A B C D E")
        print("  +-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1