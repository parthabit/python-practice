# File name: story_generator.py

import random

def random_story():
    subjects = ["A wizard", "An astronaut", "A detective", "A dragon", "A robot"]
    actions = ["found", "lost", "built", "destroyed", "discovered"]
    objects = ["a magical book", "an ancient map", "a secret code", "a golden key", "a hidden portal"]
    places = ["in the forest", "on the moon", "inside a cave", "at the library", "under the sea"]

    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(objects)
    place = random.choice(places)
    

    return f"{subject} {action} {obj} {place}."

def menu():
    while True:
        print("\n--- Random Story Generator ---")
        print("1. Generate a story")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nYour story:")
            print(random_story())
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()

