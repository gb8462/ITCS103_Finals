import customtkinter

main = customtkinter.CTk()
main.title("TryQuizMe login")
main.geometry("1100x680")
customtkinter.set_appearance_mode("dark")

main.configure(fg_color="#1f2024")

# ========== Clear Frame Function ==========
def clear_frame():
    """Clear all widgets in the main window."""
    for widget in main.winfo_children():
        widget.destroy()

# ========== Login Page ==========
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

    def on_login():
        Dashboard()

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

    create_account_button = customtkinter.CTkButton(signup_frame, text="Create Account", corner_radius=20,text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e')
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

    label = customtkinter.CTkLabel(topbar, text="username",font=('Arial',18))
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

# ========== QuizMe ==========
def quizMe():
    clear_frame()
    main.title("QuizMe")
    main.configure(fg_color="#010101")

    dashboard = customtkinter.CTkFrame(main, corner_radius=10, fg_color='#dee0e0', width=300)
    dashboard.pack(pady=(5,20), padx=10, fill="both",side='left')

    label = customtkinter.CTkLabel(dashboard,text="QuizMe",font=('Arial',35), text_color='#101010')
    label.pack(pady=(15,15), padx=70)

    label = customtkinter.CTkLabel(dashboard,text="Difficulty",font=('Arial',17), text_color='#101010')
    label.pack(pady=(25,0), padx=(0,135))

# ========== Difficulty ==========
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

    button = customtkinter.CTkButton(dashboard, text='Go Back', command=Dashboard)
    button.pack(pady=(25,0))

    Quiz = customtkinter.CTkFrame(main, corner_radius=10, fg_color='#dee0e0')
    Quiz.pack(pady=(5,20), padx=(0,10), side='right', fill="both", expand=True)

# ========== Window Close ==========
def close_window():
    main.destroy()

# ========== Start ==========
login_page()

main.mainloop()
