from random import randint


class GameBoard:
    def __init__(self, board):
        self.board = board

    def fix_letters_to_numbers():
        """
        Convert letters entered by users to numbers
        """
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        return letters_to_numbers

    def print_board(self):
        """
        Prints the 5 grid game board for the user
        """
        print("  A B C D E")
        print("  +-+-+-+-+")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    def __init__(self, board):
        self.board = board

    def create_battleship(self):
        """
        Randomly create and position 3 hidden battleships in computer board
        """
        for i in range(3):
            self.h_row, self.v_column = randint(0, 4), randint(0, 4)
            while self.board[self.h_row][self.v_column] == "X":
                self.h_row, self.v_column = randint(0, 4), randint(0, 4)
            self.board[self.h_row][self.v_column] = "X"
        return self.board

    def get_player_input(self):
        """
        Get player's guess row and column input data
        """
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

    def count_eliminated_ships(self):
        """
        Tracks and counts the number of ships guessed successfully
        """
        eliminated_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    eliminated_ships += 1
        return eliminated_ships


def RunGame():
    """
    Starts a new game with 10 turns for the user.
    Runs the program functions which starts a new game
    with 10 turns, which display the players game board,
    prompts the user to make a guess of the cordinates of hidden ship.
    Displays game status to user
    """
    computer_board = GameBoard([[" "] * 5 for i in range(5)])
    players_board = GameBoard([[" "] * 5 for i in range(5)])
    Battleship.create_battleship(computer_board)
    # starts 10 turns
    turns = 10
    while turns > 0:
        print("-------------------------------------")
        print("Welcome to Battling Ships Game")
        print("Board size: 5. Number of hidden ships: 3")
        print("Top left corner is row: 1, column: A")
        print(f"You have {turns} turns remaining")
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
                print("You have no turns left - Game Over")
                GameBoard.print_board(players_board)
                break


if __name__ == '__main__':
    RunGame()
