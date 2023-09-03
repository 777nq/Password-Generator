# password_generator.py
import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    include_digits = input("Include digits (yes/no): ").lower() == "yes"
    include_special_chars = input("Include special characters (yes/no): ").lower() == "yes"

    password = generate_password(length, include_digits, include_special_chars)
    print(f"Generated password: {password}")
