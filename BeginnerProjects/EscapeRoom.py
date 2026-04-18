inventory = []
door_unlocked = False
has_key = False
safe_open = False

print("🚪 ESCAPE ROOM")
print("Type commands like: look, open, take, use")

while True:
    command = input("\n> ").lower()

    if command == "look":
        print("You see: a door, a table, a safe")

    elif command == "open table":
        if not has_key:
            print("You found a key!")
            inventory.append("key")
            has_key = True
        else:
            print("Nothing else here.")

    elif command == "open safe":
        if "code" in inventory:
            print("Safe already opened.")
        else:
            code = input("Enter 3-digit code: ")
            if code == "123":
                print("🔓 Safe opened! You found a note with a code!")
                inventory.append("code")
                safe_open = True
            else:
                print("❌ Wrong code!")

    elif command == "use key":
        if "key" in inventory:
            print("You unlocked the door!")
            door_unlocked = True
        else:
            print("You don't have a key!")

    elif command == "open door":
        if door_unlocked:
            print("🎉 You escaped!")
            break
        else:
            print("The door is locked.")

    elif command == "inventory":
        print("Inventory:", inventory)

    else:
        print("Unknown command.")