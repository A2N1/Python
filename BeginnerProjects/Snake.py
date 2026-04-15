import random
import os
import time

width = 15
height = 10

snake = [(5, 5)]
direction = (1, 0)

food = (random.randint(0, width-1), random.randint(0, height-1))

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw():
    clear()
    for y in range(height):
        row = ""
        for x in range(width):
            if (x, y) == food:
                row += "*"
            elif (x, y) in snake:
                row += "O"
            else:
                row += " "
        print(row)

while True:
    draw()

    move = input("w/a/s/d: ")

    if move == "w":
        direction = (0, -1)
    elif move == "s":
        direction = (0, 1)
    elif move == "a":
        direction = (-1, 0)
    elif move == "d":
        direction = (1, 0)

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Kollision Wand
    if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
        print("💀 Game Over!")
        break

    # Kollision mit sich selbst
    if head in snake:
        print("💀 You hit yourself!")
        break

    snake.insert(0, head)

    # Essen
    if head == food:
        food = (random.randint(0, width-1), random.randint(0, height-1))
    else:
        snake.pop()

    time.sleep(0.2)