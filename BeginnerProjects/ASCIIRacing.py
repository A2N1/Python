import random
import os
import time

width = 7
player_pos = width // 2
obstacles = []

score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw():
    clear()
    for y in range(10):
        row = ""
        for x in range(width):
            if y == 9 and x == player_pos:
                row += "A"
            elif (y, x) in obstacles:
                row += "X"
            else:
                row += "."
        print(row)
    print("Score:", score)

while True:
    # neue Hindernisse
    if random.random() < 0.3:
        obstacles.append((0, random.randint(0, width - 1)))

    # Hindernisse bewegen
    obstacles = [(y+1, x) for (y, x) in obstacles if y < 9]

    draw()

    # Kollision prüfen
    if (9, player_pos) in obstacles:
        print("💥 Crash! Game Over")
        break

    move = input("Move (a=left, d=right, enter=stay): ")

    if move == "a" and player_pos > 0:
        player_pos -= 1
    elif move == "d" and player_pos < width - 1:
        player_pos += 1

    score += 1
    time.sleep(0.2)