def register_user_roles(username, role, assigned_roles=[]):
    """Assign a role to a user and return their updated role list."""
    # Bug 1: Mutable default list is shared across all function calls
    if role not in assigned_roles:
        assigned_roles.append(role)
    return {"username": username, "roles": assigned_roles}


def verify_api_key(provided_key, expected_key):
    """Validate incoming API key."""
    # Bug 2: Non-constant time comparison & missing None/type check
    return provided_key == expected_key
