import random
import time
import os

sequence = []
round_num = 1

def clear():
    os.system("cls" if os.name == "nt" else "clear")

print("🔢 MEMORY GAME")
print("Remember the sequence!")

while True:
    # neue Zahl hinzufügen
    sequence.append(str(random.randint(0, 9)))

    print(f"\nRound {round_num}")
    print("Memorize:")

    for num in sequence:
        print(num, end=" ", flush=True)
        time.sleep(0.7)

    time.sleep(1)
    clear()

    guess = input("Enter the sequence: ").strip()

    if guess == "".join(sequence):
        print("✅ Correct!")
        round_num += 1
    else:
        print(f"❌ Wrong! Sequence was: {''.join(sequence)}")
        break