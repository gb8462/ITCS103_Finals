import customtkinter

main = customtkinter.CTk()
main.title("TryQuizMe")
main.geometry("1100x680")
customtkinter.set_appearance_mode("dark")

main.configure(fg_color="#010101")


dashboard = customtkinter.CTkFrame(main, corner_radius=10,fg_color='#dee0e0',width=300)
dashboard.pack(pady=(5,20), padx=10, fill="both",side='left')

label = customtkinter.CTkLabel(dashboard,text="QuizMe",font=('Arial',35), text_color='#101010')
label.pack(pady=(15,15), padx=70)

label = customtkinter.CTkLabel(dashboard,text="Difficulty",font=('Arial',18), text_color='#101010')
label.pack(pady=(30,5), padx=70)


sideboard = customtkinter.CTkFrame(main, corner_radius=10,fg_color='#dee0e0')
sideboard.pack(pady=(5,20), padx=(0,10), side='right',fill="both", expand=True)


main.mainloop()