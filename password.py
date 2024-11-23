import re

def validate_password(password):
    # Check if password length is at least 8 characters
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    
    # Check if password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
    
    # Check if password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
    
    # Check if password contains at least one number
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one number.")
    
    # Check if password contains at least one special character
    special_characters = re.compile('[@_!#$%^&*()<>?/\\|}{~:]')
    if special_characters.search(password) is None:
        print("Password must contain at least one special character.")
    
    # If no issues were found, the password is valid
    if (len(password) >= 8 and any(char.isupper() for char in password)
            and any(char.islower() for char in password)
            and any(char.isdigit() for char in password)
            and special_characters.search(password) is not None):
        print("Password is valid.")

# Input from user
user_password = input("Enter a password: ")

# Call the validation function
validate_password(user_password)
