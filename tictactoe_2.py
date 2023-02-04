import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        
        self.board = [[" " for i in range(3)] for j in range(3)]
        
        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                button = tk.Button(master, text=" ", width=10, height=5, font=("Helvetica", 20), command=lambda i=i, j=j: self.move(i, j))
                button.grid(row=i, column=j)
                button_row.append(button)
            self.buttons.append(button_row)
        
    def move(self, i, j):
        if self.board[i][j] == " ":
            self.board[i][j] = "X"
            self.buttons[i][j].configure(text="X", state="disabled")
            if not self.check_win("X"):
                self.computer_move()
            self.check_win("O")
    
    def computer_move(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    self.buttons[i][j].configure(text="O", state="disabled")
                    return
    
    def check_win(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                self.game_over(player)
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                self.game_over(player)
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            self.game_over(player)
            return True
        return False
    
    def game_over(self, player):
        self.disable_buttons()
        tk.messagebox.showinfo("Game Over", player + " wins")
    
    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
