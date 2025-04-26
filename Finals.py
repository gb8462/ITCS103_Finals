import tkinter as tk
from tkinter import ttk
from Modules import (takeQuiz,Credits,createQuiz)

window = tk.Tk()
window.geometry("900x500")
window.title("TryQuizMe")
window.configure(bg="#353A3E")

# Functions
def TQuiz():
    takeQuiz.quiz(window)

def CQuiz():
    createQuiz.makeQuiz(window)

def cred():
    Credits.credits(window)

def close_window():
    window.destroy()

# widgets

label = ttk.Label(window, text="TryQuizMe", font=("Roboto", 40),foreground="#EAEAEA",background="#353A3E")
label.pack(pady=25)

button1 = tk.Button(window, text="Take Quiz", height=3, width=25, command=TQuiz)
button1.pack(pady=10)

button2 = tk.Button(window, text="Create Quiz", height=3, width=25, command=CQuiz)
button2.pack(pady=10)

button3 = tk.Button(window, text="Quit", height=3, width=25, command=close_window)
button3.pack(pady=10)


window.mainloop()
