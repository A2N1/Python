import random

def generate_number():
    digits = list("0123456789")
    random.shuffle(digits)
    return "".join(digits[:4])

secret = generate_number()
attempts = 0

print("🧠 BULLS & COWS")
print("Guess the 4-digit number (no repeating digits)")

while True:
    guess = input("\nYour guess: ")

    if len(guess) != 4 or not guess.isdigit():
        print("❌ Enter exactly 4 digits!")
        continue

    attempts += 1

    bulls = sum(1 for i in range(4) if guess[i] == secret[i])
    cows = sum(1 for c in guess if c in secret) - bulls

    print(f"🐂 Bulls: {bulls} | 🐄 Cows: {cows}")

    if bulls == 4:
        print(f"🎉 You cracked the code in {attempts} attempts!")
        break