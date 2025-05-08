import customtkinter
import openpyxl
import hashlib, os, re 
from tkinter import messagebox
from openpyxl import Workbook, load_workbook
from datetime import datetime

main = customtkinter.CTk()
main.title("TryQuizMe login")
main.geometry("1100x680")
customtkinter.set_appearance_mode('dark')

main.configure(fg_color="#1f2024")


quiz_file = "quizzes.xlsx"
if not os.path.exists(quiz_file):
    wb = Workbook()
    sheet = wb.active
    sheet.title = "Template"
    sheet['A1'] = "This is a placeholder sheet."
    wb.create_sheet("Scores")
    wb.save(quiz_file)


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def valid_username(username):
    return re.match("^[A-Za-z0-9_]{4,}$", username) is not None

def strong_password(password):
    if len(password) < 6:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[@$!%*#?&]", password):
        return False
    return True

# ========== openpyxl ==========
def initialize_database():
    if not os.path.exists("users.xlsx"):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Users"
        sheet.append(["Username", "Password"])
        workbook.save("users.xlsx")

def save_account(username, password):
    hashed_password = hash_password(password)
    workbook = openpyxl.load_workbook("users.xlsx")
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] == username:
            return False

    sheet.append([username, hashed_password])
    workbook.save("users.xlsx")
    return True

def check_login(username, password):
    hashed_password = hash_password(password)
    workbook = openpyxl.load_workbook("users.xlsx")
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] == username and row[1] == hashed_password:
            return True
    return False

# ========== Window Close ==========
def close_window():
    main.destroy()

# ========== Clear Frame Function ==========
def clear_frame():
    """Clear all widgets in the main window."""
    for widget in main.winfo_children():
        widget.destroy()

# ========== Login Page ==========
current_user = ""

def login_page():
    clear_frame()
    
    login_frame = customtkinter.CTkFrame(main, corner_radius=20)
    login_frame.pack(pady=100, padx=300, fill="both", expand=True)

    label = customtkinter.CTkLabel(login_frame, text="Login", fg_color="transparent", font=("Arial", 75))
    label.pack(pady=(60, 20))

    username_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Username", width=230, corner_radius=15)
    username_entry.pack(pady=(10, 5))

    password_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Password", width=230, corner_radius=15, show="*")
    password_entry.pack(pady=(10, 20))

    error_label = customtkinter.CTkLabel(login_frame, text="", text_color="red")
    error_label.pack()

    def on_login():
        global current_user

        username = username_entry.get()
        password = password_entry.get()

        if check_login(username, password):
            current_user = username 
            Dashboard()
        else:
            error_label.configure(text="Invalid username or password")
    
    main.bind('<Return>', lambda event: on_login()) # Bind Enter key to login
    
    login_button = customtkinter.CTkButton(login_frame, text="Login", corner_radius=20, text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e', command=on_login)
    login_button.pack()

    label = customtkinter.CTkLabel(login_frame, text='or', fg_color='transparent', font=('Arial',12))
    label.pack()

    create_account_button = customtkinter.CTkButton(login_frame, text="Sign up", corner_radius=20, text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e', command=signUp_page)
    create_account_button.pack()

# ========== Sign Up Page ==========
def signUp_page():
    clear_frame()

    signup_frame = customtkinter.CTkFrame(main, corner_radius=20)
    signup_frame.pack(pady=100, padx=300, fill="both", expand=True)

    label = customtkinter.CTkLabel(signup_frame, text="Sign-Up", fg_color="transparent", font=("Arial", 75))
    label.pack(pady=(60, 20))

    username_entry = customtkinter.CTkEntry(signup_frame, placeholder_text="Username", width=230, corner_radius=15)
    username_entry.pack(pady=(10, 5))

    password_entry = customtkinter.CTkEntry(signup_frame, placeholder_text="Password", width=230, corner_radius=15, show="*")
    password_entry.pack(pady=(10, 5))

    confirm_password_entry = customtkinter.CTkEntry(signup_frame, placeholder_text="Confirm Password", width=230, corner_radius=15, show="*")
    confirm_password_entry.pack(pady=(10, 20))

    error_label = customtkinter.CTkLabel(signup_frame, text="", text_color="red")
    error_label.pack()

# ========== Creating Account ==========
    def create_account():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if not username or not password or not confirm_password:
            error_label.configure(text="Please fill in all fields!", text_color="red")
            return

        if not valid_username(username):
            error_label.configure(text="Invalid username. Use 4+ letters/numbers/underscores.", text_color="red")
            return

        if not strong_password(password):
            error_label.configure(text="Weak password. Must be 6+ chars with upper, lower, number, symbol.", text_color="red")
            return

        if password != confirm_password:
            error_label.configure(text="Passwords don't match!", text_color="red")
            return

        if save_account(username, password):
            error_label.configure(text="Account created!", text_color="green")
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            confirm_password_entry.delete(0, 'end')
        else:
            error_label.configure(text="Username already exists!", text_color="red")

    main.bind('<Return>', lambda event: create_account()) # Bind Enter key to create account

    create_account_button = customtkinter.CTkButton(signup_frame, text="Create Account", corner_radius=20, text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e', command=create_account)
    create_account_button.pack(pady=(5, 10))

    go_back_button = customtkinter.CTkButton(signup_frame, text="Go back", corner_radius=20, text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e', command=login_page)
    go_back_button.pack()

# ========== Dashboard ==========
def Dashboard():
    clear_frame()
    main.title("TryQuizMe")
    main.configure(fg_color="#010101")
    
    topbar = customtkinter.CTkFrame(main, fg_color="#353A3E",corner_radius=0,height=60)
    topbar.pack(pady=0, padx=10, fill="both")

    label = customtkinter.CTkLabel(topbar, text="TryQuizMe",font=('Arial',25))
    label.pack(pady=10,padx=(50,0), side='left')

    label = customtkinter.CTkLabel(topbar, text=current_user, font=('Arial',18))
    label.pack(pady=10,padx=(0,30), side='right')

    background = customtkinter.CTkFrame(main, fg_color="#f0f0f0",corner_radius=0,height=400)
    background.pack(pady=(0,10), padx=10, fill="both", expand=True)

    button = customtkinter.CTkButton(background, text="QuizMe", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A', command=quizMe)
    button.pack(pady=(170,5))

    button = customtkinter.CTkButton(background, text="Achievements", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A')
    button.pack(pady=(10,5))

    button = customtkinter.CTkButton(background, text="Leaderboards", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A')
    button.pack(pady=(10,5))

    button = customtkinter.CTkButton(background, text="Quit", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A', command=close_window)
    button.pack(pady=(10,5))

# Global lists for Create Quiz

isho_quiz_name_entry = None
isho_question_entries = []
isho_choice_entries = []
isho_correct_answers = []

# ========== QuizMe ==========
def quizMe():
    clear_frame()
    main.title("QuizMe")
    main.configure(fg_color="#010101")

    # ========== Difficulty ==========
    dashboard = customtkinter.CTkFrame(main, corner_radius=10, fg_color='#dee0e0', width=300)
    dashboard.pack(pady=(5,20), padx=10, fill="both",side='left')

    label = customtkinter.CTkLabel(dashboard,text="QuizMe",font=('Arial',35), text_color='#101010')
    label.pack(pady=(15,15), padx=70)

    label = customtkinter.CTkLabel(dashboard,text="Difficulty",font=('Arial',17), text_color='#101010')
    label.pack(pady=(25,0), padx=(0,135))

    difficulty = customtkinter.CTkFrame(dashboard, fg_color='#ebeded', border_width=1, border_color='#c9c9c9', height=230)
    difficulty.pack()

    for diff in ["All Difficulty", "Easy", "Medium", "Hard"]:
        button = customtkinter.CTkButton(difficulty, text=diff, anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010', hover_color='#4668f2')
        button.pack(pady=1, padx=1)

    label = customtkinter.CTkLabel(dashboard,text="Category",font=('Arial',17), text_color='#101010')
    label.pack(pady=(25,0), padx=(0,135))

    # ========== Category ========== 
    category = customtkinter.CTkFrame(dashboard, fg_color='#ebeded', border_width=1, border_color='#c9c9c9', height=230)
    category.pack(pady=0, padx=1)

    for cat in ["All Category", "General Skills", "Web Development", "Cryptography", "Python"]:
        button = customtkinter.CTkButton(category, text=cat, anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010', hover_color='#4668f2')
        button.pack(pady=1, padx=1)
    
    # ========== Create Quiz Function ========== 
    def isho_create_quiz_page():
        clear_frame()
        main.configure(fg_color="#1f2024")
        
        question_entries = []
        choice_entries = []
        correct_answers = []

        # links the local ones to global for saving later
        global isho_quiz_name_entry, isho_question_entries, isho_choice_entries, isho_correct_answers
        isho_question_entries = question_entries
        isho_choice_entries = choice_entries
        isho_correct_answers = correct_answers

        customtkinter.CTkLabel(main, text="Create Quiz", font=("Arial", 24)).pack(pady=10)
        customtkinter.CTkLabel(main, text="Enter Quiz Name:").pack()
        quiz_name_entry = customtkinter.CTkEntry(main, width=300)
        quiz_name_entry.pack(pady=5)
        isho_quiz_name_entry = quiz_name_entry

        questions_container = customtkinter.CTkScrollableFrame(main, width=1000, height=400)
        questions_container.pack(pady=10, fill="both", expand=True)
    
        # ========== Adding Questions ==========
        def add_question():
            frame = customtkinter.CTkFrame(questions_container)
            frame.pack(pady=15, fill="x", padx=20)

            q_entry = customtkinter.CTkEntry(frame, width=600, placeholder_text="Enter question")
            q_entry.pack(pady=4)

            choices = []
            for i in range(4):
                entry = customtkinter.CTkEntry(frame, width=500, placeholder_text=f"Choice {chr(65 + i)}")
                entry.pack(pady=5)
                choices.append(entry)

            correct_var = customtkinter.IntVar(value=0)
            for i in range(4):
                radiobuttn = customtkinter.CTkRadioButton(frame, text=f"Correct: Choice {chr(65+i)}", variable=correct_var, value=i)
                radiobuttn.pack(anchor="w", pady=5)

            question_entries.append(q_entry)
            choice_entries.append(choices)
            correct_answers.append(correct_var)
        
        # ========== Remove Last Questions ==========
        def remove_last_question():
            if question_entries:
                question_entries.pop().master.destroy()
                choice_entries.pop()
                correct_answers.pop()
        
        def save_quiz():
            name = isho_quiz_name_entry.get().strip()
            if not name:
                messagebox.showerror("Error", "Please enter a quiz name.")
                return

            wb = load_workbook(quiz_file)
            if name in wb.sheetnames:
                messagebox.showerror("Error", "Quiz already exists.")
                return

            sheet = wb.create_sheet(title=name)
            sheet.append(["Question", "ChoiceA", "ChoiceB", "ChoiceC", "ChoiceD", "CorrectIndex"])

            for q_entry, choices, correct in zip(isho_question_entries, isho_choice_entries, isho_correct_answers):
                question = q_entry.get().strip()
                choice_vals = [c.get().strip() for c in choices]
                sheet.append([question] + choice_vals + [correct.get()])

            wb.save(quiz_file)
            messagebox.showinfo("Success", "Quiz saved successfully!")

        button_row = customtkinter.CTkFrame(main)
        button_row.pack(pady=10)

        customtkinter.CTkButton(button_row, text="Add Question", command=add_question).pack(side="left", padx=5)
        customtkinter.CTkButton(button_row, text="Remove Last Question", command=remove_last_question).pack(side="left", padx=5)
        customtkinter.CTkButton(button_row, text="Save Quiz", command=save_quiz).pack(side="left", padx=5)

        add_question()
        
        back_button = customtkinter.CTkButton(main, text="Go Back", command=quizMe)
        back_button.pack(pady=5)

    # ========== Buttons ==========
    CreateQ = customtkinter.CTkButton(dashboard, text='Create Quiz', command=isho_create_quiz_page)
    CreateQ.pack(pady=(25,0))

    back = customtkinter.CTkButton(dashboard, text='Go Back', command=Dashboard)
    back.pack(pady=(25,0))

    # ========== Take Quiz Available ==========
    Quiz = customtkinter.CTkFrame(main, corner_radius=10, fg_color='#dee0e0')
    Quiz.pack(pady=(5,20), padx=(0,10), side='right', fill="both", expand=True)

    label = customtkinter.CTkLabel(Quiz, text="Available Quizzes", font=("Arial",20), text_color="#1f2024").pack()
    def load_quizzes():
        wb = load_workbook(quiz_file)
        excluded = ["template", "scores", "users", "sheet"]  # add any sheet you want to ignore

        for sheet_name in wb.sheetnames:
            if sheet_name.lower() in excluded:
                continue

            quiz_button = customtkinter.CTkButton(
                Quiz, 
                text=sheet_name, 
                command=lambda name=sheet_name: take_quiz(name),
                fg_color="#ffffff", 
                text_color="#101010", 
                hover_color="#4668f2"
            )
            quiz_button.pack(pady=5)

    def take_quiz(quiz_name):
        clear_frame()
        main.title(f"Taking Quiz: {quiz_name}")

        wb = load_workbook(quiz_file)
        sheet = wb[quiz_name]

        questions = []
        for row in sheet.iter_rows(min_row=2, values_only=True):  # skip header
            question_text = row[0]
            choices = row[1:5]
            correct = row[5]
            questions.append((question_text, choices, correct))

        user_answers = []
        index = [0]  # use list to allow mutability inside nested functions

        question_frame = customtkinter.CTkFrame(main)
        question_frame.pack(pady=10, padx=10)

        question_label = customtkinter.CTkLabel(question_frame, text="", font=("Arial", 18))
        question_label.pack(pady=10)

        choice_vars = []
        radio_var = customtkinter.IntVar()

        for i in range(4):
            btn = customtkinter.CTkRadioButton(question_frame, text="", variable=radio_var, value=i)
            btn.pack(anchor="w", pady=2)
            choice_vars.append(btn)

        def load_question():
            q, choices, _ = questions[index[0]]
            question_label.configure(text=q)
            for i, choice in enumerate(choices):
                choice_vars[i].configure(text=choice)
            radio_var.set(-1)

        def next_question():
            if radio_var.get() == -1:
                messagebox.showerror("Error", "Select an answer before continuing!")
                return
            user_answers.append(radio_var.get())
            index[0] += 1
            if index[0] < len(questions):
                load_question()
            else:
                show_results()

        def show_results():
            score = 0
            for (q, _, correct), user_ans in zip(questions, user_answers):
                if user_ans == correct:
                    score += 1

            clear_frame()
            result_text = f"You scored {score} out of {len(questions)}"
            customtkinter.CTkLabel(main, text=result_text, font=("Arial", 24)).pack(pady=20)
            customtkinter.CTkButton(main, text="Back to Quizzes", command=quizMe).pack()

        customtkinter.CTkButton(question_frame, text="Next", command=next_question).pack(pady=10)
        load_question()
    load_quizzes()

# ========== Start ==========
initialize_database()
login_page()

main.mainloop()