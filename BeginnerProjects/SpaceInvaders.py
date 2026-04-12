import os
import time
import random

width = 20
height = 10

player_x = width // 2
bullets = []
enemies = [(x, 0) for x in range(5, 15, 2)]

score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw():
    clear()
    for y in range(height):
        row = ""
        for x in range(width):
            if (x, y) in enemies:
                row += "W"
            elif (x, y) in bullets:
                row += "|"
            elif y == height-1 and x == player_x:
                row += "A"
            else:
                row += " "
        print(row)
    print("Score:", score)

while True:
    draw()

    move = input("a=left d=right space=shoot: ")

    # Bewegung
    if move == "a" and player_x > 0:
        player_x -= 1
    elif move == "d" and player_x < width-1:
        player_x += 1
    elif move == " ":
        bullets.append((player_x, height-2))

    # Kugeln bewegen
    bullets = [(x, y-1) for (x, y) in bullets if y > 0]

    # Gegner bewegen (nach unten)
    if random.random() < 0.3:
        enemies = [(x, y+1) for (x, y) in enemies]

    # Kollisionen
    new_bullets = []
    new_enemies = []

    for e in enemies:
        hit = False
        for b in bullets:
            if e == b:
                hit = True
                score += 1
        if not hit:
            new_enemies.append(e)

    for b in bullets:
        if b not in enemies:
            new_bullets.append(b)

    enemies = new_enemies
    bullets = new_bullets

    # Neue Gegner
    if random.random() < 0.2:
        enemies.append((random.randint(0, width-1), 0))

    # Game Over
    for e in enemies:
        if e[1] == height-1:
            print("💀 Game Over!")
            exit()

    time.sleep(0.1)