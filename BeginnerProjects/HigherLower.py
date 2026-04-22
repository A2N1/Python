import random

cards = list(range(1, 14))  # 1=Ace, 11=J, 12=Q, 13=K

def card_name(value):
    names = {1: "A", 11: "J", 12: "Q", 13: "K"}
    return names.get(value, str(value))

score = 0
current = random.choice(cards)

print("🃏 HIGHER OR LOWER")
print("Guess if the next card is higher or lower!")

while True:
    print(f"\nCurrent card: {card_name(current)}")
    guess = input("Higher or Lower? (h/l or q to quit): ").lower()

    if guess == "q":
        break

    next_card = random.choice(cards)
    print(f"Next card: {card_name(next_card)}")

    if next_card == current:
        print("😐 Same card! No points.")
    elif (guess == "h" and next_card > current) or (guess == "l" and next_card < current):
        score += 1
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        break

    current = next_card
    print(f"Score: {score}")

print(f"\n🏁 Final Score: {score}")