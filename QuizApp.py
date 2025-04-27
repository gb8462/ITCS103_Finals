import customtkinter

main = customtkinter.CTk()
main.title("TryQuizMe")
main.geometry("1100x680")
customtkinter.set_appearance_mode("dark")

main.configure(fg_color="#010101")

topbar = customtkinter.CTkFrame(main, fg_color="#252525",corner_radius=0,height=60)
topbar.pack(pady=0, padx=10, fill="both")

background = customtkinter.CTkFrame(main, fg_color="#E0E0E0",corner_radius=0,height=400)
background.pack(pady=(0,10), padx=10, fill="both", expand=True)

# Dashboard


main.mainloop()