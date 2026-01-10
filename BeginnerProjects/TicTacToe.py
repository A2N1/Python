import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            button = tk.Button(frame, text=" ", font=("Arial", 20), height=2, width=5,
                               command=lambda idx=i: self.on_click(idx))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        restart_button = tk.Button(self.root, text="Restart", font=("Arial", 12),
                                   command=self.restart_game)
        restart_button.pack(pady=10)

    def on_click(self, idx):
        if self.board[idx] == " ":
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)

            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.restart_game()
                return

            if self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.restart_game()
                return

            self.current_player = "O" if self.current_player == "X" else "X"

            if self.current_player == "O":
                self.computer_move()

    def computer_move(self):
        empty_spots = [i for i, spot in enumerate(self.board) if spot == " "]
        if empty_spots:
            move = random.choice(empty_spots)
            self.board[move] = "O"
            self.buttons[move].config(text="O")

            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.restart_game()
                return

            if self.is_board_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                self.restart_game()
                return

            self.current_player = "X"

    def check_winner(self):
        lines = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for line in lines:
            a, b, c = line
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def is_board_full(self):
        return " " not in self.board

    def restart_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
