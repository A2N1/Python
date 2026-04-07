import random

size = 5
mines = 5

board = [["." for _ in range(size)] for _ in range(size)]
mine_positions = set()

while len(mine_positions) < mines:
    x = random.randint(0, size-1)
    y = random.randint(0, size-1)
    mine_positions.add((x, y))

def print_board():
    for row in board:
        print(" ".join(row))

print("💣 Minesweeper")
print("Enter coordinates like: row col")

while True:
    print_board()

    try:
        row, col = map(int, input("Choose a field: ").split())
    except:
        print("Invalid input!")
        continue

    if (row, col) in mine_positions:
        print("💥 BOOM! You hit a mine!")
        break

    board[row][col] = "O"

    if sum(row.count("O") for row in board) == size*size - mines:
        print("🎉 You won!")
        break