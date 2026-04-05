

def convert_case(text, choice):
    if choice == 1:
        return text.lower()
    elif choice == 2:
        return text.upper()
    elif choice == 3:
        return text.title()
    else:
        return "Invalid choice!"



def main():
    text = input("Enter text: ")
    print("Choose conversion:")
    print("1. Lowercase")
    print("2. Uppercase")
    print("3. Title Case")
    choice = int(input("Enter choice (1-3): "))
    result = convert_case(text, choice)
    print("Converted text:", result)

if __name__ == "__main__":
    main()
