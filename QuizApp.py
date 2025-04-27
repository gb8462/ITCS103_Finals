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

label = customtkinter.CTkLabel(dashboard,text="Difficulty",font=('Arial',17), text_color='#101010')
label.pack(pady=(25,0), padx=70)

difficulty = customtkinter.CTkFrame(dashboard, fg_color='#ebeded', border_width=1, border_color='gray',height=230)
difficulty.pack(pady=0, padx=1)

label = customtkinter.CTkLabel(dashboard,text="Category",font=('Arial',17), text_color='#101010')
label.pack(pady=(25,0), padx=70)

category = customtkinter.CTkFrame(dashboard, fg_color='#ebeded', border_width=1, border_color='gray',height=230)
category.pack(pady=0, padx=1)

sideboard = customtkinter.CTkFrame(main, corner_radius=10,fg_color='#dee0e0')
sideboard.pack(pady=(5,20), padx=(0,10), side='right',fill="both", expand=True)


main.mainloop()