
Overview:

Matthew Renza is the original author of the tic tac toe environment using modern best practices and PEP-8 guidelines. Shruti Shah made modifications to make the code base ready for assignments related to algorithm development. 

In addition, he created unit tests for every aspect of this environment to verify it's correctness.
He also eliminated all 3rd-party library dependencies (except for unit testing) to keep things simple.


Files:
 - tic_tac_toe.py - the main program to play a game of tic tac toe against an agent
 - experiment.py - a program to run a specified number of games with automated players for analysis
 - game.py - represents a game of tic tac toe played by two players
 - board.py - represents a tic tac toe board
 - player.py - represents an abstract player to be implemented by the following subclasses <below>
   - human_player.py - represents an human player who is prompted for input via the console
   - sequence_player.py - represents an automated player who plays a pre-defined sequence of moves (for testing)
   - random_player.py - represents an automated player that choses moves at random
   - conditional_player.py - represents an automated agent who uses conditional logic on decisive moves
   - utility_player.py - represents an automated agent who uses a utility function to evaluate moves
   - minimax_player.py - represents an automated agent who uses the brute-force minimax algorithm
   - alpha_beta_player.py - represents an automated agent who uses minimax with alpha-beta pruning
 - [class]_tests.py - contains unit tests for the corresponding class

Notes:
 - The main script is called "tic_tac_toe.py".
 - The indexes of the spaces in the board are row-based rather than column-based.
 - The analysis of optimality and runtime complexity is contained in the "Analysis.docx" file.
 - He used the PyCharm IDE with Python 3.10 interpreter.
 - Caution should be taken running the Minimax player (implementation dependent) in large experiments (e.g. n=100) -- especially as Player 1
    - It can take several minutes to complete the full experiment
 