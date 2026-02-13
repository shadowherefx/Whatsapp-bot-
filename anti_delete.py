def anti_delete_message(user, message):
    # اگر یوزر نے delete کیا تو دوبارہ بھیجیں
    return f"شیڈو: دوبارہ میسج نہ ڈیلیٹ کریں!\nOriginal: {message}"