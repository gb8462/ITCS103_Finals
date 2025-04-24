import tkinter as tk
from tkinter import ttk
from Modules import (takeQuiz,Credits,createQuiz)

window = tk.Tk()
window.geometry("800x500")
window.title("TryQuizMe")
window.configure(bg="#353A3E")

# Functions
def TQuiz():
    takeQuiz.quiz(window)

def CQuiz():
    createQuiz.makeQuiz(window)

def cred():
    Credits.credits(window)

# widgets

label = ttk.Label(window, text="TryQuizMe", font=("Arial", 60),foreground="#EAEAEA",background="#353A3E")
label.pack(pady=20)

button1 = tk.Button(window, text="Take Quiz", command=TQuiz)
button1.pack(pady=10)

button2 = tk.Button(window, text="Create Quiz", command=CQuiz)
button2.pack(pady=10)

button3 = tk.Button(window, text="Credits", command=cred)
button3.pack(pady=10)


window.mainloop()
