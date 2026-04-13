import time

money = 0
click_value = 1
auto_income = 0

while True:
    print("\n💰 Money:", money)
    print("1 = Click (+{})".format(click_value))
    print("2 = Upgrade Click (cost: 10)")
    print("3 = Buy Auto Income (cost: 20)")
    print("4 = Wait (earn passive money)")
    print("q = Quit")

    choice = input("Choose: ")

    if choice == "1":
        money += click_value

    elif choice == "2":
        if money >= 10:
            money -= 10
            click_value += 1
            print("⬆️ Click upgraded!")
        else:
            print("❌ Not enough money!")

    elif choice == "3":
        if money >= 20:
            money -= 20
            auto_income += 1
            print("🤖 Auto income increased!")
        else:
            print("❌ Not enough money!")

    elif choice == "4":
        print("⏳ Waiting...")
        time.sleep(2)
        money += auto_income * 2

    elif choice == "q":
        break