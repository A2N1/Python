import os
import time
import random

width = 20
height = 10

bird_y = height // 2
velocity = 0

gravity = 1
jump = -3

pipes = []
gap_size = 3

score = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw():
    clear()
    for y in range(height):
        row = ""
        for x in range(width):
            if x == 2 and y == bird_y:
                row += "O"
            elif (x, y) in pipes:
                row += "|"
            else:
                row += " "
        print(row)
    print("Score:", score)

while True:
    # Input
    move = input("Press Enter to flap (or type anything): ")

    if move == "":
        velocity = jump

    # Physik
    velocity += gravity
    bird_y += velocity

    # Neue Pipes
    if len(pipes) == 0 or max([x for x, y in pipes]) < width - 5:
        gap_y = random.randint(2, height - gap_size - 2)
        for y in range(height):
            if not (gap_y <= y < gap_y + gap_size):
                pipes.append((width-1, y))

    # Pipes bewegen
    pipes = [(x-1, y) for (x, y) in pipes if x > 0]

    # Kollision
    if bird_y < 0 or bird_y >= height:
        print("💀 Game Over!")
        break

    if (2, bird_y) in pipes:
        print("💥 You hit a pipe!")
        break

    # Score
    score += 1

    draw()
    time.sleep(0.2)