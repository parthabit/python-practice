import random

riddles = [
    ("What has to be broken before you can use it?", "An egg"),
    ("I’m tall when I’m young, and I’m short when I’m old. What am I?", "A candle"),
    ("What month of the year has 28 days?", "All of them"),
    ("What is full of holes but still holds water?", "A sponge"),
    ("What question can you never answer yes to?", "Are you asleep yet?")
]

def show_riddle():
    riddle, answer = random.choice(riddles)
    print("\nRiddle:", riddle)
    input("Press Enter to reveal the answer...")
    print("Answer:", answer)

def riddle_generator():
    while True:
        print("\n--- Menu Driven Riddle Generator ---")
        print("1. Show a random riddle")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            show_riddle()
        elif choice == '2':
            print("Goodbye! Keep puzzling your mind!")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    riddle_generator()
