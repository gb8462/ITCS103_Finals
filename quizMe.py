import customtkinter

main = customtkinter.CTk()
main.title("QuizMe")
main.geometry("1100x680")
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

# Quizzes
Quiz = customtkinter.CTkFrame(main, corner_radius=10,fg_color='#dee0e0')
Quiz.pack(pady=(5,20), padx=(0,10), side='right',fill="both", expand=True)


main.mainloop()