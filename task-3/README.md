🧾 Invoice Generator (Tkinter + FPDF)
.

📌 Features

GUI built using Tkinter.

Predefined medicine price list.

Add medicine and quantity to cart.

Automatically calculates the total amount.

Generates a professional PDF invoice using FPDF.

Stores invoice with filename based on customer name.

🛠️ Requirements

Make sure you have Python 3.x installed.
Install dependencies before running the project:

pip install fpdf


(Tkinter comes pre-installed with Python, so no need to install separately.)

🚀 How to Run

Clone or download this project.

Open terminal/command prompt inside the project folder.

Run the script:

python invoice_generator.py


GUI will open.

🖼️ Usage Guide

Select a medicine from the list.

Enter the quantity.

Click Add Medicine.

Enter Customer Name.

Click Generate Invoice → A PDF invoice will be saved in the same folder.

📂 Project Structure
Invoice-Generator/
│
├── invoice_generator.py   # Main application script
├── README.md              # Project documentation
├── invoice_<customer>.pdf # Auto-generated invoice (after running)

📄 Sample Invoice (PDF)

The generated invoice contains:

Customer Name

Medicine Name(s)

Quantity

Price per Item

Total Amount

⚡ Example Output

GUI Preview

Medicine List

Quantity Input

Total Amount (auto-calculated)

Generate Invoice Button

Generated Invoice (PDF Example):

Invoice for John Doe
----------------------------------------
Medicine     Quantity   Price   Total
Medicine A   2          Rs.10   Rs.20
Medicine C   1          Rs.15   Rs.15

Total Amount: Rs.35.00
