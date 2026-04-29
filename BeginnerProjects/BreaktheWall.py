import time
import os

width = 20
height = 10

# Paddle
paddle_x = width // 2

# Ball
ball_x = width // 2
ball_y = height - 2
dx = 1
dy = -1

# Blöcke
bricks = {(x, 1) for x in range(2, width-2)}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def draw():
    clear()
    for y in range(height):
        row = ""
        for x in range(width):
            if (x, y) in bricks:
                row += "#"
            elif x == ball_x and y == ball_y:
                row += "O"
            elif y == height-1 and abs(x - paddle_x) <= 2:
                row += "="
            else:
                row += " "
        print(row)

print("🧱 BREAK THE WALL")
print("a = left | d = right")

while True:
    draw()

    move = input("Move: ")

    if move == "a" and paddle_x > 2:
        paddle_x -= 1
    elif move == "d" and paddle_x < width-3:
        paddle_x += 1

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

    # Block Kollision
    if (ball_x, ball_y) in bricks:
        bricks.remove((ball_x, ball_y))
        dy *= -1

    # Game Over
    if ball_y > height-1:
        print("💀 Game Over!")
        break

    # Win
    if not bricks:
        print("🎉 You destroyed all bricks!")
        break

    time.sleep(0.1)