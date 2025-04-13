"""
Contains the AI player implementation using:
- Minimax algorithm
- Alpha-beta pruning
- Heuristic evaluation
"""

import numpy as np

class AIPlayer:
    def __init__(self, player_symbol, use_alpha_beta=True, use_heuristics=True):
        self.player = player_symbol  # 1=X, 2=O
        self.use_alpha_beta = use_alpha_beta
        self.use_heuristics = use_heuristics
        
    def get_move(self, board):
        """Get the AI's best move using minimax with optional optimizations"""
        available_moves = board.get_available_moves()
        
        # First move optimization
        if len(available_moves) == 9:
            return (1, 1)  # Always start with center for optimal play
            
        best_move = None
        best_value = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        
        for move in available_moves:
            new_board = board.copy()
            new_board.make_move(*move)
            
            if self.use_alpha_beta:
                move_value = self.minimax_alpha_beta(new_board, False, alpha, beta)
            else:
                move_value = self.minimax(new_board, False)
                
            if move_value > best_value:
                best_value = move_value
                best_move = move
                
            alpha = max(alpha, best_value)
            
        return best_move
        
    def minimax(self, board, is_maximizing):
        """Standard minimax implementation without optimizations"""
        if board.is_game_over():
            return self._evaluate_terminal(board)
            
        best_value = -float('inf') if is_maximizing else float('inf')
        
        for move in board.get_available_moves():
            new_board = board.copy()
            new_board.make_move(*move)
            current_value = self.minimax(new_board, not is_maximizing)
            
            if is_maximizing:
                best_value = max(best_value, current_value)
            else:
                best_value = min(best_value, current_value)
                
        return best_value
            
    def minimax_alpha_beta(self, board, is_maximizing, alpha, beta):
        """Minimax with alpha-beta pruning optimization"""
        if board.is_game_over():
            return self._evaluate_terminal(board)
            
        # Use heuristic evaluation for early game states to speed up
        if self.use_heuristics and not is_maximizing and len(board.get_available_moves()) > 6:
            return self._heuristic_evaluation(board)
            
        best_value = -float('inf') if is_maximizing else float('inf')
        
        for move in board.get_available_moves():
            new_board = board.copy()
            new_board.make_move(*move)
            
            current_value = self.minimax_alpha_beta(new_board, not is_maximizing, alpha, beta)
            
            if is_maximizing:
                best_value = max(best_value, current_value)
                alpha = max(alpha, best_value)
            else:
                best_value = min(best_value, current_value)
                beta = min(beta, best_value)
                
            if alpha >= beta:
                break  # Prune the remaining branches
                
        return best_value
            
    def _evaluate_terminal(self, board):
        """Evaluate terminal game states (win/lose/draw)"""
        if not board.winner:
            return 0
        return 10 if board.winner == self.player else -10
            
    def _heuristic_evaluation(self, board):
        """Evaluate non-terminal board states using heuristics"""
        score = 0
        opponent = 3 - self.player
        
        # Evaluate all possible lines (rows, columns, diagonals)
        lines = []
        
        # Add rows and columns
        for i in range(3):
            lines.append(board.board[i, :])  # Rows
            lines.append(board.board[:, i])  # Columns
            
        # Add diagonals
        lines.append(np.diag(board.board))
        lines.append(np.diag(np.fliplr(board.board)))
        
        for line in lines:
            count_ai = np.count_nonzero(line == self.player)
            count_opponent = np.count_nonzero(line == opponent)
            count_empty = np.count_nonzero(line == 0)
            
            # Positive scores for AI opportunities
            if count_ai == 2 and count_empty == 1:
                score += 5  # Potential win
            elif count_ai == 1 and count_empty == 2:
                score += 1  # Potential line
                
            # Negative scores for opponent threats
            if count_opponent == 2 and count_empty == 1:
                score -= 4  # Block opponent
                
        # Bonus for center control
        if board.board[1, 1] == self.player:
            score += 2
            
        return score