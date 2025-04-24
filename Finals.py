import tkinter as tk
from tkinter import ttk
from Modules import Home

window = tk.Tk()
window.geometry("700x500")
window.title("Quiz App!")
window.configure(bg="#353A3E")

# Functions
def handle_click(event):
    Home.home(window)  # Pass the window to the home function

# widgets
button = tk.Button(window, text="Testing")
button.bind("<Button-1>", handle_click)
button.pack(pady=100)

window.mainloop()
