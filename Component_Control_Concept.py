# creating a class Armor
class Robotic_Armor:
   # Defining what it will take as input
    def __init__(self, model):
        self.model = model # Model numbers in alphanumeric order

    # Display info
    def about(self):
        print(f"Armor Model: {self.model}")

# creating another class for drone
class drone:
    # Defining what it will take as input
    def __init__(self, drone_type, battery_life, range):
        self.drone_type = drone_type
        self.battery_life = battery_life # in hours
        self.range = range # in Kilometers
    def about(self):
        print(f"Drone Type: {self.drone_type}\n",
              f"Battery Life: {self.battery_life} hours | Range: {self.range} KM")

#Creating 2 objects of Armor and Drone
Armor = Robotic_Armor("TW-98x+")
Drone = drone("Survelance", 72, 150)

# Creating a function to control both
def control():
    # Creating while loop to continue until told to stop
    while True:
        user = input ("Command: ")

        # Using Conditional Statements to define how it will work
        if user == "Armor info":
            Armor.about()
        elif user == "Drone info":
            Drone.about()
        elif user == "Quit":
            break
        elif user == "Get Armor":
            print(f"Unpacking Model {Armor.model}....")
            print(f"Armor on")
        elif user == "Armor off":
            print("Armor off...")
            print(f"Model {Armor.model} packed")
        elif user == "Drone info":
            Drone.about()
        elif user == "Cover Area":
            print(f"Covering within {Drone.range} KM Area")
        else:
            print("What?")

control()
