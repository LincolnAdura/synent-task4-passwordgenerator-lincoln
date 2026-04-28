# ============================================
# Synent Technologies - Python Internship
# Task 4: Password Generator (CLI)
# Developer: Lincoln Adura
# ============================================

import random
import string

def generate_password(length, use_upper, use_lower, use_numbers, use_special):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("yes", "no"):
            return choice == "yes"
        print("❌ Please enter yes or no.")

def password_generator():
    print("=" * 40)
    print(" Synent Technologies - Password Generator")
    print("=" * 40)

    while True:
        print("\nConfigure your password:")
        print("-" * 40)

        while True:
            try:
                length = int(input("Enter password length (8-50): "))
                if 8 <= length <= 50:
                    break
                print("❌ Please enter a length between 8 and 50.")
            except ValueError:
                print("❌ Invalid input! Please enter a number.")

        use_upper = get_yes_no("Include uppercase letters? (yes/no): ")
        use_lower = get_yes_no("Include lowercase letters? (yes/no): ")
        use_numbers = get_yes_no("Include numbers? (yes/no): ")
        use_special = get_yes_no("Include special characters? (yes/no): ")

        password = generate_password(length, use_upper, use_lower,
                                     use_numbers, use_special)

        if password is None:
            print("❌ You must select at least one character type!")
            continue

        print("\n" + "=" * 40)
        print("🔐 Your Generated Password:")
        print(f"   {password}")
        print("=" * 40)
        print(f"   Length: {length} characters")
        print(f"   Uppercase: {'✅' if use_upper else '❌'}")
        print(f"   Lowercase: {'✅' if use_lower else '❌'}")
        print(f"   Numbers: {'✅' if use_numbers else '❌'}")
        print(f"   Special Characters: {'✅' if use_special else '❌'}")
        print("=" * 40)

        again = get_yes_no("\nGenerate another password? (yes/no): ")
        if not again:
            print("\nStay secure! Goodbye! 🔒")
            break

if __name__ == "__main__":
    password_generator()