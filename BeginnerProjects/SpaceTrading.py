import random

money = 100
cargo = 0
day = 1

def get_prices():
    return {
        "Ore": random.randint(5, 15),
        "Food": random.randint(3, 10),
        "Tech": random.randint(10, 25)
    }

print("🚀 SPACE TRADER")
print("Buy low, sell high!")

while True:
    prices = get_prices()

    print(f"\n🌍 Day {day}")
    print(f"💰 Money: {money} | 📦 Cargo: {cargo}")
    print("Prices:", prices)

    print("\n1 = Buy")
    print("2 = Sell")
    print("3 = Travel (next day)")
    print("q = Quit")

    choice = input("Choose: ")

    if choice == "1":
        item = input("What to buy (Ore/Food/Tech): ").title()
        if item in prices:
            amount = int(input("Amount: "))
            cost = prices[item] * amount
            if money >= cost:
                money -= cost
                cargo += amount
                print(f"📦 Bought {amount} {item}")
            else:
                print("❌ Not enough money!")

    elif choice == "2":
        item = input("What to sell (Ore/Food/Tech): ").title()
        if item in prices:
            amount = int(input("Amount: "))
            if cargo >= amount:
                money += prices[item] * amount
                cargo -= amount
                print(f"💰 Sold {amount} {item}")
            else:
                print("❌ Not enough cargo!")

    elif choice == "3":
        print("🚀 Traveling...")
        day += 1

    elif choice == "q":
        break