import random

size = 4

# Board erstellen
board = list(range(1, size*size)) + [" "]
random.shuffle(board)

def print_board():
    for i in range(size):
        row = board[i*size:(i+1)*size]
        print(" ".join(f"{str(x).rjust(2)}" for x in row))
    print()

def move(direction):
    empty = board.index(" ")
    x = empty % size
    y = empty // size

    target = None

    if direction == "w" and y < size-1:
        target = empty + size
    elif direction == "s" and y > 0:
        target = empty - size
    elif direction == "a" and x < size-1:
        target = empty + 1
    elif direction == "d" and x > 0:
        target = empty - 1

    if target is not None:
        board[empty], board[target] = board[target], board[empty]

def is_solved():
    return board[:-1] == list(range(1, size*size))

print("🧩 Sliding Puzzle (15 Puzzle)")
print("w/a/s/d to move")

while True:
    print_board()
    move(input("Move: "))

    if is_solved():
        print("🎉 You solved it!")
        break