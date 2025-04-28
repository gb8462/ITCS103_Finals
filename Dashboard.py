import customtkinter

main = customtkinter.CTk()
main.geometry("1100x680")

main.configure(fg_color="#010101")

def clear_frame():
    """Clear all widgets in the login_frame."""
    for widget in main.winfo_children():
        widget.destroy()
def close_window():
    main.destroy()

def quizMe():
    clear_frame()
    main.title("QuizMe")
    customtkinter.set_appearance_mode("dark")

    main.configure(fg_color="#010101")

    # Dashboard
    dashboard = customtkinter.CTkFrame(main, corner_radius=10,fg_color='#dee0e0',width=300)
    dashboard.pack(pady=(5,20), padx=10, fill="both",side='left')

    label = customtkinter.CTkLabel(dashboard,text="QuizMe",font=('Arial',35), text_color='#101010')
    label.pack(pady=(15,15), padx=70)

    label = customtkinter.CTkLabel(dashboard,text="Difficulty",font=('Arial',17), text_color='#101010')
    label.pack(pady=(25,0), padx=(0,135))


    # Difficulty
    difficulty = customtkinter.CTkFrame(dashboard, fg_color='#ebeded', border_width=1, border_color='#c9c9c9', height=230)
    difficulty.pack()

    button = customtkinter.CTkButton(difficulty, text="All Difficulty", anchor='w', height=35,corner_radius=0,width=200,fg_color='#ffffff', text_color='#101010')
    button.pack(pady=1, padx=1)

    button = customtkinter.CTkButton(difficulty, text="Easy", anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010')
    button.pack(pady=1, padx=1)

    button = customtkinter.CTkButton(difficulty, text="Medium", anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010')
    button.pack(pady=1, padx=1)

    button = customtkinter.CTkButton(difficulty, text="Hard", anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010')
    button.pack(pady=1, padx=1)


    # Category
    label = customtkinter.CTkLabel(dashboard,text="Category",font=('Arial',17), text_color='#101010')
    label.pack(pady=(25,0), padx=(0,135))

    category = customtkinter.CTkFrame(dashboard, fg_color='#ebeded', border_width=1, border_color='#c9c9c9',height=230)
    category.pack(pady=0, padx=1)

    button = customtkinter.CTkButton(category, text="All Category", anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010')
    button.pack(pady=1, padx=1)

    button = customtkinter.CTkButton(category, text="General Skills", anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010')
    button.pack(pady=1, padx=1)

    button = customtkinter.CTkButton(category, text="Web Development", anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010')
    button.pack(pady=1, padx=1)

    button = customtkinter.CTkButton(category, text="Cryptography", anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010')
    button.pack(pady=1, padx=1)

    button = customtkinter.CTkButton(category, text="Python", anchor='w', height=35, corner_radius=0, width=200, fg_color='#ffffff', text_color='#101010')
    button.pack(pady=1, padx=1)

    button = customtkinter.CTkButton(dashboard, text='Go Back', command=Dashboard)
    button.pack(pady=(25,0))

    # Quizzes
    Quiz = customtkinter.CTkFrame(main, corner_radius=10,fg_color='#dee0e0')
    Quiz.pack(pady=(5,20), padx=(0,10), side='right',fill="both", expand=True)


def Dashboard():
    clear_frame()
    main.title("TryQuizMe")
    customtkinter.set_appearance_mode("dark")
    
    # TopBar
    topbar = customtkinter.CTkFrame(main, fg_color="#353A3E",corner_radius=0,height=60)
    topbar.pack(pady=0, padx=10, fill="both")

    label = customtkinter.CTkLabel(topbar, text="TryQuizMe",font=('Arial',25))
    label.pack(pady=10,padx=(50,0), side='left')

    label = customtkinter.CTkLabel(topbar, text="username",font=('Arial',18))
    label.pack(pady=10,padx=(0,30), side='right')

    # Dashboard
    background = customtkinter.CTkFrame(main, fg_color="#f0f0f0",corner_radius=0,height=400)
    background.pack(pady=(0,10), padx=10, fill="both", expand=True)

    button = customtkinter.CTkButton(background, text="QuizMe", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A',command=quizMe)
    button.pack(pady=(170,5))

    button = customtkinter.CTkButton(background, text="Achievements", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A')
    button.pack(pady=(10,5))

    button = customtkinter.CTkButton(background, text="Leaderboards", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A')
    button.pack(pady=(10,5))

    button = customtkinter.CTkButton(background, text="Quit", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0', hover_color='#1A1A1A', command=close_window)
    button.pack(pady=(10,5))

Dashboard()

main.mainloop()