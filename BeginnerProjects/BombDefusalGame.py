import random
import time

code = str(random.randint(100, 999))
start_time = time.time()
time_limit = 15

print("💣 BOMB DEFUSAL")
print("You have 15 seconds to guess the 3-digit code!")

while True:
    remaining = int(time_limit - (time.time() - start_time))

    if remaining <= 0:
        print("💥 BOOM! Time's up!")
        break

    print(f"\n⏳ Time left: {remaining}s")
    guess = input("Enter code: ")

    if guess == code:
        print("🎉 Bomb defused!")
        break

    # Hinweise
    correct_positions = sum(1 for i in range(3) if guess[i] == code[i])
    print(f"🔍 Correct digits in correct place: {correct_positions}")