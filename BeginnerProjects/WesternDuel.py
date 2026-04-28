import time
import random

print("🤠 WESTERN DUEL")
print("Wait for 'FIRE!' then press Enter FAST!")
print("But don't shoot too early... 😈")

while True:
    wait_time = random.uniform(2, 5)
    print("\nGet ready...")
    time.sleep(wait_time)

    # Fake Chance (tricky!)
    if random.random() < 0.3:
        print("...")
        early = input()
        print("💥 Too early! You lose!")
        break

    print("🔥 FIRE!")
    start = time.time()

    shot = input()

    reaction = time.time() - start

    if reaction < 0.3:
        print(f"🎯 You win! Reaction: {round(reaction, 3)}s")
    else:
        print(f"💀 Too slow! Reaction: {round(reaction, 3)}s")
        break

    again = input("Play again? (y/n): ")
    if again != "y":
        break