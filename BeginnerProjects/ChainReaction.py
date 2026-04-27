import random

size = 5
board = [[0 for _ in range(size)] for _ in range(size)]

def draw():
    for row in board:
        print(" ".join(str(cell) if cell > 0 else "." for cell in row))
    print()

def explode(x, y):
    if board[y][x] < 3:
        return

    board[y][x] = 0

    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            board[ny][nx] += 1
            explode(nx, ny)

print("💥 CHAIN REACTION")
print("Place bombs and trigger explosions!")

while True:
    draw()

    try:
        x = int(input("x (0-4): "))
        y = int(input("y (0-4): "))
    except:
        print("❌ Invalid input!")
        continue

    if not (0 <= x < size and 0 <= y < size):
        print("❌ Out of bounds!")
        continue

    board[y][x] += 1
    explode(x, y)