import tkinter as tk
from tkinter import ttk

def credits(root):
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Credits")
    root.configure(bg="#353A3E")
    
    label = ttk.Label(root, text="Credits", font=("Arial", 30),foreground="#EAEAEA",background="#353A3E")
    label.pack(pady=20)
