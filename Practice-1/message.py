# Step 1: Import Required Libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Step 2: Twilio Credentials (replace with your actual credentials)
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'

client = Client(account_sid, auth_token)

# Step 3: Define the send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',  # This is Twilio’s sandbox number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print('An error occurred:', str(e))

# Step 4: User Input
name = input('Enter the recipient name: ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g., +1234567890): ')
message_body = input(f'Enter the message you want to send to {name}: ')

# Step 5: Parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')

# Convert input to datetime object
schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate the delay in seconds
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

# Step 6: Wait and Send Message
if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time.')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message_body)
