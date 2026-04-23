import random

width = 10
height = 10

# Einfaches zufälliges Labyrinth
maze = []
for y in range(height):
    row = []
    for x in range(width):
        if random.random() < 0.2:
            row.append("#")
        else:
            row.append(".")
    maze.append(row)

player = [0, 0]
exit_pos = [height-1, width-1]
maze[exit_pos[0]][exit_pos[1]] = "E"
maze[player[0]][player[1]] = "P"

def draw():
    for row in maze:
        print(" ".join(row))

def move(dx, dy):
    new_y = player[0] + dy
    new_x = player[1] + dx

    if 0 <= new_y < height and 0 <= new_x < width:
        if maze[new_y][new_x] != "#":
            maze[player[0]][player[1]] = "."
            player[0], player[1] = new_y, new_x
            maze[new_y][new_x] = "P"

print("🗺️ MAZE ESCAPE")
print("Find the exit (E)!")

while True:
    print()
    draw()

    move_input = input("Move (w/a/s/d): ")

    if move_input == "w":
        move(0, -1)
    elif move_input == "s":
        move(0, 1)
    elif move_input == "a":
        move(-1, 0)
    elif move_input == "d":
        move(1, 0)

    if player == exit_pos:
        print("🎉 You escaped the maze!")
        break