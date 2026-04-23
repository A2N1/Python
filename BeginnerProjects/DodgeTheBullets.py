import random
import os
import time

width = 15
height = 10

player_x = width // 2
bullets = []
score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw():
    clear()
    for y in range(height):
        row = ""
        for x in range(width):
            if (x, y) in bullets:
                row += "|"
            elif y == height-1 and x == player_x:
                row += "A"
            else:
                row += " "
        print(row)
    print("Score:", score)

while True:
    # neue Kugeln
    if random.random() < 0.4:
        bullets.append((random.randint(0, width-1), 0))

    # bewegen
    bullets = [(x, y+1) for (x, y) in bullets if y < height]

    draw()

    move = input("a=left d=right: ")

    if move == "a" and player_x > 0:
        player_x -= 1
    elif move == "d" and player_x < width-1:
        player_x += 1

    # Kollision
    if (player_x, height-1) in bullets:
        print("💥 Hit! Game Over")
        break

    score += 1
    time.sleep(0.1)