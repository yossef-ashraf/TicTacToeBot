## 🧠 **Tic-Tac-Toe AI Algorithm Flowchart**

✅ Minimax  
✅ Alpha-Beta Pruning  
✅ Heuristic Evaluation  

```
                 +-----------------------------+
                 |  Start AI Player Turn       |
                 +-----------------------------+
                              |
                              ↓
           +-----------------------------------------+
           |  Get Current Board State                |
           +-----------------------------------------+
                              |
                              ↓
        +-----------------------------------------------+
        |  Generate List of Available Moves            |
        +-----------------------------------------------+
                              |
                              ↓
        +-------------------------------------------------+
        |  For each Move:                                 |
        |  1. Apply Move to a Copy of the Board           |
        |  2. Call Minimax Function                       |
        +-------------------------------------------------+
                              |
                              ↓
       +-------------------------------------------------------+
       |                Minimax(Board, Depth, Alpha, Beta)     |
       +-------------------------------------------------------+
                 |                     |                   |
                 |                     |                   |
        If Game Over?         If Depth Limit?          Else
        (Win/Lose/Draw)         Use Heuristic         Recursive
          Return Value         Evaluation Score      Exploration
            ↑                        ↑                      |
            +------------------------+                      |
                              |                             |
                     Return Score to Caller                 |
                              |                             ↓
             +----------------------------------------------+
             |  Update Best Move:                           |
             |  - For MAX (AI) → Maximize Score             |
             |  - For MIN (Opponent) → Minimize Score       |
             |                                              |
             |  Apply Alpha-Beta Pruning:                   |
             |  If Alpha ≥ Beta → Stop Further Search       |
             +----------------------------------------------+
                              |
                              ↓
                +-------------------------------+
                |  Select Move with Best Score  |
                +-------------------------------+
                              |
                              ↓
           +-------------------------------------------+
           |  Apply Selected Move on Actual Board      |
           +-------------------------------------------+
                              |
                              ↓
                 +-----------------------------+
                 |     Display Board           |
                 +-----------------------------+
                              |
                              ↓
                 +-----------------------------+
                 |        End Turn             |
                 +-----------------------------+
```

---

💡 **Summary of Logic:**
- The AI explores the entire game tree.
- Alpha-Beta Pruning skips useless branches.
- If the game reaches a depth limit, the AI uses a heuristic to estimate.
- The AI always chooses the move that maximizes its chances of winning (or forces a draw at worst).
