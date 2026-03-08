# text_utility.py

def to_title_case(text):
    return " ".join(word.capitalize() for word in text.split())

def reverse_text(text):
    return text[::-1]

def word_count(text):
    return len(text.split())

def remove_extra_spaces(text):
    return " ".join(text.split())

def main():
    while True:
        print("\n--- Text Utility ---")
        print("1. Convert to UPPERCASE")
        print("2. Convert to lowercase")
        print("3. Convert to Title Case")
        print("4. Reverse text")
        print("5. Word count")
        print("6. Remove extra spaces")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice in ["1","2","3","4","5","6"]:
            text = input("Enter text: ")

            if choice == "1":
                print("Result:", text.upper())
            elif choice == "2":
                print("Result:", text.lower())
            elif choice == "3":
                print("Result:", to_title_case(text))
            elif choice == "4":
                print("Result:", reverse_text(text))
            elif choice == "5":
                print("Word count:", word_count(text))
            elif choice == "6":
                print("Result:", remove_extra_spaces(text))
        elif choice == "7":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
