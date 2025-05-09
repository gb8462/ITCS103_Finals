import tkinter as tk
import customtkinter
import openpyxl
import hashlib, os, re 
from tkinter import messagebox
from tkinter import ttk
from openpyxl import Workbook, load_workbook

main = customtkinter.CTk()
main.title("TryQuizMe login")
main.geometry("1100x680")
customtkinter.set_appearance_mode('dark')

main.configure(fg_color="#1f2024")


quiz_file = "quizzes.xlsx"
if not os.path.exists(quiz_file):
    wb = Workbook()
    sheet = wb.active
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

    def on_create_account():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        if password != confirm_password:
            error_label.configure(text="Passwords do not match!")
            return

        if save_account(username, password):
            messagebox.showinfo("Success", "Account created successfully!")
            login_page()  # Navigate back to the login page after successful sign-up
        else:
            error_label.configure(text="Username already exists!")

    # Create Account button
    create_account_button = customtkinter.CTkButton(signup_frame, text="Create Account", corner_radius=20, text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e', command=on_create_account)
    create_account_button.pack(pady=(0, 5))

    # Back to Login button
    back_button = customtkinter.CTkButton(signup_frame, text="Back to Login", corner_radius=20, text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e', command=login_page)
    back_button.pack(pady=(5, 20))

# ========== Creating Account ==========
def Leaderboard():
    clear_frame()
    main.title("TryQuizMe")
    main.configure(fg_color="#010101")

    frame = customtkinter.CTkFrame(main, fg_color="#353A3E", corner_radius=0)
    frame.pack(fill='both', expand=True)

    title = customtkinter.CTkLabel(frame, text="🏆 Leaderboard", font=("Arial", 32), text_color="#ffffff")
    title.pack(pady=(30, 10))

    tree_frame = customtkinter.CTkFrame(frame, fg_color="#2e2f33", corner_radius=15)
    tree_frame.pack(padx=60, pady=20, fill="both", expand=True)

    style = ttk.Style()
    style.theme_use("default")
    style.configure("Treeview", background="#2e2f33", foreground="#f2f2f2", rowheight=30, fieldbackground="#2e2f33", font=("Arial", 12))
    style.configure("Treeview.Heading", font=("Arial", 16, "bold"), background="#353A3E", foreground="#ffffff")
    style.map("Treeview", background=[('selected', '#353A3E')], foreground=[('selected', '#ffffff')])

    tree = ttk.Treeview(tree_frame, columns=("Rank", "Username", "Score"), show="headings", selectmode="none")
    tree.heading("Rank", text="Rank")
    tree.heading("Username", text="Username")
    tree.heading("Score", text="Score")
    tree.column("Rank", anchor="center", width=80)
    tree.column("Username", anchor="w", width=200)
    tree.column("Score", anchor="center", width=100)

    tree.pack(fill="both", expand=True, padx=20, pady=20)

    # Insert data
    try:
        wb = openpyxl.load_workbook("users.xlsx")
        sheet = wb.active

        users_data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            username = row[0]
            score = row[2] if len(row) > 2 and isinstance(row[2], int) else 0
            users_data.append((username, score))

        users_data.sort(key=lambda x: x[1], reverse=True)

        for index, (username, score) in enumerate(users_data, start=1):
            tree.insert("", "end", values=(index, username, score))

    except Exception as e:
        messagebox.showerror("Error", f"Failed to load leaderboard: {e}")

    customtkinter.CTkButton(frame, text="Back to Dashboard", command=Dashboard, fg_color="#4668f2", hover_color="#314ad1", text_color="#fff",font=("Arial", 14), corner_radius=8, width=180).pack(pady=(0, 20))
# ========== Dashboard ==========
def Dashboard():
    clear_frame()
    main.title("TryQuizMe")
    main.configure(fg_color="#010101")
    
    topbar = customtkinter.CTkFrame(main, fg_color="#353A3E",corner_radius=0,height=60)
    topbar.pack(pady=0, padx=0, fill="both")

    label = customtkinter.CTkLabel(topbar, text="TryQuizMe",font=('Arial',25))
    label.pack(pady=10,padx=(50,0), side='left')

    label = customtkinter.CTkLabel(topbar, text=current_user, font=('Arial',18))
    label.pack(pady=10,padx=(0,30), side='right')

    background = customtkinter.CTkFrame(main, fg_color="#f0f0f0",corner_radius=0,height=400)
    background.pack(pady=(0,10), padx=0, fill="both", expand=True)

    button = customtkinter.CTkButton(background, text="QuizMe", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A', command=quizMe)
    button.pack(pady=(170,5))

    button = customtkinter.CTkButton(background, text="Achievements", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A')
    button.pack(pady=(10,5))

    button = customtkinter.CTkButton(background, text="Leaderboards", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A', command=Leaderboard)
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
    Quiz.pack(pady=(5, 20), padx=(0, 10), side='right', fill="both", expand=True)

    label = customtkinter.CTkLabel(Quiz, text="Available Quizzes", font=("Arial", 20), text_color="#1f2024")
    label.pack()

    def load_quizzes():
        try:
            wb = load_workbook(quiz_file)
            excluded = ["template", "scores", "users", "sheet"]  # Make sure "Sheet" is in lowercase to avoid case issues

            for sheet_name in wb.sheetnames:
                normalized_sheet_name = sheet_name.strip().lower()  # Normalize to lowercase and remove leading/trailing spaces
                
                if normalized_sheet_name in excluded:
                    continue

                quiz_button = customtkinter.CTkButton(Quiz, text=sheet_name, command=lambda name=sheet_name: take_quiz(name), fg_color="#4668f2", hover_color="#314ad1", text_color="#fff", font=("Arial", 16), width=200, height=35, corner_radius=12)
                quiz_button.pack(pady=8)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load quizzes: {e}")

    def take_quiz(quiz_name):
        clear_frame()
        main.configure(fg_color="#1f2024")
        customtkinter.CTkLabel(main, text=f"{quiz_name} Quiz", font=("Arial", 28), text_color="#ffffff").pack(pady=20)

        quiz_frame = customtkinter.CTkScrollableFrame(main, width=800, height=500, fg_color="#2a2b2e")
        quiz_frame.pack(pady=10)

        wb = load_workbook(quiz_file)
        sheet = wb[quiz_name]

        selected_answers, valid_rows = [], []

        for i, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), 1):
            if not row or len(row) < 6:
                print(f"⚠️ Skipping row {i} due to wrong length: {row}")
                continue

            q_text, choice_a, choice_b, choice_c, choice_d, correct_index = row[:6]
            choices = [choice_a, choice_b, choice_c, choice_d]
            valid_rows.append((i, correct_index))

            customtkinter.CTkLabel(quiz_frame, text=f"Q{i}: {q_text}", font=("Arial", 18), text_color="#ffffff", wraplength=700, justify="left").pack(anchor="w", pady=(15, 5), padx=20)

            var = customtkinter.IntVar(value=-1)
            selected_answers.append(var)

            for idx, choice in enumerate(choices):
                if choice is None:
                    continue
                customtkinter.CTkRadioButton(quiz_frame, text=choice, variable=var, value=idx, text_color="#ccc", hover_color="#4668f2", fg_color="#1a1b1e", font=("Arial", 14)).pack(anchor="w", padx=40, pady=2)

            ttk.Separator(quiz_frame, orient="horizontal").pack(fill="x", pady=10, padx=20)

        def submit_answers():
            score, total = 0, len(selected_answers)

            for i, (row_idx, correct) in enumerate(valid_rows):
                if selected_answers[i].get() == correct:
                    score += 1

            messagebox.showinfo("Quiz Result", f"You got {score} out of {total} correct!")

            try:
                user_wb = openpyxl.load_workbook("users.xlsx")
                user_sheet = user_wb.active

                headers = [cell.value for cell in user_sheet[1]]
                
                # If "Score" column doesn't exist, add it
                if "Score" not in headers:
                    user_sheet.cell(row=1, column=len(headers) + 1, value="Score")
                    score_col_index = len(headers) + 1
                else:
                    score_col_index = headers.index("Score") + 1

                # Find the row for the current user and update the score
                for row in user_sheet.iter_rows(min_row=2):
                    if row[0].value == current_user:
                        user_sheet.cell(row=row[0].row, column=score_col_index, value=score)
                        break

                user_wb.save("users.xlsx")

            except Exception as e:
                messagebox.showerror("Error", f"Failed to save score: {e}")

        customtkinter.CTkButton(main, text="Submit Quiz", command=submit_answers, fg_color="#4668f2", hover_color="#314ad1", font=("Arial", 16), corner_radius=10, width=200).pack(pady=15)
        customtkinter.CTkButton(main, text="Go Back", command=quizMe, fg_color="#6c6c6c", hover_color="#3a3a3a", font=("Arial", 14), corner_radius=10, width=150).pack(pady=5)

    load_quizzes()

# ========== Start ==========
initialize_database()
login_page()

main.mainloop()