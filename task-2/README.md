💊 Tkinter Invoice Generator
📖 Description

A simple Invoice Generator GUI built using Python’s Tkinter library.
The application allows users to:

Select medicines,

Enter quantity,

Add customer details,

Display a basic invoice inside the app window.

This project demonstrates GUI design in Tkinter and is useful as a beginner-level billing/invoice system.

⚙️ Setup Instructions

Make a directory for the project and navigate into it

mkdir tkinter_invoice_generator && cd tkinter_invoice_generator


Create a Python virtual environment (optional)

python -m venv venv
# Activate
venv\Scripts\activate      # Windows  
source venv/bin/activate   # Linux/Mac


No external libraries required (Tkinter is included with Python).

Save the script as invoice.py

Run the application

python invoice.py

📂 Project Files

invoice.py → Main Tkinter GUI script for the Invoice Generator.

README.md → Documentation file.

🔑 Features

Input medicine name from a listbox.

Enter quantity and calculate total amount (manual entry).

Add customer name.

Generate and display invoice details in a Text widget.

🖼️ GUI Components

Medicine Listbox → Choose/select a medicine.

Quantity Entry → Input quantity for the medicine.

Total Amount Entry → Enter total amount (currently manual).

Customer Name Entry → Add customer details.

Generate Invoice Button → Create invoice and display in text area.

Invoice Display Area (Text widget) → Shows invoice details.

📸 Example Invoice (Displayed in Text Box)
Customer: Riya
Medicine: Paracetamol
Quantity: 2
Total Amount: ₹50
