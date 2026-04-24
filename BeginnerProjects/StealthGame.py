import random

size = 7

player = [0, 0]
goal = [size-1, size-1]
guard = [size//2, size//2]

def draw():
    for y in range(size):
        row = ""
        for x in range(size):
            if [y, x] == player:
                row += "P "
            elif [y, x] == goal:
                row += "E "
            elif [y, x] == guard:
                row += "G "
            else:
                row += ". "
        print(row)

def move(entity, direction):
    if direction == "w" and entity[0] > 0:
        entity[0] -= 1
    elif direction == "s" and entity[0] < size-1:
        entity[0] += 1
    elif direction == "a" and entity[1] > 0:
        entity[1] -= 1
    elif direction == "d" and entity[1] < size-1:
        entity[1] += 1

def guard_move():
    # zufällige Bewegung
    direction = random.choice(["w", "a", "s", "d"])
    move(guard, direction)

def guard_sees_player():
    # gleiche Reihe oder Spalte = gesehen
    return player[0] == guard[0] or player[1] == guard[1]

print("👮 STEALTH GAME")
print("Reach E without being seen!")

while True:
    print()
    draw()

    action = input("Move (w/a/s/d): ")
    move(player, action)

    guard_move()

    if guard_sees_player():
        print("👀 You were spotted! Game Over!")
        break

    if player == goal:
        print("🎉 You escaped undetected!")
        break