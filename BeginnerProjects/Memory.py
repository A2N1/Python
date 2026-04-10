import random

symbols = ["A","B","C","D","E","F"]
cards = symbols * 2
random.shuffle(cards)

board = ["#" for _ in range(len(cards))]
revealed = []

def print_board():
    for i in range(len(board)):
        print(f"{i}:{board[i]}", end="  ")
        if (i+1) % 4 == 0:
            print()
    print()

while len(revealed) < len(cards):
    print_board()

    try:
        c1 = int(input("Choose first card: "))
        c2 = int(input("Choose second card: "))
    except:
        print("Invalid input!")
        continue

    if c1 == c2 or c1 in revealed or c2 in revealed:
        print("Invalid choice!")
        continue

    print(f"You revealed: {cards[c1]} and {cards[c2]}")

    if cards[c1] == cards[c2]:
        print("✅ Match!")
        board[c1] = cards[c1]
        board[c2] = cards[c2]
        revealed.extend([c1, c2])
    else:
        print("❌ No match!")

input("🎉 You won! Press Enter to exit.")