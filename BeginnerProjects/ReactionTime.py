import time
import random

print("🎯 REACTION TIME GAME")
print("Wait for 'GO!' and press Enter as fast as possible!")

while True:
    wait_time = random.uniform(2, 5)
    time.sleep(wait_time)

    print("\nGO!")
    start = time.time()

    input()  # warten auf Enter

    reaction = time.time() - start
    print(f"⏱️ Your reaction time: {round(reaction, 3)} seconds")

    if reaction < 0.2:
        print("⚡ INSANE!")
    elif reaction < 0.3:
        print("🔥 Very fast!")
    elif reaction < 0.5:
        print("👍 Good!")
    else:
        print("🐢 Too slow!")

    again = input("\nPlay again? (y/n): ").lower()
    if again != "y":
        break