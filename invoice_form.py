import tkinter as tk
from tkinter import messagebox

# Dummy user database (in-memory)
users = {}

# Sign-Rp Window
def sign_up():
    def register():
        username = entry_user.get()
        password = entry_pass.get()
        if username in users:
            messagebox.showerror("Error", "User already exists!")
        else:
            users[username] = password
            messagebox.showinfo("Success", "Registered successfully!")
            signup_window.destroy()

    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    tk.Label(signup_window, text="Username").pack()
    entry_user = tk.Entry(signup_window)
    entry_user.pack()

    tk.Label(signup_window, text="Password").pack()
    entry_pass = tk.Entry(signup_window, show='*')
    entry_pass.pack()

    tk.Button(signup_window, text="Register", command=register).pack()

# Invoice Window
def open_invoice_form():
    def calculate():
        try:
            quantity = int(entry_qty.get())
            price = float(entry_price.get())
            total = quantity * price
            label_total.config(text=f"Total: ${total:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Enter valid numbers")

    invoice = tk.Toplevel(root)
    invoice.title("Invoice Form")

    tk.Label(invoice, text="Customer Name").pack()
    entry_name = tk.Entry(invoice)
    entry_name.pack()

    tk.Label(invoice, text="Item").pack()
    entry_item = tk.Entry(invoice)
    entry_item.pack()

    tk.Label(invoice, text="Quantity").pack()
    entry_qty = tk.Entry(invoice)
    entry_qty.pack()

    tk.Label(invoice, text="Price per Item").pack()
    entry_price = tk.Entry(invoice)
    entry_price.pack()

    tk.Button(invoice, text="Calculate Total", command=calculate).pack()
    label_total = tk.Label(invoice, text="Total: $0.00")
    label_total.pac

# Sign-In Function
def sign_in():
    username = entry_username.get()
    password = entry_password.get()
    if users.get(username) == password:
        messagebox.showinfo("Success", "Login successful!")
        open_invoice_form()
    else:
        messagebox.showerror("Failed", "Invalid credentials")

# Main window
root = tk.Tk()
root.title("Sign In / Sign Up")

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show='*')
entry_password.pack()

tk.Button(root, text="Sign In", command=sign_in).pack()
tk.Button(root, text="Sign Up", command=sign_up).pack()

root.mainloop()