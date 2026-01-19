# Send-Message-To-Telegram-User

This project demonstrates how to send a message to a specific Telegram user using Python with **Telethon** and **TeleBot** libraries.

---

## 🚀 Features
- Send direct messages to Telegram users
- Authenticate using Telegram API credentials
- Secure session-based communication
- Simple and reusable Python script

---

## 📌 Prerequisites

- Python 3.7+
- Telegram account
- Telegram Bot Token
- Telegram API credentials

---

## 🤖 Step 1: Create a Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Click **Start** or send `/start`
3. Send `/newbot`
4. Set a **bot name** and **username**
5. Copy the **Bot Token** provided

---

## 🔐 Step 2: Get Telegram API Credentials

1. Visit: https://my.telegram.org/auth/auth
2. Login using your Telegram phone number
3. Go to **API Development Tools**
4. Fill in the form
5. Copy:
   - `api_id`
   - `api_hash`

---

## 📦 Step 3: Install Required Modules

pip install -r requirements.txt

---

## 🧠 Step 4: Code Explanation
- Telebot is used to interact with Telegram bots.
- Telethon allows user-level access to Telegram.
- A session is created using TelegramClient.
- On first run, Telegram sends an OTP for authentication.
- The script sends a message to a specific user using InputPeerUser.
- Errors like invalid peer, flood wait, or hash mismatch are handled.
- The session is safely disconnected after execution.

---

## ▶️ Step 5: Run the Script
python main.py
On first execution, enter the OTP sent to your Telegram app.

---

##  ⚠️ Common Errors
- PeerFloodError: Too many messages sent
- InvalidUserError: Wrong user ID or hash
- AuthKeyError: Session issue, delete session.session
