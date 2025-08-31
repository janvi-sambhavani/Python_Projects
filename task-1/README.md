🧾 Tkinter Sign-In / Sign-Up with Invoice Generator
📖 Description

A Python GUI application built using Tkinter that allows users to:

Sign Up (register with username & password)

Sign In (login with credentials)

Access an Invoice Form to enter customer details, items, and automatically calculate the total bill.

This is a beginner-friendly project demonstrating user authentication and invoice calculation in Tkinter.

⚙️ Setup Instructions

Make a directory for the project and navigate into it

mkdir tkinter_invoice && cd tkinter_invoice


Create virtual environment (optional but recommended)

python -m venv venv
# Activate
venv\Scripts\activate      # Windows  
source venv/bin/activate   # Linux/Mac


No external libraries required (Tkinter is included with Python).

Save the script as app.py

Run the application

python app.py

📂 Project Files

app.py → Main script with Sign-In, Sign-Up, and Invoice functionality.

README.md → Documentation file.

🔑 Features

Sign Up

New users can register with a username and password.

Duplicate usernames are not allowed.

Sign In

Existing users can log in with valid credentials.

Invalid login shows an error popup.

Invoice Form

Enter Customer Name

Enter Item, Quantity, and Price per Item

Calculate total cost dynamically.

🖼️ GUI Flow
Sign-In / Sign-Up Window

Username input

Password input

Sign In button

Sign Up button

Invoice Window

Customer Name input

Item input

Quantity input

Price per item input

Calculate Total button

Displays total amount

📸 Example Usage

Sign Up Flow:

Username: janvi
Password: 12345
→ Registered successfully!


Sign In Flow:

Username: janvi
Password: 12345
→ Login successful!


Invoice Calculation:

Customer: Riya
Item: Notebook
Quantity: 5
Price per item: 20
Total: $100.00
