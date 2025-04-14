# Tic-Tac-Toe AI — Full Explanation

## How to Play

### Starting the Game:
1. Run the program (`main.py`).
2. Choose:
   - `1` to play as **X** (you start first).
   - `2` to play as **O** (the computer starts first).

### Entering Moves:
- Enter your move as two numbers: `row` and `column` separated by a space.
- Example: `0 1` means row `0` and column `1`.
```
  0 1 2  ← Column numbers
0  | | 
1  | | 
2  | | 
↑
Row numbers
```

### Example Round:
```
Your move (row col): 1 1
  0 1 2
0  | | 
1  |X| 
2  | | 

AI is thinking...
AI played at (0, 0)
  0 1 2
0 O| | 
1  |X| 
2  | | 
```

---

## UML Class Diagram

```
+-------------------+       +----------------+       +-------------------+
|      Board        |       |    AIPlayer    |       |     main.py       |
+-------------------+       +----------------+       +-------------------+
| - board: int[3][3]|<>-----| - player: int  |       |                   |
| - current_player  |       | - use_alpha_beta|       | - play_game()     |
| - winner          |       | - use_heuristics|       | - user input      |
+-------------------+       +----------------+       +-------------------+
| + make_move()     |       | + get_move()   |       |                   |
| + is_game_over()  |       | + minimax()    |       |                   |
| + display()       |       | + minimax_alpha_beta()|                   |
| + copy()          |       | + _evaluate_terminal()|                   |
| + get_available_moves()|  | + _heuristic_evaluation()|               |
+-------------------+       +----------------+       +-------------------+
```

---

## Sequence Diagram (AI Move)

```
User           main.py         Board         AIPlayer
 |               |               |               |
 |  make move    |               |               |
 |-------------> |               |               |
 |               | update board  |               |
 |               |-------------> |               |
 |               |               |               |
 |  AI turn      |               |               |
 |<------------- |               |               |
 |               | get best move |               |
 |               |------------------------------>|
 |               |               | minimax search |
 |               |               |<--------------|
 |               |               |               |
 |               | make AI move  |               |
 |               |-------------> |               |
 |               |               |               |
 |  display      |               |               |
 |<------------- |               |               |
```

---

## Algorithm Overview: Minimax with Alpha-Beta Pruning

### Step 1: Initial Setup
- AI receives the current board state.
- AI identifies all possible empty cells.

### Step 2: Minimax Recursion
For each move:
1. Apply a hypothetical move.
2. Evaluate:
   - If the game is over: return `10, -10, or 0`.
   - If depth limit reached: return heuristic evaluation.
   - Else: continue recursion.

3. Select:
   - MAX player (AI) → pick highest score.
   - MIN player (opponent) → pick lowest score.

---

### Step 3: Alpha-Beta Pruning
- `alpha`: Best score the MAX player is guaranteed.
- `beta`: Best score the MIN player is guaranteed.
- Prune branches when:
  - MAX’s best ≥ beta.
  - MIN’s best ≤ alpha.

---

### Step 4: Backpropagation
- AI backtracks the evaluated values.
- Picks the move with the highest value.

---

### Example Minimax Walkthrough:

Board (X’s turn):
```
  0 1 2
0 X| | 
1  |O| 
2  | |X
```

- AI checks 5 possible moves.
- Move `(0,1)` leads to an opponent’s win → Score `-10`.
- Move `(1,0)` leads to forced win → Score `+10`.
- AI chooses move `(1,0)`.

---

## Heuristic Evaluation Breakdown

For non-terminal states:

1. **Potential Winning Lines**:
   - `2 X's + empty`: +5.
   - `1 X + 2 empty`: +1.

2. **Blocking Opponent**:
   - `2 O's + empty`: -4.

3. **Center Control**:
   - If center occupied by AI: +1.

---

### Example Heuristic Calculation:

Board:
```
  0 1 2
0 X| |O
1  |X| 
2  | | 
```
Calculation:
- Rows: +1, +1.
- Columns: +1, +1.
- Diagonals: +5.
- Center occupied: +1.

**Total Score = 10.**

---

## Performance Optimization Techniques

1. **Alpha-Beta Pruning**:  
   Reduces search space by half.

2. **Move Ordering**:  
   Evaluates center first, corners second, edges last.

3. **Early Termination**:  
   Detects immediate win/loss.

4. **Memoization** (Optional):  
   Caches evaluated boards to avoid repeating calculations.

---

## Example: Computer Strategy When Player Picks the Center

If the player starts with the center:
```
  0 1 2
0  | | 
1  |X| 
2  | | 
```
The AI will always respond to set up double threats, forcing the player into defense. If the player makes one wrong move, the AI wins. If the player plays perfectly, the game ends in a draw.

---

## Game Tree Illustration

```
       [A] (X turn)
      / | \
    [B][C][D] (O responses)
    / \ ... 
  [E][F] ... (X responses)
```

---

### Practical Example: Move Breakdown

Board (X’s turn):
```
  0 1 2
0 X| |O
1  |X| 
2  | |O
```
Available Moves: `(0,1), (1,0), (1,2), (2,0), (2,1)`.

- Move `(1,2)` leads to instant win: Score `+10`.
- Move `(1,0)` leads to forced win: Score `+10`.
- Other moves lead to lower or draw scores.

---

### Alpha-Beta Pruning Example:

Evaluating move `(2,1)`:
```
  0 1 2
0 X| |O
1  |X| 
2  |X|O
```
- Opponent can force a draw, so AI prunes this move early if it knows other moves lead to a win.

---

### Final Decision:

AI compares all evaluated moves and always picks the one with the highest score, guaranteeing:
- Win if possible.
- Draw if the opponent plays perfectly.
- Never loses.


