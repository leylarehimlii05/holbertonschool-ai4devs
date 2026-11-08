users_db = {
    101: {"name": "Alice", "role": "admin"},
    102: {"name": "Bob", "role": "user"}
}

def get_user_role(user_id):
    user = users_db[user_id]
    return user['role'].upper()

print("User 101 role:", get_user_role(101))
print("User 103 role:", get_user_role(103))
