import random
import time

player_hp = 20
enemy_hp = 20

print("🧮 MATH BATTLE")
print("Solve math problems to attack!")

while player_hp > 0 and enemy_hp > 0:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        correct = a + b
    elif op == "-":
        correct = a - b
    else:
        correct = a * b

    print(f"\n❤️ You: {player_hp} | 👾 Enemy: {enemy_hp}")
    print(f"Solve: {a} {op} {b}")

    start = time.time()
    try:
        answer = int(input("Your answer: "))
    except:
        print("❌ Invalid!")
        answer = None

    time_taken = time.time() - start

    if answer == correct:
        damage = max(1, int(5 - time_taken))  # schneller = mehr Schaden
        enemy_hp -= damage
        print(f"⚔️ You hit for {damage}!")
    else:
        print("❌ Wrong! No damage.")

    # Gegner greift an
    enemy_damage = random.randint(2, 5)
    player_hp -= enemy_damage
    print(f"👾 Enemy hits you for {enemy_damage}")

print("\n💀 Game Over!" if player_hp <= 0 else "\n🎉 You win!")