import random

colors = ["R", "G", "B", "Y", "O", "P"]  # Rot, Grün, Blau, Gelb, Orange, Purple
code = [random.choice(colors) for _ in range(4)]

print("🧠 MASTERMIND")
print("Guess the 4-color code!")
print("Colors:", " ".join(colors))
print("Example input: R G B Y")

attempts = 0

while True:
    guess = input("\nYour guess: ").upper().split()

    if len(guess) != 4:
        print("❌ Enter exactly 4 colors!")
        continue

    attempts += 1

    # richtige Position
    correct_pos = sum(1 for i in range(4) if guess[i] == code[i])

    # richtige Farbe (egal wo)
    correct_color = sum(min(guess.count(c), code.count(c)) for c in set(colors)) - correct_pos

    print(f"✅ Correct position: {correct_pos}")
    print(f"🎯 Correct color (wrong place): {correct_color}")

    if correct_pos == 4:
        print(f"🎉 You cracked the code in {attempts} attempts!")
        break