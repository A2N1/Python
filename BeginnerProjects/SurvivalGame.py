import random

wood = 0
food = 5
health = 10
day = 1

print("🌲 SURVIVAL GAME")
print("Survive as long as you can!")

while health > 0:
    print(f"\n🌅 Day {day}")
    print(f"❤️ Health: {health} | 🍖 Food: {food} | 🪵 Wood: {wood}")

    print("1 = Gather Wood")
    print("2 = Hunt Food")
    print("3 = Rest")
    print("4 = Do nothing")

    choice = input("Choose: ")

    if choice == "1":
        gained = random.randint(1, 4)
        wood += gained
        print(f"🪵 You gathered {gained} wood")

    elif choice == "2":
        if random.random() < 0.6:
            gained = random.randint(2, 5)
            food += gained
            print(f"🍖 You got {gained} food")
        else:
            health -= 2
            print("🐺 You got hurt while hunting!")

    elif choice == "3":
        if food > 0:
            food -= 1
            health += 2
            print("😴 You rested and recovered")
        else:
            print("❌ No food to rest!")

    elif choice == "4":
        print("...nothing happens")

    # Hunger-System
    food -= 1
    if food < 0:
        health -= 2
        print("🥶 You are starving!")

    day += 1

print("💀 You died...")