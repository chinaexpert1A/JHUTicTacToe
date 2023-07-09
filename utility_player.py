from board import Board
from conditional_player import ConditionalPlayer
from argmax import argmax


# Represents a tic-tac-toe agent evaluating moves with a utility function
# Note: this agent inherits from a conditional player
# Note: it uses its conditional logic for making decisive moves
class UtilityPlayer(ConditionalPlayer):
    def __init__(self, mark):
        # Initialize the player with a mark ('X' or 'O')
        super().__init__(mark)
        self.mark = mark
        self.lines = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6))

    def get_next_move(self, board):
        util_board = board.copy()  # Make a copy of the board

        # Check if AI can win in the next move
        winning_move = self._get_winning_move(util_board, self.mark)
        if winning_move is not None:
            return winning_move

        # Check if opponent can win in the next move and block them
        opponent_mark = 'O' if self.mark == 'X' else 'X'
        blocking_move = self._get_winning_move(util_board, opponent_mark)
        if blocking_move is not None:
            return blocking_move

        util_spaces = self.get_utility_of_spaces(util_board)

        # If no immediate win or block, use utility function to determine best move
        best_move = self._get_best_move(util_spaces)
        return best_move

    def _get_winning_move(self, util_board, mark):
        # Check all available moves to see if there's a winning move for the given mark
        available_moves = util_board.get_open_spaces()  # Get a list of available moves
        for move in available_moves:
            util_board.make_move(move, mark)
            if util_board.current_winner() == mark:
                util_board.board[move] = ' '  # reset the move after check
                return move
            util_board.board[move] = ' '  # reset the move after check
        return None

    def _get_best_move(self, util_spaces):
        # Use utility function to score each available move and return the move with the highest score
        max_index = self.get_max_index(util_spaces)
        return max_index

    def get_max_index(self, lst):
        max_index = 0
        for i in range(1, len(lst)):
            if lst[i] > lst[max_index]:
                max_index = i
        return max_index

    def make_move(self, util_board, space, mark):
        if not util_board.is_open_space(space):
            raise Exception("Move is not valid.")
        util_board.spaces[space] = mark

    def current_winner(self, util_board):
        for mark in ['X', 'O']:
            for line in self.lines:
                if util_board.spaces[line[0]] == mark \
                        and util_board.spaces[line[1]] == mark \
                        and util_board.spaces[line[2]] == mark:
                    return mark
        return None

    def get_line_utility(self, board, line):
        agentMarks = 0
        opponentMarks = 0
        opponent_mark = 'O' if self.mark == 'X' else 'X'
        for space in line:
            if board.spaces[space] == self.mark:
                agentMarks += 1
            elif board.spaces[space] == opponent_mark:
                opponentMarks += 1

        # Utility function
        x1 = 0
        x2 = 0
        o1 = 0
        o2 = 0
        if agentMarks == 2:
            x1 = 1
            x2 = 1
        elif agentMarks == 1:
            x1 = 1
            x2 = 0
        if opponentMarks == 2:
            o1 = 1
            o2 = 1
        elif opponentMarks == 1:
            o1 = 1
            o2 = 0
        lineUtility = 3 * x2 + x1 - (3 * o2 + o1)
        return lineUtility

    def get_utility_of_spaces(self, board):
        lineUtilities = []
        for line in self.lines:
            if board.spaces[line[0]] == "-" and board.spaces[line[1]] == "-" and board.spaces[line[2]] == "-":
                utility = 0
            elif board.spaces[line[0]] != "-" and board.spaces[line[1]] != "-" and board.spaces[line[2]] != "-":
                utility = -10
            else:
                utility = self.get_line_utility(board, line)
            lineUtilities.append(utility)
        return lineUtilities
