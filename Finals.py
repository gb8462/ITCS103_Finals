import tkinter as tk
from tkinter import ttk

# Group 2 ITCS103 Finals Project

window = tk.Tk()
window.geometry("500x500")
window.title("Group2 Finals Project!")

# widgets

label = ttk.Label(window, text="Chess", font=("Arial", 30))
label.pack(pady=40)

button = tk.Button(window, text="Play Game",width=20, height=3) # Play
button.pack(pady=5)
button = tk.Button(window, text="Quit",width=20, height=3) # Quit
button.pack(padx=5,pady=5)




window.mainloop()