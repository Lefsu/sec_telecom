import re

# Function to validate password based on new criteria
def validate_password(password):
    # Check if password length is at least 10 characters
    if len(password) < 10:
        return False
    # Check if password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    # Check if password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    # Check if password contains at least one digit
    if not re.search(r'\d', password):
        return False
    # Check if password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    # If all checks passed, password is valid
    return True

# Function to check users' passwords and identify weak ones
def check_user_passwords(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            # Each line should follow the format: username:password
            username, password = line.strip().split(':')
            if not validate_password(password):
                print(f"{username} needs to change their password.")

# Example usage
# Assuming 'users.txt' contains user:password data
check_user_passwords('users.txt')
