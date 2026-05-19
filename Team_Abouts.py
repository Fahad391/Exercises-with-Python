class Team:
    def __init__(self, Team_Name, Total_Member):
        self.Team_Name = Team_Name
        self.Total_Member = Total_Member
        self.Members = [] # Holds Member Details

    # Adds Member's details int the Members List
    def include_Member(self, n, ag, D):
        self.Members.append({
            "Name" : n, "Age" : ag, "Designation" : D
        })

    # Shows Team Name, Total Member and Each Member's Details
    def display_Team_Abouts(self):
        print(f"Team {self.Team_Name}\nTotal Members -> {self.Total_Member}")
        print("\nMember Details\n")
        for member in self.Members:
            print(f"Name: {member['Name']}  Age: {member['Age']}  Designation: {member['Designation']}")

#Exception Handling to Tackle Errors + Objects of the Class
try: 
        # While loop for each input
        while True:
            Name_of_Team = input("Team Name: ")
            if Name_of_Team == "":
                print("Fill it up")
            else:
                break
        while True:
            try:
                Member_Total = int(input("Total Members: ")) 
                if Member_Total <= 0:
                    print("Must be a positive number greater than 0.")
                else:
                    break
            except ValueError:
                print("Invalid Input. Enter a valid number please")

        T = Team(Name_of_Team, Member_Total)

        # A For loop to add each Member's details
        for n in range(Member_Total):
            print(f"\nMember {n + 1} Details\n")

            while True:
                name = input("Name: ").strip()
                if name == "":
                     print("Name can't be Blank")
                else:
                     break
                
            while True: 
                try:
                    age = int(input("Age: "))
                    if age <= 0:
                        print("Age must be a positive number greater than 0.")
                    else:
                        break 
                except ValueError:
                    print("Invalid input. Please enter a valid number for age.")

            while True:
                Designation = input("Designation: ").strip()
                if Designation == "":
                     print("Designation can't be Blank")
                else:
                     break
            T.include_Member(name, age, Designation)

        # Displays Team Abouts
        T.display_Team_Abouts()

except Exception as e:
    print(e)
