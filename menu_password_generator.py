
import random
import string

def generate_simple(length=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def generate_strong(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_pin(length=4):
    return ''.join(random.choice(string.digits) for _ in range(length))

def menu():
    print("\n--- Password Generator Menu ---")
    print("1. Simple Password (letters + digits)")
    print("2. Strong Password (letters + digits + symbols)")
    print("3. Numeric PIN")
    print("4. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '4':
        print("Exiting... Goodbye!")
        break

    if choice in ['1', '2', '3']:
        length = int(input("Enter desired length: "))
        if choice == '1':
            print("Generated Password:", generate_simple(length))
        elif choice == '2':
            print("Generated Password:", generate_strong(length))
        elif choice == '3':
            print("Generated PIN:", generate_pin(length))
    else:
        print("Invalid choice! Please try again.")
