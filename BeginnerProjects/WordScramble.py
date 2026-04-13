import random

words = ["python", "developer", "computer", "keyboard", "programming", "algorithm"]

score = 0

while True:
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))

    print("\n🔤 Unscramble the word:")
    print(scrambled)

    guess = input("Your guess (or 'quit'): ").lower()

    if guess == "quit":
        break

    if guess == word:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The word was: {word}")

    print("Score:", score)

print("👋 Thanks for playing!")