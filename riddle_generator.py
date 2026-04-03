import random

def show_menu():
    print("\n=== Riddle Generator Menu ===")
    print("1. Get a random riddle")
    print("2. Add a new riddle")
    print("3. View all riddles")
    print("4. Exit")

def get_random_riddle(riddles):
    if riddles:
        riddle, answer = random.choice(riddles)
        print(f"\nRiddle: {riddle}")
        input("Press Enter to reveal the answer...")
        print(f"Answer: {answer}")
    else:
        print("\nNo riddles available yet!")

def add_riddle(riddles):
    riddle = input("\nEnter your riddle: ")
    answer = input("Enter the answer: ")
    riddles.append((riddle, answer))
    print("Riddle added successfully!")

def view_riddles(riddles):
    if riddles:
        print("\n=== All Riddles ===")
        for i, (riddle, answer) in enumerate(riddles, start=1):
            print(f"{i}. {riddle} -> {answer}")
    else:
        print("\nNo riddles stored yet!")

def main():
    riddles = [
        ("What has keys but can’t open locks?", "A piano"),
        ("The more you take, the more you leave behind. What am I?", "Footsteps"),
        ("What has to be broken before you can use it?", "An egg")
    ]
    
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            get_random_riddle(riddles)
        elif choice == "2":
            add_riddle(riddles)
        elif choice == "3":
            view_riddles(riddles)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
