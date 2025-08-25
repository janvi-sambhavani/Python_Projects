import tkinter as tk
from tkinter import messagebox
from fpdf import FPDF
import os

# Sample medicine price list
medicine_prices = {
    "Medicine A": 10,
    "Medicine B": 20,
    "Medicine C": 15,
    "Medicine D": 25
}

# Store added items
cart = []

# Add selected medicine and quantity to the cart
def add_medicine():
    try:
        selection = listbox.curselection()
        if not selection:
            raise ValueError("No medicine selected.")
        
        medicine = listbox.get(selection)
        quantity_text = quantity_entry.get()

        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            raise ValueError("Invalid quantity.")
        
        quantity = int(quantity_text)
        price = medicine_prices[medicine]
        total = price * quantity

        cart.append({
            "medicine": medicine,
            "quantity": quantity,
            "price": price,
            "total": total
        })

        update_total()
        quantity_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Please select a medicine and enter a valid quantity.\n\nDetails: {e}")

# Update total amount label
def update_total():
    total_amount = sum(item['total'] for item in cart)
    total_amount_var.set(f"Rs. {total_amount:.2f}")

# Generate invoice as PDF
def generate_invoice():
    customer_name = customer_name_entry.get().strip()

    if not customer_name:
        messagebox.showerror("Error", "Customer name is required.")
        return

    if not cart:
        messagebox.showerror("Error", "Please add at least one medicine to the cart.")
        return

    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, f"Invoice for {customer_name}", ln=True, align="C")
        pdf.set_font("Arial", size=12)
        pdf.ln(10)

        # Table headers
        pdf.cell(60, 10, "Medicine", border=1)
        pdf.cell(30, 10, "Quantity", border=1)
        pdf.cell(30, 10, "Price", border=1)
        pdf.cell(30, 10, "Total", border=1)
        pdf.ln()

        total_price = 0
        for item in cart:
            pdf.cell(60, 10, item['medicine'], border=1)
            pdf.cell(30, 10, str(item['quantity']), border=1)
            pdf.cell(30, 10, f"Rs. {item['price']}", border=1)
            pdf.cell(30, 10, f"Rs. {item['total']}", border=1)
            pdf.ln()
            total_price += item['total']

        pdf.ln(5)
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(60, 10, f"Total Amount: Rs. {total_price:.2f}", ln=True)

        filename = f"invoice_{customer_name.replace(' ', '_')}.pdf"
        save_path = os.path.join(os.getcwd(), filename)
        pdf.output(save_path)

        messagebox.showinfo("Invoice Generated", f"Invoice saved as:\n{save_path}")

        # Reset
        cart.clear()
        total_amount_var.set("")
        customer_name_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate invoice.\n\nDetails: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("Invoice Generator")
root.geometry("400x500")
root.configure(bg="#2e2e2e")

tk.Label(root, text="Medicine:", fg="white", bg="#2e2e2e", font=("Arial", 12)).pack()

# Listbox for medicine selection
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=5, bg="black", fg="white")
for med in medicine_prices.keys():
    listbox.insert(tk.END, med)
listbox.pack(pady=5)

tk.Label(root, text="Quantity:", fg="white", bg="#2e2e2e", font=("Arial", 12)).pack()
quantity_entry = tk.Entry(root, bg="black", fg="white")
quantity_entry.pack(pady=5)

tk.Button(root, text="Add Medicine", command=add_medicine, bg="white", fg="black").pack(pady=10)

tk.Label(root, text="Total Amount:", fg="white", bg="#2e2e2e", font=("Arial", 12)).pack()
total_amount_var = tk.StringVar()
total_amount_entry = tk.Entry(root, textvariable=total_amount_var, state="readonly", bg="black", fg="white")
total_amount_entry.pack(pady=5)

tk.Label(root, text="Customer Name:", fg="white", bg="#2e2e2e", font=("Arial", 12)).pack()
customer_name_entry = tk.Entry(root, bg="black", fg="white")
customer_name_entry.pack(pady=5)

tk.Button(root, text="Generate Invoice", command=generate_invoice, bg="white", fg="black").pack(pady=20)

root.mainloop()



