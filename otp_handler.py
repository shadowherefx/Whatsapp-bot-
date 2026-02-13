import random

otp_store = {}

def generate_otp(user_id):
    otp = random.randint(100000, 999999)
    otp_store[user_id] = otp
    return otp

def verify_otp(user_id, entered_otp):
    if otp_store.get(user_id) == entered_otp:
        del otp_store[user_id]
        return True
    return False