import random
import time
import os

height = 10
note_y = 0
hit_zone = height - 2

score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    note_y = 0

    while note_y < height:
        clear()

        for y in range(height):
            if y == note_y:
                print("   O   ")
            elif y == hit_zone:
                print(" [===] ")
            else:
                print("       ")

        print(f"\nScore: {score}")

        move = input("Press Enter to hit (or wait): ")

        # Treffer prüfen
        if move == "" and note_y == hit_zone:
            print("🎯 PERFECT!")
            score += 1
            time.sleep(0.5)
            break
        elif move == "" and note_y != hit_zone:
            print("❌ Miss!")
            time.sleep(0.5)

        note_y += 1
        time.sleep(0.2)

    # wenn Note unten angekommen ohne Treffer
    if note_y >= height:
        print("💀 Missed note!")
        break