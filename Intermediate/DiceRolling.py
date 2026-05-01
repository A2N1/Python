import random

print("🎲 DICE ROLLING SIMULATOR")

while True:
    try:
        sides = int(input("\nHow many sides? (e.g. 6, 20): "))
        rolls = int(input("How many rolls?: "))
    except:
        print("❌ Please enter numbers!")
        continue

    results = []

    for _ in range(rolls):
        roll = random.randint(1, sides)
        results.append(roll)

    print("\n🎲 Results:", results)
    print("➕ Total:", sum(results))
    print("📊 Average:", round(sum(results) / len(results), 2))

    # Statistik
    print("\n📈 Frequency:")
    for i in range(1, sides + 1):
        count = results.count(i)
        print(f"{i}: {count}")

    again = input("\nRoll again? (y/n): ").lower()
    if again != "y":
        break