import random

money = 100
population = 0
houses = 0
factories = 0
day = 1

print("🏗️ CITY BUILDER")
print("Build your city!")

while True:
    print(f"\n📅 Day {day}")
    print(f"💰 Money: {money} | 👥 Population: {population}")
    print(f"🏠 Houses: {houses} | 🏭 Factories: {factories}")

    print("\n1 = Build House (cost 20)")
    print("2 = Build Factory (cost 30)")
    print("3 = Collect Taxes")
    print("4 = Next Day")
    print("q = Quit")

    choice = input("Choose: ")

    if choice == "1":
        if money >= 20:
            money -= 20
            houses += 1
            population += random.randint(2, 5)
            print("🏠 House built!")
        else:
            print("❌ Not enough money!")

    elif choice == "2":
        if money >= 30:
            money -= 30
            factories += 1
            print("🏭 Factory built!")
        else:
            print("❌ Not enough money!")

    elif choice == "3":
        income = houses * 5 + factories * 10
        money += income
        print(f"💰 Collected {income} in taxes!")

    elif choice == "4":
        day += 1

        # Events
        if random.random() < 0.3:
            loss = random.randint(5, 15)
            money -= loss
            print(f"⚠️ Event! You lost {loss} money!")

    elif choice == "q":
        break