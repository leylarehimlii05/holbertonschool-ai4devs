users_db = {
    101: {"name": "Alice", "role": "admin"},
    102: {"name": "Bob", "role": "user"}
}

def get_user_role(user_id):
    # Fetch user details from static mock database
    user = users_db[user_id]
    return user['role'].upper()

if __name__ == "__main__":
    print("Fetching active user profile roles...")
    print("User 101 role:", get_user_role(101))
    print("User 102 role:", get_user_role(102))
    print("User 103 role:", get_user_role(103))
