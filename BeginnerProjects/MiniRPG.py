import random

player_hp = 20
player_attack = 5
gold = 0
xp = 0
level = 1

def new_enemy():
    return {
        "name": random.choice(["Goblin", "Orc", "Slime"]),
        "hp": random.randint(5, 15),
        "attack": random.randint(2, 5)
    }

def level_up():
    global level, player_hp, player_attack, xp
    if xp >= level * 10:
        level += 1
        xp = 0
        player_hp += 5
        player_attack += 1
        print("⬆️ LEVEL UP!")

while player_hp > 0:
    enemy = new_enemy()
    print(f"\n⚔️ A wild {enemy['name']} appears!")

    while enemy["hp"] > 0 and player_hp > 0:
        print(f"\n❤️ HP: {player_hp} | ⚔️ ATK: {player_attack} | 💰 Gold: {gold} | ⭐ XP: {xp}")
        print(f"{enemy['name']} HP: {enemy['hp']}")

        action = input("1=Attack  2=Run: ")

        if action == "1":
            damage = random.randint(2, player_attack)
            enemy["hp"] -= damage
            print(f"You hit for {damage}")

            if enemy["hp"] <= 0:
                print("💀 Enemy defeated!")
                reward = random.randint(5, 10)
                gold += reward
                xp += 5
                print(f"💰 You got {reward} gold!")
                break

            enemy_damage = random.randint(1, enemy["attack"])
            player_hp -= enemy_damage
            print(f"Enemy hits you for {enemy_damage}")

        elif action == "2":
            print("🏃 You escaped!")
            break

    level_up()

print("💀 Game Over")