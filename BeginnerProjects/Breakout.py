import os
import time

width = 20
height = 10

paddle_x = width // 2
ball_x = width // 2
ball_y = height - 2

dx = 1
dy = -1

bricks = {(y, x) for y in range(2) for x in range(width)}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw():
    clear()
    for y in range(height):
        row = ""
        for x in range(width):
            if (y, x) in bricks:
                row += "#"
            elif y == ball_y and x == ball_x:
                row += "O"
            elif y == height-1 and abs(x - paddle_x) <= 2:
                row += "="
            else:
                row += " "
        print(row)

while True:
    draw()

    # Ball bewegen
    ball_x += dx
    ball_y += dy

    # Wand Kollision
    if ball_x <= 0 or ball_x >= width-1:
        dx *= -1
    if ball_y <= 0:
        dy *= -1

    # Paddle Kollision
    if ball_y == height-1 and abs(ball_x - paddle_x) <= 2:
        dy *= -1

    # Brick Kollision
    if (ball_y, ball_x) in bricks:
        bricks.remove((ball_y, ball_x))
        dy *= -1

    # Game Over
    if ball_y >= height:
        print("💀 Game Over!")
        break

    if not bricks:
        print("🎉 You win!")
        break

    move = input("Move (a=left, d=right, enter=stay): ")

    if move == "a" and paddle_x > 2:
        paddle_x -= 1
    elif move == "d" and paddle_x < width-3:
        paddle_x += 1

    time.sleep(0.1)