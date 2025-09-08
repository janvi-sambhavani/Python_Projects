import qrcode

# Taking UPI ID as input from the user
upi_id = input("Enter your UPI ID: ")

# Defining the payment URLs for each app
# You can customize these (add amount, currency, note, etc.)
phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# Create QR codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# Save the QR codes as image files (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

# Display the QR codes (optional; needs PIL or Pillow installed)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

