import re

def check_password_strength(password):
    # Minimum length requirement
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Presence of uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return "Weak: Password should contain both uppercase and lowercase letters."

    # Presence of numbers
    if not any(char.isdigit() for char in password):
        return "Weak: Password should contain at least one number."

    # Presence of special characters
    special_characters = re.compile(r'[@_!#$%^&*()<>?/\\|}{~:]')
    if not special_characters.search(password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets all criteria for strength."

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print("Password Strength:", strength)

if __name__ == "__main__":
    main()

