from Base_Data import *

print("       Base Control System         ")



while True:
    Admin = input("Command: ").strip()

    if Admin == "Show total room":
        print(f"Total Room: {room}")
    elif Admin == "Shutdown":
        break
    elif Admin == "Open Main Gate":
        main_gate_open = True
        print("Main Gate Opened")
    elif Admin == "Close Main Gate":
        main_gate_open = False
        print("Main Gate Closed")
    elif Admin == "Show Food Supply":
       for food_data in food_supply:
         for food in food_data:
             print(food)
    elif Admin == "Turn On Light":
        light_on = True
        print("Light Turned On")
    elif Admin == "Turn Off Light":
        light_on = False
        print("Light Turned Off")
    elif Admin == "Show Base people":
        for residents in resident_info:
            for resident in residents:
                print(resident, residents[resident])
    else:
        print("Invalid Command")

