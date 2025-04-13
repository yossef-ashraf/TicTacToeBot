"""
Main game file that runs the Tic-Tac-Toe game
Handles:
- Game initialization
- Player vs AI turn management
- Game loop and win conditions
- User interface
"""

from board import Board
from ai_player import AIPlayer

def play_game(human_first=True):
    game = Board()
    ai = AIPlayer(player_symbol=2 if human_first else 1)
    
    print("Welcome to Intelligent Tic-Tac-Toe!")
    print("You are playing as", 'X' if human_first else 'O')
    print("Enter moves as row and column numbers (0-2), separated by space")
    
    while not game.is_game_over():
        game.display()
        
        if (game.current_player == 1 and human_first) or (game.current_player == 2 and not human_first):
            # Human player's turn
            while True:
                try:
                    move = input("Your move (row col): ").strip().split()
                    if len(move) != 2:
                        raise ValueError
                    row, col = map(int, move)
                    if not game.make_move(row, col):
                        print("Invalid move. Try again.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter two numbers between 0-2 separated by space.")
        else:
            # AI's turn
            print("AI is thinking...")
            row, col = ai.get_move(game)
            game.make_move(row, col)
            print(f"AI played at ({row}, {col})")
    
    game.display()
    if game.winner == 0:
        print("It's a draw!")
    else:
        winner = 'X' if game.winner == 1 else 'O'
        print(f"{winner} wins!")

if __name__ == "__main__":
    print("Tic-Tac-Toe AI Player")
    print("1. Play as X (go first)")
    print("2. Play as O (go second)")
    choice = input("Choose (1/2): ")
    play_game(choice == '1')