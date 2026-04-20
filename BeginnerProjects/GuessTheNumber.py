import random

number = random.randint(1, 100)
last_diff = None
attempts = 0

print("🕵️ GUESS THE NUMBER (Hot & Cold)")
print("Guess a number between 1 and 100")

while True:
    try:
        guess = int(input("\nYour guess: "))
    except:
        print("❌ Enter a number!")
        continue

    attempts += 1
    diff = abs(number - guess)

    if guess == number:
        print(f"🎉 Correct! You needed {attempts} attempts.")
        break

    if last_diff is None:
        print("🔍 First guess...")
    else:
        if diff < last_diff:
            print("🔥 Warmer!")
        elif diff > last_diff:
            print("❄️ Colder!")
        else:
            print("😐 Same distance!")

    last_diff = diff