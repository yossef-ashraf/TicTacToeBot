"""
Contains all game constants and configurations
"""

# Player symbols
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2

# Game outcomes
DRAW = 0
X_WIN = 1
O_WIN = 2

# Heuristic weights
WIN_SCORE = 10
LOSE_SCORE = -10
TWO_IN_LINE = 5
ONE_IN_LINE = 1
OPPONENT_TWO_IN_LINE = -4