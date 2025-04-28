import customtkinter

main = customtkinter.CTk()
main.title("TryQuizMe")
main.geometry("1100x680")
customtkinter.set_appearance_mode("dark")

main.configure(fg_color="#010101")

# TopBar
topbar = customtkinter.CTkFrame(main, fg_color="#353A3E",corner_radius=0,height=60)
topbar.pack(pady=0, padx=10, fill="both")

label = customtkinter.CTkLabel(topbar, text="TryQuizMe",font=('Arial',25))
label.pack(pady=10,padx=(50,0), side='left')

label = customtkinter.CTkLabel(topbar, text="username",font=('Arial',22))
label.pack(pady=10,padx=(0,30), side='right')

# Dashboard
background = customtkinter.CTkFrame(main, fg_color="#f0f0f0",corner_radius=0,height=400)
background.pack(pady=(0,10), padx=10, fill="both", expand=True)

button = customtkinter.CTkButton(background, text="QuizMe", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0')
button.pack(pady=(170,5))

button = customtkinter.CTkButton(background, text="Achievements", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0')
button.pack(pady=(10,5))

button = customtkinter.CTkButton(background, text="Leaderboards", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0')
button.pack(pady=(10,5))

button = customtkinter.CTkButton(background, text="Quit", corner_radius=3, width=350, height=40, font=('Arial',20), fg_color='#353A3E',text_color='#E0E0E0')
button.pack(pady=(10,5))

main.mainloop()