import tkinter as tk
from tkinter import messagebox
import random

def create_board_ui(root, board, handle_click):
    """Creates a simple UI for the game board."""
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(
                root, text=board[i][j], font=('Arial', 24), height=2, width=5,
                command=lambda r=i, c=j: handle_click(r, c)
            )
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)
    return buttons

def update_board_ui(buttons, board):
    """Updates the UI buttons to reflect the current board state."""
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])

def check_winner(board, player):
    """Checks if the given player has won."""
    return (
        any(all(board[i][j] == player for j in range(3)) for i in range(3)) or
        any(all(board[j][i] == player for j in range(3)) for i in range(3)) or
        all(board[i][i] == player for i in range(3)) or
        all(board[i][2 - i] == player for i in range(3))
    )

def check_tie(board):
    """Checks if the game is a tie."""
    return all(cell != ' ' for row in board for cell in row)

def random_fun_fact():
    """Returns a random fun fact about Tic Tac Toe or related games."""
    facts = [
        "Did you know? Tic Tac Toe was played as early as 1300 BC in ancient Egypt!",
        "Fun Fact: The first computer game was a Tic Tac Toe simulation in 1952 called 'OXO'.",
        "Did you know? Tic Tac Toe is called 'Noughts and Crosses' in the UK.",
        "Fun Fact: A perfect game of Tic Tac Toe always ends in a tie!",
        "Did you know? There are 255,168 unique games of Tic Tac Toe possible!"
    ]
    return random.choice(facts)

def main():
    """Main function to run the game with Tkinter UI."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = [0]  

    def handle_click(row, col):
        if board[row][col] == ' ':
            board[row][col] = players[turn[0]]
            update_board_ui(buttons, board)

            if check_winner(board, players[turn[0]]):
                messagebox.showinfo("Game Over", f"Player {players[turn[0]]} wins! Congratulations!\n{random_fun_fact()}")
                root.quit()
            elif check_tie(board):
                messagebox.showinfo("Game Over", f"It's a tie! Well played both players!\n{random_fun_fact()}")
                root.quit()
            else:
                turn[0] = 1 - turn[0] 
        else:
            messagebox.showwarning("Invalid Move", "This square is already taken!")

    root = tk.Tk()
    root.title("Tic Tac Toe")

    buttons = create_board_ui(root, board, handle_click)

    root.mainloop()

if __name__ == "__main__":
    main()
