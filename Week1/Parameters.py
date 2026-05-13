def validate_password(password):
    if len(password) < 8:
        return "Too short"
    if not any(char.isupper() for char in password):
        return "Must contain uppercase"
    if not any(char.isdigit() for char in password):
        return "Must contain a digit"
    return "Valid password"

print(validate_password("Pass123"))   # Too short
print(validate_password("Password1")) # Valid password
