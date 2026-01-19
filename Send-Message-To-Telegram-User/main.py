# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon import sync

# ================================
# CONFIGURATION
# ================================

# Get these values from Telegram
api_id = 'API_ID'
api_hash = 'API_HASH'
token = 'BOT_TOKEN'

# Message to be sent
message = "Working..."

# Phone number with country code
phone = 'YOUR_PHONE_NUMBER_WITH_COUNTRY_CODE'

# Receiver details
receiver_user_id = 'USER_ID'
receiver_user_hash = 'USER_HASH'

# ================================
# TELEGRAM CLIENT SETUP
# ================================

client = TelegramClient('session', api_id, api_hash)
client.connect()

# First-time login authorization
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the OTP received: '))

# ================================
# SEND MESSAGE
# ================================

try:
    receiver = InputPeerUser(receiver_user_id, receiver_user_hash)
    client.send_message(receiver, message, parse_mode='html')
    print("Message sent successfully!")

except Exception as e:
    print("Error occurred:", e)

# Disconnect the session
client.disconnect()
