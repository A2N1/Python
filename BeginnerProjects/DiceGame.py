import random

score = 0

print("🎲 DICE GAME (Pig)")
print("Reach 50 points to win!")

while score < 50:
    turn_total = 0
    print(f"\n🏆 Total Score: {score}")

    while True:
        choice = input("Roll or Hold? (r/h): ").lower()

        if choice == "r":
            roll = random.randint(1, 6)
            print(f"🎲 You rolled: {roll}")

            if roll == 1:
                print("💥 You lost this round!")
                turn_total = 0
                break
            else:
                turn_total += roll
                print(f"Round total: {turn_total}")

        elif choice == "h":
            score += turn_total
            print(f"💰 You banked {turn_total} points!")
            break

print("🎉 You reached 50! You win!")