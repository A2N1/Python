import random

size = 7
player = [size//2, size//2]
zombies = [[0, 0], [6, 6]]
hp = 10
score = 0

def draw():
    for y in range(size):
        row = ""
        for x in range(size):
            if [y, x] == player:
                row += "P "
            elif [y, x] in zombies:
                row += "Z "
            else:
                row += ". "
        print(row)
    print(f"HP: {hp}  Score: {score}")

def move_player(direction):
    if direction == "w" and player[0] > 0:
        player[0] -= 1
    elif direction == "s" and player[0] < size-1:
        player[0] += 1
    elif direction == "a" and player[1] > 0:
        player[1] -= 1
    elif direction == "d" and player[1] < size-1:
        player[1] += 1

def move_zombies():
    for z in zombies:
        if z[0] < player[0]:
            z[0] += 1
        elif z[0] > player[0]:
            z[0] -= 1

        if z[1] < player[1]:
            z[1] += 1
        elif z[1] > player[1]:
            z[1] -= 1

def attack():
    global score
    for z in zombies[:]:
        if abs(z[0] - player[0]) <= 1 and abs(z[1] - player[1]) <= 1:
            zombies.remove(z)
            score += 1
            print("💥 Zombie killed!")

while hp > 0:
    print("\n" * 2)
    draw()

    action = input("Move (w/a/s/d) or attack (f): ")

    if action in ["w", "a", "s", "d"]:
        move_player(action)
    elif action == "f":
        attack()

    move_zombies()

    # Schaden prüfen
    for z in zombies:
        if z == player:
            hp -= 1
            print("🧟 You got hit!")

    # neue Zombies spawnen
    if random.random() < 0.3:
        zombies.append([random.randint(0, size-1), random.randint(0, size-1)])

print("💀 Game Over! Score:", score)