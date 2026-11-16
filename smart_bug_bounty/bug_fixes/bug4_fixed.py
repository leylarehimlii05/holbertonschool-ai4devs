import hmac


def register_user_roles(username, role, assigned_roles=None):
    """Assign a role to a user without mutating shared state across calls."""
    roles = list(assigned_roles) if assigned_roles is not None else []
    if role not in roles:
        roles.append(role)
    return {"username": username, "roles": roles}


def verify_api_key(provided_key, expected_key):
    """Validate incoming API key using constant-time comparison."""
    if not isinstance(provided_key, str) or not isinstance(expected_key, str):
        return False
    if not provided_key or not expected_key:
        return False
    return hmac.compare_digest(provided_key, expected_key)


if __name__ == "__main__":
    u1 = register_user_roles("alice", "admin")
    u2 = register_user_roles("bob", "viewer")
    assert u1["roles"] == ["admin"]
    assert u2["roles"] == ["viewer"]
    assert verify_api_key("secret_123", "secret_123") is True
    assert verify_api_key(None, "secret_123") is False
    print("bug4_fixed.py: All 4 test cases passed!")
