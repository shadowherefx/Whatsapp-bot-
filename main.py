# main.py

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from bot_handlers import start_handler, verify_handler, menu_handler, pair_handler, dispair_handler, basic_commands
from config import TELEGRAM_BOT_TOKEN

updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dp = updater.dispatcher

# Handlers رجسٹر
dp.add_handler(CommandHandler("start", start_handler))
dp.add_handler(CommandHandler("otp", verify_handler))
dp.add_handler(CommandHandler("menu", menu_handler))
dp.add_handler(CommandHandler("pair", pair_handler))
dp.add_handler(CommandHandler("dispair", dispair_handler))

# Basic commands
for cmd in basic_commands:
    dp.add_handler(CommandHandler(cmd, basic_commands[cmd]))

print("Shadow Bot چل رہا ہے...")
updater.start_polling()
updater.idle()
