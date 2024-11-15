import tkinter as tk
import random
import string

# Function to generate random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function called when the "Generate" button is clicked
def on_generate():
    try:
        length = int(length_entry.get())  # Get length from user input
        if length < 1:
            result_label.config(text="Password length must be at least 1.")
        else:
            password = generate_random_password(length)
            result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        result_label.config(text="Please enter a valid number for length.")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Set up the layout of the window
tk.Label(root, text="Enter password length:").grid(row=0, column=0, padx=10, pady=10)

# Entry box to input password length
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
generate_button = tk.Button(root, text="Generate", command=on_generate)
generate_button.grid(row=1, columnspan=2, pady=10)

# Label to display the generated password
result_label = tk.Label(root, text="Generated Password: ", width=50, height=2, relief="solid")
result_label.grid(row=2, columnspan=2, pady=10)

# Start the GUI loop
root.mainloop()
