import json
USERS_FILE = "data/users.json"

def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def is_verified(user_id):
    users = load_users()
    return users.get(str(user_id), {}).get("verified", False)

def mark_verified(user_id):
    users = load_users()
    users[str(user_id)] = {"verified": True}
    save_users(users)