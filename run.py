from random import randint


class GameBoard:
    def __init__(self, board):
        self.board = board

    # Convert letters to numbers
    def fix_letters_to_numbers(self):
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    def print_board(self):
        print("  A B C D E")
        print("  +-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    # Create 3 hidden battleships in computer board
    def create_battleship(self):
        for i in range(3):
            self.h_row, self.v_column = randint(0, 4), randint(0, 4)
            while self.board[self.h_row][self.v_column] == "X":
                self.h_row, self.v_column = randint(0, 4), randint(0, 4)
            self.board[self.h_row][self.v_column] = "X"
        return self.board

    # Get player's guess input
    def get_player_input(self):
        try:
            h_row = input("Enter row value 1-5: ")
            while h_row not in "12345":
                print('Invalid choice, please enter a valid row number')
                h_row = input("Enter row value 1-5: ")

            v_column = input("Enter column value A-E: ").upper()
            while v_column not in "ABCDE":
                print('Invalid choice, please enter a valid column letter')
                v_column = input("Enter column value A-E: ").upper()
            return int(h_row) - 1, GameBoard.fix_letters_to_numbers()[v_column]
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


def RunGame():
    """
    Starts a new game. Displays the game board and prompts the user
    to guess the cordinates for the position of target battleship
    """
    computer_board = GameBoard([[" "] * 5 for i in range(5)])
    players_board = GameBoard([[" "] * 5 for i in range(5)])
    Battleship.create_battleship(computer_board)
    # Start 5 turns
    turns = 10
    while turns > 0:
        print("-------------------------------------")
        print("Welcome to Battling Ships Game")
        print("Board size: 5. Number of hidden ships: 3")
        print("Top left corner is row: 1, column: A")
        print("-------------------------------------")
        GameBoard.print_board(players_board)
        # get player input
        player_h_row, player_v_column = Battleship.get_player_input(object)

        # check if guess already exist
        p = players_board.board[player_h_row][player_v_column] == "-"
        c = players_board.board[player_h_row][player_v_column] == "X"
        while p or c:
            print("You have already guessed that ship positions2")
            player_h_row, player_v_column = Battleship.get_player_input(object)
        # check for hit or miss
        if computer_board.board[player_h_row][player_v_column] == "X":
            print("Hurrah you successfully sunk a battleship!")
            players_board.board[player_h_row][player_v_column] = "X"
        else:
            print("You missed your target shot")
            players_board.board[player_h_row][player_v_column] = "-"
        # check for win or lose
        if Battleship.count_eliminated_ships(players_board) == 3:
            print("You successfully eliminated all enemy ships!")
            break
        else:
            turns -= 1
            print(f"You have {turns} turns remaining")
            if turns == 0:
                print("You have no turns left")
                GameBoard.print_board(players_board)
                break


if __name__ == '__main__':
    RunGame()
