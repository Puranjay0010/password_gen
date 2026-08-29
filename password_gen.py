import random
import string

def generate_password(length=12, use_special=True):
    # Base character sets
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation if use_special else ""
    
    all_characters = letters + digits + special
    
    if length < 4:
        return "Password must be at least 4 characters long."
        
    # Ensure at least one of each required type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits)
    ]
    
    if use_special:
        password.append(random.choice(string.punctuation))
        
    # Fill the rest randomly
    while len(password) < length:
        password.append(random.choice(all_characters))
        
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    print("--- Secure Password Generator ---")
    try:
        length = int(input("Enter desired password length (default 12): ") or 12)
        special_chars = input("Include special characters? (y/n): ").lower().strip() != 'n'
        
        pwd = generate_password(length, special_chars)
        print(f"\nYour generated password is: {pwd}")
    except ValueError:
        print("Please enter a valid number for the length.")
