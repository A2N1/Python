import time
import random

sentences = [
    "python is a powerful programming language",
    "practice makes perfect",
    "coding every day improves your skills",
    "never give up on your goals",
    "debugging is part of programming"
]

print("⌨️ TYPING SPEED TEST")
print("Type the sentence as fast and accurately as possible!\n")

while True:
    sentence = random.choice(sentences)
    print("📝 Sentence:")
    print(sentence)

    input("\nPress Enter to start...")

    start = time.time()
    typed = input("\nType here:\n")
    end = time.time()

    time_taken = end - start
    words = len(sentence.split())
    wpm = (words / time_taken) * 60

    print(f"\n⏱️ Time: {round(time_taken, 2)} seconds")
    print(f"⚡ Speed: {int(wpm)} WPM")

    # Accuracy
    correct_chars = sum(1 for i in range(min(len(sentence), len(typed))) if sentence[i] == typed[i])
    accuracy = (correct_chars / len(sentence)) * 100

    print(f"🎯 Accuracy: {round(accuracy, 1)}%")

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        break