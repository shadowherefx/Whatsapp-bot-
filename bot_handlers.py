from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
from config import TELEGRAM_CHANNEL_1, TELEGRAM_CHANNEL_2, WHATSAPP_LINK, YOUTUBE_LINK, ADMIN_NUMBER
from utils import is_verified, mark_verified
from otp_handler import generate_otp, verify_otp
from whatsapp_api import send_otp as send_whatsapp_otp

# Basic commands
basic_commands = {
    "admin": lambda update, context: update.message.reply_text(f"شیڈو پلس، نمبر: {ADMIN_NUMBER}"),
    "ping": lambda update, context: update.message.reply_text("pong!"),
    "status_view": lambda update, context: update.message.reply_text("Active"),
    "auto_reply": lambda update, context: update.message.reply_text("Auto reply enabled"),
    "anti_delete": lambda update, context: update.message.reply_text("Anti delete active"),
}

def start(update: Update, context: CallbackContext):
    buttons = [
        [InlineKeyboardButton("ٹیلیگرام چینل 1", url=TELEGRAM_CHANNEL_1)],
        [InlineKeyboardButton("ٹیلیگرام چینل 2", url=TELEGRAM_CHANNEL_2)],
        [InlineKeyboardButton("واٹس ایپ گروپ", url=WHATSAPP_LINK)],
        [InlineKeyboardButton("یوٹیوب سبسکرائب", url=YOUTUBE_LINK)],
        [InlineKeyboardButton("ویریفائی", callback_data="verify")]
    ]
    keyboard = InlineKeyboardMarkup(buttons)
    update.message.reply_text("Welcome to Shadow Bot! تمام چینلز جوائن کریں اور Verify کریں:", reply_markup=keyboard)

def verify_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    user_id = query.from_user.id
    try:
        member1 = context.bot.get_chat_member(TELEGRAM_CHANNEL_1, user_id)
        member2 = context.bot.get_chat_member(TELEGRAM_CHANNEL_2, user_id)
        if member1.status in ["member", "administrator", "creator"] and member2.status in ["member", "administrator", "creator"]:
            query.answer("ویریفکیشن مکمل!")
            mark_verified(user_id)
            query.edit_message_text("اب آپ رسائی حاصل کر چکے ہیں۔ پلیز /menu ٹائپ کریں")
        else:
            query.answer("پہلے تمام چینلز جوائن کریں!")
    except:
        query.answer("چینل چیک میں مسئلہ، دوبارہ کوشش کریں!")

def menu_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Menu: \n"
        "1. /pair \n"
        "2. /dispair \n"
        "3. /ping \n"
        "4. /admin \n"
        "5. /status_view \n"
        "6. /auto_reply \n"
        "7. /anti_delete"
    )

def pair_handler(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    try:
        number = update.message.text.split(" ")[1]  # /pair 0300XXXXXXX
        otp = generate_otp(user_id)
        send_whatsapp_otp(number, otp)
        update.message.reply_text(f"OTP بھیجا گیا ہے: {otp} (Telegram & WhatsApp)")
    except IndexError:
        update.message.reply_text("استعمال: /pair <number>")

def dispair_handler(update: Update, context: CallbackContext):
    update.message.reply_text("نمبر ہٹا دیا گیا ہے /pair دوبارہ کریں")