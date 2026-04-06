import random
import string

def generate_simple_password(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_custom_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def menu():
    while True:
        print("\n=== Password Generator Menu ===")
        print("1. Generate Simple Password (8 chars)")
        print("2. Generate Strong Password (12 chars)")
        print("3. Generate Custom Length Password")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Generated Password:", generate_simple_password())
        elif choice == '2':
            print("Generated Password:", generate_strong_password())
        elif choice == '3':
            length = int(input("Enter desired length: "))
            print("Generated Password:", generate_custom_password(length))
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    menu()
