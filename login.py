import tkinter as tk
from tkinter import messagebox

# Function to handle login button click
def login():
    email = email_var.get()
    password = password_var.get()

    # Add your login logic here (e.g., check against the database)
    # For demonstration, we'll show a messagebox
    messagebox.showinfo("Login", f"Email: {email}\nPassword: {password}")

# Function to open the registration page
def open_register_page():
    register_window = tk.Toplevel(root)
    register_window.title("Register")

    # Create labels and entry widgets for registration
    tk.Label(register_window, text="First Name:").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(register_window, text="Last Name:").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(register_window, text="Email:").grid(row=2, column=0, padx=10, pady=5)
    tk.Label(register_window, text="Password:").grid(row=3, column=0, padx=10, pady=5)
    tk.Label(register_window, text="Phone Number:").grid(row=4, column=0, padx=10, pady=5)

    first_name_entry = tk.Entry(register_window)
    last_name_entry = tk.Entry(register_window)
    email_entry = tk.Entry(register_window)
    password_entry = tk.Entry(register_window, show="*")
    phone_entry = tk.Entry(register_window)

    first_name_entry.grid(row=0, column=1, padx=10, pady=5)
    last_name_entry.grid(row=1, column=1, padx=10, pady=5)
    email_entry.grid(row=2, column=1, padx=10, pady=5)
    password_entry.grid(row=3, column=1, padx=10, pady=5)
    phone_entry.grid(row=4, column=1, padx=10, pady=5)

    # Function to handle registration button click
    def register():
        # Get values from entry widgets
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        phone = phone_entry.get()

        # Add your registration logic here (e.g., store in the database)
        # For demonstration, we'll show a messagebox
        messagebox.showinfo("Registration", f"Registration Successful!\nEmail: {email}")

    # Create a registration button
    tk.Button(register_window, text="Register", command=register).grid(row=5, column=1, pady=10)

# Main window
root = tk.Tk()
root.title("Login")

# Create labels and entry widgets for login
tk.Label(root, text="Email:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)

email_var = tk.StringVar()
password_var = tk.StringVar()

email_entry = tk.Entry(root, textvariable=email_var)
password_entry = tk.Entry(root, textvariable=password_var, show="*")

email_entry.grid(row=0, column=1, padx=10, pady=5)
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create a login button
tk.Button(root, text="Login", command=login).grid(row=2, column=1, pady=10)

# Create a link to the registration page
tk.Label(root, text="Not registered?").grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Register", command=open_register_page).grid(row=3, column=2)

# Run the main loop
root.mainloop()
