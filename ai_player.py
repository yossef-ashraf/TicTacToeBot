"""
Contains the AI player implementation using:
- Minimax algorithm
- Alpha-beta pruning
- Heuristic evaluation
"""

class AIPlayer:
    def __init__(self, player_symbol, use_alpha_beta=True, use_heuristics=True):
        self.player = player_symbol  # 1=X, 2=O
        self.use_alpha_beta = use_alpha_beta
        self.use_heuristics = use_heuristics
        
    def get_move(self, board):
        """Get the AI's best move using minimax with optional optimizations"""
        if len(board.get_available_moves()) == 9:
            # First move optimization
            return (1, 1)  # Always start with center for optimal play
            
        best_move = None
        best_value = -float('inf')
        alpha = -float('inf')
        beta = float('inf')
        
        for move in board.get_available_moves():
            new_board = board.copy()
            new_board.make_move(move[0], move[1])
            
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
            
        if is_maximizing:
            best_value = -float('inf')
            for move in board.get_available_moves():
                new_board = board.copy()
                new_board.make_move(move[0], move[1])
                value = self.minimax(new_board, False)
                best_value = max(best_value, value)
            return best_value
        else:
            best_value = float('inf')
            for move in board.get_available_moves():
                new_board = board.copy()
                new_board.make_move(move[0], move[1])
                value = self.minimax(new_board, True)
                best_value = min(best_value, value)
            return best_value
            
    def minimax_alpha_beta(self, board, is_maximizing, alpha, beta):
        """Minimax with alpha-beta pruning optimization"""
        if board.is_game_over():
            return self._evaluate_terminal(board)
            
        if self.use_heuristics and not is_maximizing and len(board.get_available_moves()) > 6:
            return self._heuristic_evaluation(board)
            
        if is_maximizing:
            value = -float('inf')
            for move in board.get_available_moves():
                new_board = board.copy()
                new_board.make_move(move[0], move[1])
                value = max(value, self.minimax_alpha_beta(new_board, False, alpha, beta))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  # Beta cutoff
            return value
        else:
            value = float('inf')
            for move in board.get_available_moves():
                new_board = board.copy()
                new_board.make_move(move[0], move[1])
                value = min(value, self.minimax_alpha_beta(new_board, True, alpha, beta))
                beta = min(beta, value)
                if beta <= alpha:
                    break  # Alpha cutoff
            return value
            
    def _evaluate_terminal(self, board):
        """Evaluate terminal game states (win/lose/draw)"""
        if board.winner == self.player:
            return 10
        elif board.winner == 3 - self.player:
            return -10
        return 0
            
    def _heuristic_evaluation(self, board):
        """Evaluate non-terminal board states using heuristics"""
        score = 0
        opponent = 3 - self.player
        
        # Evaluate all possible lines (rows, columns, diagonals)
        lines = [
            *[board.board[i] for i in range(3)],  # Rows
            *[board.board[:,i] for i in range(3)],  # Columns
            [board.board[i][i] for i in range(3)],  # Diagonal
            [board.board[i][2-i] for i in range(3)]  # Anti-diagonal
        ]
        
        for line in lines:
            if np.count_nonzero(line == self.player) == 2 and np.count_nonzero(line == 0) == 1:
                score += 5  # Potential win
            elif np.count_nonzero(line == self.player) == 1 and np.count_nonzero(line == 0) == 2:
                score += 1  # Potential line
            
            if np.count_nonzero(line == opponent) == 2 and np.count_nonzero(line == 0) == 1:
                score -= 4  # Block opponent
        
        return score