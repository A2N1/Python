import math
import random

print("🏀 BASKETBALL SHOT GAME")

# Zielposition (Korb)
hoop_distance = random.randint(8, 15)
hoop_height = random.randint(2, 5)

print(f"🏀 The hoop is {hoop_distance}m away and {hoop_height}m high")

while True:
    try:
        angle = float(input("\nAngle (degrees): "))
        power = float(input("Power: "))
    except:
        print("❌ Invalid input!")
        continue

    # einfache Wurfphysik
    g = 9.8
    angle_rad = math.radians(angle)

    # Flugzeit grob berechnen
    time_flight = (2 * power * math.sin(angle_rad)) / g

    # x und y Position am Ende
    x = power * math.cos(angle_rad) * time_flight
    y = power * math.sin(angle_rad) * time_flight - 0.5 * g * time_flight**2

    print(f"📍 Ball landed at x={round(x,1)}, y={round(y,1)}")

    if abs(x - hoop_distance) < 1 and abs(y - hoop_height) < 1:
        print("🎉 SWISH! You scored!")
        break
    elif x < hoop_distance:
        print("⬆️ Too short!")
    else:
        print("⬇️ Too far!")