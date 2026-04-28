import random

size = 5
ships = 3

board = [["." for _ in range(size)] for _ in range(size)]
ship_positions = set()

# Schiffe platzieren
while len(ship_positions) < ships:
    x = random.randint(0, size-1)
    y = random.randint(0, size-1)
    ship_positions.add((x, y))

hits = 0

def print_board():
    for row in board:
        print(" ".join(row))
    print()

print("🚢 BATTLESHIP")
print("Find all ships!")

while hits < ships:
    print_board()

    try:
        x = int(input("x (0-4): "))
        y = int(input("y (0-4): "))
    except:
        print("❌ Invalid input!")
        continue

    if (x, y) in ship_positions:
        print("💥 HIT!")
        board[y][x] = "X"
        hits += 1
        ship_positions.remove((x, y))
    else:
        print("🌊 Miss!")
        board[y][x] = "O"

print("🎉 You sank all ships!")