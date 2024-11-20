# GroupME-Reminder-BOT
This project is an automated reminder bot designed to send messages about Kevin's Programming Sessions, scheduled every Friday. The bot uses a scheduling library to send two reminders:
1. A pre-meeting reminder at 2:30 PM CST.
2. A notification when the meeting starts at 3:00 PM CST.

## Features
- Automatically sends reminders for a recurring Friday meeting.
- Notifies participants when the meeting starts.
- Customizable meeting link and reminder times.

## Prerequisites
- Python 3.7 or higher.
- Required Python libraries: `requests`, `schedule`.

## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/friday-meeting-reminder-bot.git
cd friday-meeting-reminder-bot

## Install dependencies
pip install requests schedule
