🕹️ Tic-Tac-Toe Game (Tkinter)
📖 Description

A simple Tic-Tac-Toe game built with Python’s tkinter library.
Two players can play alternately, and the game highlights the winning combination.

⚙️ Setup Instructions

Make a directory for the project and navigate into it

mkdir tic_tac_toe && cd tic_tac_toe


Create virtual environment (optional but recommended)

python -m venv venv
# Activate
venv\Scripts\activate      # Windows


No external dependencies required (Tkinter is included with Python).

Save the code as game.py and run:

python game.py

📂 Project Files

game.py → Main file containing the Tic-Tac-Toe logic and Tkinter GUI.

README.md → Documentation file.

🎮 How to Play

The game starts with Player X.

Players take turns clicking on the grid.

The first player to align 3 of their marks (row, column, or diagonal) wins.

Winning cells are highlighted in green, and a popup announces the winner.

📸 Example (GUI)
[ X ][ O ][   ]  
[ O ][ X ][   ]  
[   ][ O ][ X ]   → Player X wins

📲 WhatsApp Message Scheduler (Twilio)
📖 Description

A Python script that uses Twilio’s WhatsApp API to schedule and send messages at a specific date and time.

⚙️ Setup Instructions

Make a directory for the project and navigate into it

mkdir whatsapp_scheduler && cd whatsapp_scheduler


Create virtual environment (optional but recommended)

python -m venv venv
# Activate
venv\Scripts\activate      # Windows


Install dependencies

pip install twilio


Save the code as whatsapp_scheduler.py

Run the script

python whatsapp_scheduler.py

📂 Project Files

whatsapp_scheduler.py → Main script for scheduling and sending WhatsApp messages.

README.md → Documentation file.

🔑 Configuration

Replace the placeholders with your actual Twilio credentials:

account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'


Use Twilio Sandbox WhatsApp number:

from_='whatsapp:+14155238886'


Add your verified WhatsApp number when prompted.

📖 Workflow

Enter recipient’s name and WhatsApp number (with country code).

Enter the message to send.

Enter date (YYYY-MM-DD) and time (HH:MM 24-hour format).

The script waits until the scheduled time and sends the message.

📸 Example

Input:

Enter the recipient name: Janvi
Enter the recipient WhatsApp number with country code (e.g., +919876543210): +919876543210
Enter the message you want to send to Janvi: Hello Janvi! This is a scheduled test message.
Enter the date to send the message (YYYY-MM-DD): 2025-09-01
Enter the time to send the message (HH:MM in 24-hour format): 20:30


Output:

Message scheduled to be sent to Janvi at 2025-09-01 20:30:00.
Message sent successfully! Message SID: SMxxxxxxxxxxxx
