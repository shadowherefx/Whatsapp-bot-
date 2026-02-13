# Whatsapp_api.py

import pywhatkit

def send_otp(number, otp_code):
    """
    WhatsApp Web استعمال کرتے ہوئے OTP بھیجیں
    number: country code کے ساتھ، جیسے "923001234567"
    otp_code: OTP number
    """
    pywhatkit.sendwhatmsg_instantly(f"+{number}", f"Your OTP code is: {otp_code}")
