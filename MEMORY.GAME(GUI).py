import tkinter as tk
import random

root = tk.Tk()
root.title("Memory Game")
root.geometry("420x480")
root.configure(bg="#1e1e2f")  # dark background

symbols = ['🍎','🍎','🍌','🍌','🍒','🍒','🍇','🍇',
           '🍉','🍉','🥝','🥝','🍍','🍍','🍑','🍑']

random.shuffle(symbols)

buttons = []
revealed = []
matched = []


def on_click(index):
    if index in matched or index in revealed:
        return

    buttons[index].config(text=symbols[index],
                          bg="#ffffff",
                          fg="#000000",
                          state="disabled")
    revealed.append(index)

    if len(revealed) == 2:
        root.after(500, check_match)


def check_match():
    global revealed

    i1, i2 = revealed

    if symbols[i1] == symbols[i2]:
        matched.extend([i1, i2])
        # Green for matched
        buttons[i1].config(bg="#4CAF50", fg="white")
        buttons[i2].config(bg="#4CAF50", fg="white")
    else:
        # Flip back
        buttons[i1].config(text="", bg="#3b3b58", state="normal")
        buttons[i2].config(text="", bg="#3b3b58", state="normal")

    revealed = []

    if len(matched) == 16:
        win_label.config(text="🎉 You Win!", fg="#FFD700")



frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)

for i in range(16):
    btn = tk.Button(frame,
                    text="",
                    width=6,
                    height=3,
                    font=("Arial", 14),
                    bg="#3b3b58",          # default color
                    fg="white",
                    activebackground="#6c63ff",
                    command=lambda i=i: on_click(i))
    
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    buttons.append(btn)


title = tk.Label(root,
                 text="Memory Game",
                 font=("Arial", 20, "bold"),
                 bg="#1e1e2f",
                 fg="#ffffff")
title.pack()


win_label = tk.Label(root,
                     text="",
                     font=("Arial", 16),
                     bg="#1e1e2f",
                     fg="#FFD700")
win_label.pack(pady=10)


root.mainloop()