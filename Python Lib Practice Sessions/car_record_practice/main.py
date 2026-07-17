from Car_Analytics import Car_Tracker

tracker = Car_Tracker() # Instance class Car_Tracker

# Functions created to manage method os Car_Tracker 
def manage_add_cars():
    while True:
        brand = input("Brand: ").strip()
        model = input("Model: ").strip()

        # Inform the user if Brand or Model is empty.
        if not brand or not model:
            print("\nBrand and Model cannot be empty.")
            continue

        tracker.add_car(brand,model)
        
        choice = input("Add another?(yes/no): ").strip()
        if choice == "no":
            tracker.save_data() # Saves the data
            break

def manage_show_cars():
    df = tracker.show_all_cars()

    if df.empty:
        print("\nThere are no cars in the collection 🙁")
        return
    
    print("\n================== Car Collection ==================")

    # using for loop to print car details row by wo
    for index, row in df.iterrows():
        print(f"\nCar {index + 1}")
        print(f"Brand: {row['Brand']} | Model: {row['Model']}")
    print("====================================================")

    # Grab the calculation processed by NumPy
    stats = tracker.analyze()
    print(f"\nTotal Cars: {tracker.get_total_count()}")
    print(f"Unique Brands: {stats['total_unique']} ({', '.join(stats['brands_list'])})")

while True:
    print("\n============= Car Collection ==============")
    print("1. Add Car")
    print("2. Show All Cars")
    print("3. Exit")

    command = input("Option: ").strip()

    if command == "1":
        manage_add_cars()
    elif command == "2":
        manage_show_cars()
    elif command == "3":
        break
    else:
        print("Invalid option!")
