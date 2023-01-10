# Battling Ships

Battling Ships is a single player python-based terminal game in which the user guesses the coordinate positions of 3 battleships randomly created by the computer but hidden from the view of the user. To win the game the user must successfully locate these 3 battleships within the maximum 10 turns available.

This is a simple version of the paper board Battleship Game which one can read read about in [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game))


## How to play the game
The Battling Ships game starts and the user is presented with an empty 5-rows x 5-column players grid board. 

The user is asked to make a guess of the row number and column letter which together make up the coordinate of a targeted ship position.

If the user guess wrongly it is marked as a "-" on the players board and if the guess is correct it is marked as a "X" on the board.

The user has the 10 possible turn to make 3 correct guesses and if he achieves that the game is won.


### Existing Features
- Creation of 2 game boards
    - A player's guess board which is visible and for the user to input guess data.
    - A computer board which is hidden and contains 3 hidden battleships which the user intends to target.
-  Allows a single user to play against computer
- The user can pass on input data 
- The user receives useful information regarding the game stutus, for example the turns remaining and mention of targeted ships
- The game offers a user the option of a maximum of 10 turns in which to make a successful guess.
- Validation of the users input data 
    - Row input numbers are checked that they are within the range 1 to 5. If this is not the case the user is asked to repeat this process
    - Column input is checked that it is a letter and that it is within the range A to E. If this is not the case the user is asked to repeat the process.

### Future Features

## Data Model

## Testing
### Bugs
#### Solved Bugs

### Remaining Bugs

### Validator Testing

## Deployment

## Credits


