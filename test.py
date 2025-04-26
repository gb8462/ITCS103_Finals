import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Exit Button Example")

# Function to close the window
def close_window():
    root.destroy()

# Create the exit button
exit_button = tk.Button(root, text="Exit", command=close_window)
exit_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()