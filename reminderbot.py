import requests
import time
from datetime import datetime
#import schedule

# Your bot credentials
bot_id = '4082fee3bf2621876aa8a7b780'
link = 'https://meet.google.com/ynu-nwqh-rhy'
# Function to send a message
def send_message(message):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': bot_id,
        'text': message
    }
    response = requests.post(url, json=data)
    return response.status_code

# Function to send reminder
def send_friday_reminder():
    message = f"(Testing Bot)Reminder: Kevin's Programming Sessions online meeting starts at 3 PM CST!.\n See you there: {link}. "
    status = send_message(message)
    if status == 202:
        print(f"Reminder sent successfully at {datetime.now()}")
    else:
        print("Failed to send reminder")

def meeting_has_started():
    message = f'(Testing Bot)Meeting has started, join via: {link}'
    status = send_message(message)
    if status == 202:
        print(f"Reminder sent successfully at {datetime.now()}")
    else:
        print("Failed to send reminder")

#Schedule the task every Friday at 2:30 PM
schedule.every().friday.at("14:30").do(send_friday_reminder)
schedule.every().friday.at("15:00").do(meeting_has_started)
# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for a minute before checking again


if __name__ == "__main__":
    send_friday_reminder()
    meeting_has_started()
