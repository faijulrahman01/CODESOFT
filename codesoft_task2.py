# CODSOFT
#TIC-TAC-TOE AI
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Tic-Tac-Toe AI (Unbeatable)")

board = [' ' for _ in range(9)]
buttons = []

def is_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # cols
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in wins)

def is_draw():
    return ' ' not in board

def minimax(is_maximizing):
    if is_winner('O'): return 1
    if is_winner('X'): return -1
    if is_draw(): return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best = max(score, best)
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best = min(score, best)
        return best

def get_best_move():
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def on_click(i):
    if board[i] == ' ':
        board[i] = 'X'
        buttons[i].config(text='X', state='disabled')
        if is_winner('X'):
            messagebox.showinfo("Game Over", "You Win!")
            window.quit()
            return
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            window.quit()
            return

        ai_move = get_best_move()
        if ai_move is not None:
            board[ai_move] = 'O'
            buttons[ai_move].config(text='O', state='disabled')
            if is_winner('O'):
                messagebox.showinfo("Game Over", "AI Wins!")
                window.quit()
            elif is_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
                window.quit()

for i in range(9):
    btn = tk.Button(window, text=' ', font=('Arial', 30), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

window.mainloop()
