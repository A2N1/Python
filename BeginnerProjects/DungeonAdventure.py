import random

player_hp = 20
inventory = []

monsters = ["Goblin", "Skeleton", "Zombie"]
items = ["Potion", "Sword", "Shield"]

print("Welcome to the Dungeon!")

while player_hp > 0:
    print("\nYou walk into a new room...")
    
    event = random.choice(["monster", "item", "nothing"])

    if event == "monster":
        monster = random.choice(monsters)
        monster_hp = random.randint(5, 12)
        print(f"A {monster} appears!")

        while monster_hp > 0:
            action = input("Do you want to (attack/run)? ").lower()

            if action == "attack":
                damage = random.randint(3, 8)
                monster_hp -= damage
                print(f"You hit the {monster} for {damage} damage!")

                if monster_hp <= 0:
                    print(f"You defeated the {monster}!")
                    break

                monster_damage = random.randint(2, 6)
                player_hp -= monster_damage
                print(f"The {monster} hits you for {monster_damage} damage!")

            elif action == "run":
                print("You escaped!")
                break

        print(f"Your HP: {player_hp}")

    elif event == "item":
        item = random.choice(items)
        print(f"You found a {item}!")
        inventory.append(item)

    else:
        print("The room is empty...")

    print("Inventory:", inventory)

print("\nGame Over 💀")