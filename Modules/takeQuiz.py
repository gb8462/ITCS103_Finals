import tkinter as tk
from tkinter import ttk

def quiz(root):
    # Clear everything in the root window
    root = tk.Tk()
    root.geometry("800x500")
    root.title("Take Quiz")
    root.configure(bg="#353A3E")
    
    label = ttk.Label(root, text="Quizzes Available", font=("Arial", 30),foreground="#EAEAEA",background="#353A3E")
    label.pack(pady=20)
