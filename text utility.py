def word_count(text):
    return len(text.split())

def vowel_count(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

def reverse_text(text):
    return text[::-1]

print("1.Word Count 2.Vowel Count 3.Reverse")
choice = int(input("Choose option: "))
text = input("Enter text: ")
if choice == 1:
    print("Words:", word_count(text))
elif choice == 2:
    print("Vowels:", vowel_count(text))
elif choice == 3:
    print("Reverse:", reverse_text(text))
else:
    print("Invalid choice")
