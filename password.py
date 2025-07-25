import random
import string

def generate_password():
    print("🔐 Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("⚠ Password should be at least 4 characters for strength.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure strong password: at least one from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest randomly
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to avoid predictable sequence
    random.shuffle(password)

    # Join and display the password
    final_password = ''.join(password)
    print("\n✅ Your generated password is:")
    print(final_password)

# Run the password generator
generate_password()