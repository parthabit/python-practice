import random
import string

def generate_password(length, use_digits=True, use_special=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    while True:
        print("\n=== Password Generator Menu ===")
        print("1. Generate simple password (letters only)")
        print("2. Generate password with letters + digits")
        print("3. Generate strong password (letters + digits + special chars)")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3"]:
            length = int(input("Enter desired password length: "))
            if choice == "1":
                print("Generated Password:", generate_password(length, False, False))
            elif choice == "2":
                print("Generated Password:", generate_password(length, True, False))
            elif choice == "3":
                print("Generated Password:", generate_password(length, True, True))
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
