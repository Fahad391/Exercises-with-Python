print("       Military Base Management         ")

Bases = [{"Base" : "Kurt Vadsi", "Total Troops" : 1000, "Food Supply": f"{15} days", "Ammunition" : f"{20} days"},
        {"Base" : "Dalan Zamd", "Total Troops" : 2900, "Food Supply": f"{48} days", "Ammunition" : f"{48} days"}]


while True:
    cmd = input("Command: ")

    if cmd == "Bases info":
        for Base in Bases:
            name = Base["Base"]
            troops = Base["Total Troops"]
            food = Base["Food Supply"]
            ammo = Base["Ammunition"]
            
            print(f"Base Name: {name}, Total Troops: {troops}, Food Supply: {food}, Ammunition: {ammo}")
    elif cmd == "exit":
        break

    elif cmd == "Search":      
        target = input("Enter base name: ")
        found = False
        for base in Bases:
            if base["Base"].lower() == target.lower():
                print(f"Match found! Troops: {base['Total Troops']}, Food Supply: {base['Food Supply']}, Ammunition: {base['Ammunition']}")
                found = True
        if not found:
            print("Base not found.")
    elif cmd == "Update troops":
        target = input("Enter Base Name: ")
        found = False
        try:
            for base in Bases:
                if base["Base"].lower() == target.lower():
                    found = True
                    update_total_troops = int(input(f"Current Troops: {base['Total Troops']}, New count: "))
                    if update_total_troops < 0:
                        print("Troops count cannot be negative.")
                    else:
                        base["Total Troops"] = update_total_troops
                        print(f"Troops count updated to {update_total_troops}.")
            if not found:
                print("Base not found.")

        except ValueError:
            print("It must be a positive integer")
    elif cmd == "Update food":
        target = input("Enter Base Name: ")
        found = False
        try:
            for base in Bases:
                if base["Base"].lower() == target.lower():
                    found = True
                    update_food_supply = int(input(f"Current Food Supply: {base['Food Supply']}, New count (in days): "))
                    if update_food_supply < 0:
                        print("Food supply cannot be negative.")
                    else:
                        base["Food Supply"] = f"{update_food_supply} days"
                        print(f"Food supply updated to {update_food_supply} days.")
            if not found:
                print("Base not found.")

        except ValueError:
            print("It must be a positive integer")
    elif cmd == "Update ammo":
        target = input("Enter Base Name: ")
        found = False
        try:
            for base in Bases:
                if base["Base"].lower() == target.lower():
                    found = True
                    update_ammo_supply = int(input(f"Current Ammunition Supply: {base['Ammunition']}, New count (in days): "))
                    if update_ammo_supply < 0:
                        print("Ammunition supply cannot be negative.")
                    else:
                        base["Ammunition"] = f"{update_ammo_supply} days"
                        print(f"Ammunition supply updated to {update_ammo_supply} days.")
            if not found:
                print("Base not found.")

        except ValueError:
            print("It must be a positive integer")
    elif cmd == "Total Strength":
        total_force = 0
        for base in Bases:
            total_force += base["Total Troops"]
        print(f"Total Military Personnel: {total_force}")
    elif cmd == "Command list":
        print("Available Commands:")
        print("1. Bases info - Display information about all bases.")
        print("2. Search - Search for a specific base by name.")
        print("3. Update troops - Update the number of troops at a specific base.")
        print("4. Update food - Update the food supply (in days) at a specific base.")
        print("5. Update ammo - Update the ammunition supply (in days) at a specific base.")
        print("6. Total Strength - Calculate and display the total military personnel across all bases.")
        print("7. Command list - Display this list of available commands.")
        print("8. exit - Exit the program.")
    else:
        print("Invalid command. Please try again.")
