import math
import random

target = random.randint(50, 150)

print("🎯 ARTILLERY GAME")
print(f"Target is at distance: {target}")

while True:
    try:
        angle = float(input("\nEnter angle (degrees): "))
        power = float(input("Enter power: "))
    except:
        print("❌ Invalid input!")
        continue

    # Physik (vereinfachte Wurfparabel)
    distance = (power**2 * math.sin(math.radians(2 * angle))) / 9.8

    print(f"💥 Your shot landed at: {int(distance)}")

    if abs(distance - target) < 5:
        print("🎉 Direct hit!")
        break
    elif distance < target:
        print("⬆️ Too short!")
    else:
        print("⬇️ Too far!")