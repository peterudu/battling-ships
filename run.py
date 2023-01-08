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


# Create 3 battleships
class Battleship:
    def __init__(self, board):
        self.board = board

    def create_battleship(self):
        for i in range(3):
            self.h_row, self.v_column = randint(0, 4), randint(0, 4)
            while self.board[self.h_row][self.v_column] == "X":
                self.h_row, self.v_column = randint(0, 4), randint(0, 4)
            self.board[self.h_row][self.v_column] = "X"
        return self.board

    # Get player's input
    def get_player_input(self):
        try:
            h_row = input("Enter row position 1-5 for a battleship: ")
            while h_row not in "12345":
                print('Invalid choice, please select a valid row')
                h_row = input("Enter row position 1-5 for a battleship: ")

            v_column = input("Enter column postion A-E for a battleship: ").upper()
            while v_column not in "ABCDE":
                print('Invalid choice, please select a valid column')
                v_column = input("Enter column postion A-E for a battleship: ").upper()
                
            return int(h_row) - 1, GameBoard.convert_letters_to_numbers()[v_column]
        except ValueError and KeyError:
            print("Your input is not valid")
            return self.get_player_input()

    # Number of  battleships shot successfully
    def count_eliminated_ships(self):
        eliminated_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    eliminated_ships += 1
        return eliminated_ships
