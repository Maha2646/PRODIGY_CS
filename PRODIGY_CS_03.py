def check_password_strength(password):
    length_check = len(password) >= 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    strength_score = sum([length_check, has_uppercase, has_lowercase, has_digit, has_special])

    if all([length_check, has_uppercase, has_lowercase, has_digit, has_special]):
        print("Strong Password")
    elif 2 <= strength_score <= 4:
        print("Moderate Password")
    else:
        print("Weak Password")

if __name__ == "__main__":
    password = input("Enter your password: ")
    check_password_strength(password)