import json
import bcrypt
import os

USER_DB = "auth/users.json"

def load_users():
    if not os.path.exists(USER_DB):
        return {}
    with open(USER_DB, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=4)

# ---------------- REGISTER ----------------
def register_user(email, username, fullname, password):
    users = load_users()

    if email in users:
        return False, "Email already registered"

    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    users[email] = {
        "username": username,
        "fullname": fullname,
        "password": hashed_pw
    }

    save_users(users)
    return True, "Account created successfully"

# ---------------- LOGIN ----------------
def authenticate_user(email, password):
    users = load_users()

    if email not in users:
        return False, None

    stored_hash = users[email]["password"]

    if bcrypt.checkpw(password.encode(), stored_hash.encode()):
        return True, users[email]   # return user info

    return False, None
