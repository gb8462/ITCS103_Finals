import tkinter as tk
from tkinter import ttk

def home():
    window = tk.Tk()
    window.geometry("700x500")
    window.title("Home")
    window.configure(bg="#353A3E")

    label = ttk.Label(window, text="Quiz App", font=("Arial", 16))
    label.pack(pady=20)