"""
Handles all board-related operations:
- Board state management
- Move validation
- Win condition checking
- Board display
"""

import numpy as np

class Board:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)  # 0=empty, 1=X, 2=O
        self.current_player = 1  # X starts first
        self.winner = None
        
    def make_move(self, row, col):
        """Attempt to make a move, returns True if successful"""
        if self.board[row][col] != 0:
            return False
            
        self.board[row][col] = self.current_player
        self._check_winner()
        
        if not self.is_game_over():
            self.current_player = 3 - self.current_player  # Switch player
            
        return True
        
    def _check_winner(self):
        """Check if the current move resulted in a win"""
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                self.winner = self.board[i][0]
                return
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                self.winner = self.board[0][i]
                return
                
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            self.winner = self.board[0][0]
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            self.winner = self.board[0][2]
            return
            
        # Check for draw
        if np.all(self.board != 0):
            self.winner = 0  # Draw
            
    def is_game_over(self):
        """Check if the game has ended"""
        return self.winner is not None
        
    def get_available_moves(self):
        """Return list of available (row,col) moves"""
        return [(r,c) for r in range(3) for c in range(3) if self.board[r][c] == 0]
        
    def display(self):
        """Print the current board state"""
        symbols = {0: ' ', 1: 'X', 2: 'O'}
        print("  0 1 2")
        for i, row in enumerate(self.board):
            print(i, end=" ")
            for cell in row:
                print(symbols[cell], end=" ")
            print()
        print()
        
    def copy(self):
        """Create a deep copy of the board"""
        new_board = Board()
        new_board.board = self.board.copy()
        new_board.current_player = self.current_player
        new_board.winner = self.winner
        return new_board