# Scrabble Project
This repository is maitained as part of the course project of the course Logic of Inference. 
In this project, we have tried to implement an agent which can generate the move based on the current state of the scrabble board and the letters available in the rack such that out of all the possible moves, this move fetches the agent the maximum score.

## Problem Definition
* Scrabble is a board game with dimensions 15x15 and there are 2 to 4 players.
* Each player has a set of 7 tiles also known as the rack, to begin the game. 
* During the first turn, the player places a word formed using the tiles in the rack, either across a row or a column, which starts at position (7,7).
* During the subsequent turns, the other player has to extend the word already present either along the row or the column, such that it forms a legal move.
* After each turn, the player has to randomly pick the tiles from the bag of tiles so that there are always 7 tiles in his/her rack.

## What counts as a legal move?
* We only need to define the leagal moves across the row. The legal moves across a column are nothing but the legal moves across a row for the transpose of the board.
* For a move to be legal, at least one of the tiles should be adjacent to a tile already placed along that particular row on the board. 
* All the tiles which are now ``chained” together across a row, should form a valid word.
* If the newly placed tile happens to be adjacent to a tile along some column then that chain of tiles must also form a valid word.

## Algorithm:
* The algorithm works by checking all the extensions for all the words and then picking the legal extension which leads to maximum increase in the score.
* This logic has been implemented in the `move_generation.py` file in the `backend` subdirectory

## Technologies used 
The core logic has been implemented in Python and for the GUI, the frontend UI has been made using React.
One Flask RESTFul API endpoint is made so that the frontend can connect with the backend and use the core logic. 
Other than Flask RESTFul, NumPy has been used to manage the operations on the scrabble board. 
The `permutations` function from `itertools` library is used to generate all the valid extensions.