import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Label Example")
root.geometry("300x200")  # Width x Height

# Create a label widget
label = tk.Label(root, text="this is thirumal", font=("Arial", 14))

# Position the label on the window
label.pack(pady=20)  # pady adds vertical padding

# Run the application
root.mainloop()
