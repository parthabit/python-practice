# File name: fantasy_name_generator.py
import random

def generate_name():
    prefixes = ["Ara", "Bel", "Cor", "Dra", "Ely", "Fen", "Gal", "Hel", "Ira", "Jor"]
    middles  = ["dor", "mir", "thal", "ven", "xis", "lor", "mar", "rin", "tor", "zel"]
    suffixes = ["ion", "ael", "or", "us", "eth", "is", "an", "iel", "os", "ar"]

    name = random.choice(prefixes) + random.choice(middles) + random.choice(suffixes)
    return name

# Generate 5 random names
if __name__ == "__main__":
    print("Fantasy Name Generator\n")
    for i in range(5):
        print(f"Name {i+1}: {generate_name()}")
