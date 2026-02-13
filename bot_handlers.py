# bot_handlers.py

from telegram import Update
from telegram.ext import CallbackContext
from config import ADMIN_NUMBER
from Whatsapp_api import send_otp

# /start command
def start_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Type /otp to receive your OTP.")

# /otp command
def verify_handler(update: Update, context: CallbackContext):
    otp = "123456"  # Randomize کر سکتے ہو
    user_number = ADMIN_NUMBER  # example کے لیے
    send_otp(user_number, otp)
    update.message.reply_text(f"OTP sent to WhatsApp number: {user_number}")

# /menu command
def menu_handler(update: Update, context: CallbackContext):
    update.message.reply_text("This is the menu.")

# /pair command
def pair_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Pair handler executed.")

# /dispair command
def dispair_handler(update: Update, context: CallbackContext):
    update.message.reply_text("Dispair handler executed.")

# Basic commands dictionary
basic_commands = {
    "help": lambda update, context: update.message.reply_text("Help command executed."),
    "info": lambda update, context: update.message.reply_text("Info command executed.")
}
