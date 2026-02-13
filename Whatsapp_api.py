import pywhatkit

def send_otp(number, otp_code):
    # WhatsApp Web استعمال کرتے ہوئے OTP بھیجیں
    pywhatkit.sendwhatmsg_instantly(f"+{number}", f"Your OTP code is: {otp_code}")