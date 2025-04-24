import tkinter as tk
from tkinter import ttk

def home(root):
    # Clear everything in the root window
    for widget in root.winfo_children():
        widget.destroy()

    label = ttk.Label(root, text="Quiz App", font=("Arial", 16))
    label.pack(pady=20)
