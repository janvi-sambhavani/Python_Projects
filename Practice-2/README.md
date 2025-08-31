💳 UPI QR Code Generator
📖 Description

A simple Python script to generate QR codes for UPI payment apps like PhonePe, Paytm, and Google Pay

⚙️ Setup Instructions

Make a directory for the project and navigate into it

mkdir upi_qr_generator && cd upi_qr_generator


Create a Python virtual environment (optional but recommended)

python -m venv venv
# Activate
venv\Scripts\activate      # Windows  
source venv/bin/activate   # Linux/Mac


Install dependencies

pip install qrcode pillow


Save the script as upi_qr.py

Run the script

python upi_qr.py

📂 Project Files

upi_qr.py → Main script for generating QR codes.

phonepe_qr.png → QR code for PhonePe (generated at runtime).

paytm_qr.png → QR code for Paytm (generated at runtime).

google_pay_qr.png → QR code for Google Pay (generated at runtime).

README.md → Documentation file.

🔑 How It Works

User enters their UPI ID.

Script generates UPI payment URLs for PhonePe, Paytm, and Google Pay.

QR codes are generated for each URL.

QR codes are saved as .png images.

Optionally, QR codes are displayed on the screen.

📸 Example

Input:

Enter your UPI ID: janvi@upi


Generated Files:

phonepe_qr.png

paytm_qr.png

google_pay_qr.png

📖 Customization

You can customize the UPI URL to include more details:

upi_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234&am=100&cu=INR&tn=Test%20Payment"


pa → Payee VPA (UPI ID)

pn → Payee Name

mc → Merchant Code (optional)

am → Amount

cu → Currency (e.g., INR)

tn → Transaction Note
