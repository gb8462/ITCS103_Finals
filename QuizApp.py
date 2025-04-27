import customtkinter

main = customtkinter.CTk()
main.title("TryQuizMe")
main.geometry("1090x680")
customtkinter.set_appearance_mode("dark")

main.configure(fg_color="#010101")

sideboard = customtkinter.CTkFrame(main, corner_radius=10,fg_color='#1f2024')
sideboard.pack(pady=(5,20), padx=(0,10), side='right',fill="both", expand=True)

dashboard = customtkinter.CTkFrame(main, corner_radius=10,fg_color='#edeff0',width=300)
dashboard.pack(pady=(5,20), padx=10, fill="both",side='right')


main.mainloop()