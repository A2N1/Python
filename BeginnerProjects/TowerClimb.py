import random

height = 20
player_pos = 0
score = 0

print("🧗 TOWER CLIMB")
print("Climb as high as you can!")

while True:
    print(f"\n⬆️ Height: {player_pos} | Score: {score}")

    print("1 = Climb carefully (safe, slow)")
    print("2 = Jump (risky, fast)")

    choice = input("Choose: ")

    if choice == "1":
        player_pos += 1
        score += 1
        print("🪜 You climbed safely")

    elif choice == "2":
        if random.random() < 0.6:
            jump = random.randint(2, 4)
            player_pos += jump
            score += jump * 2
            print(f"🚀 Big jump! +{jump}")
        else:
            print("💀 You slipped!")
            break

    # Zufälliges brechendes Feld
    if random.random() < 0.2:
        print("⚠️ Platform broke!")
        player_pos -= 1
        if player_pos < 0:
            player_pos = 0

    if player_pos >= height:
        print("🎉 You reached the top!")
        break

print(f"\n🏁 Final Score: {score}")