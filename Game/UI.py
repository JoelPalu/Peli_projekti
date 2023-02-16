import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("User Interface")

# Define a function to handle button clicks
def button_click():
    print("Button clicked!")

# Create a label
label = tk.Label(root, text="This is a label")
label.pack()

# Create a button
button = tk.Button(root, text="Click me", command=button_click)
button.pack()

# Start the main event loop
root.mainloop()