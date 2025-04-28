import customtkinter

main = customtkinter.CTk()
main.title("TryQuizMe login")
main.geometry("1090x680")
customtkinter.set_appearance_mode("dark")

main.configure(fg_color="#1f2024")

login_frame = customtkinter.CTkFrame(main, corner_radius=20)
login_frame.pack(pady=100, padx=300, fill="both", expand=True)

# For Clearing the widgets

def clear_frame():
    """Clear all widgets in the login_frame."""
    for widget in login_frame.winfo_children():
        widget.destroy()


def login():
    clear_frame()

    login_frame.configure(fg_color="#35373d") 

    label = customtkinter.CTkLabel(login_frame, text="Login", fg_color="transparent", font=("Arial", 75))
    label.pack(pady=(60, 20))

    username_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Username", width=230, corner_radius=15)
    username_entry.pack(pady=(10, 5))

    password_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Password", width=230, corner_radius=15, show="*")
    password_entry.pack(pady=(10, 20))

    login_button = customtkinter.CTkButton(login_frame, text="Login", corner_radius=20, text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e')
    login_button.pack()

    label = customtkinter.CTkLabel(login_frame, text='or', fg_color='transparent', font=('Arial',12))
    label.pack()

    create_account_button = customtkinter.CTkButton(login_frame, text="Sign up", corner_radius=20, text_color='#e4e6ed', command=signUp, hover_color='#1A1A1A', fg_color='#5f626e')
    create_account_button.pack()

def signUp():
    clear_frame()

    login_frame.configure(fg_color="#35373d") 

    label = customtkinter.CTkLabel(login_frame, text="Sign-Up", fg_color="transparent", font=("Arial", 75))
    label.pack(pady=(60, 20))

    username_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Username", width=230, corner_radius=15)
    username_entry.pack(pady=(10, 5))

    password_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Password", width=230, corner_radius=15, show="*")
    password_entry.pack(pady=(10, 5))

    confirm_password_entry = customtkinter.CTkEntry(login_frame, placeholder_text="Confirm Password", width=230, corner_radius=15, show="*")
    confirm_password_entry.pack(pady=(10, 20))

    create_account_button = customtkinter.CTkButton(login_frame, text="Create Account", corner_radius=20,text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e')
    create_account_button.pack(pady=(5, 10))

    go_back_button = customtkinter.CTkButton(login_frame, text="Go back", corner_radius=20, width=20, text_color='#e4e6ed', hover_color='#1A1A1A', fg_color='#5f626e', command=login)
    go_back_button.pack()

login()
main.mainloop()