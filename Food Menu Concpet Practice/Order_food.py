from Menu import *

# This function displays the menu items and their prices in a formatted way.
def display_menu():
    print("Meal Item:")
    for item, price in Meal_Item.items():
        print(f"{item}: ${price:.2f}")
    print("\nDrink Item:")
    for item, price in Drink_Item.items():
        print(f"{item}: ${price:.2f}")
    print("\nDessert Item:")
    for item, price in Dessert_Item.items():
        print(f"{item}: ${price:.2f}")


#This function allows user to select food item
def take_order():
    while True:
        print("1. Show Menu\n" \
        "2. Exit")
        user = int(input("Option: "))
        if user == 1:
            display_menu()
            
            # a nested loop to order multiple items just by typing their name and quantity
            while True:
                order = input("Item: ")
                if order in Menu:
                    quantity = int(input("Quantity: "))
                    price = Menu[order] # this gets the price of the ordered item from the Menu dictionary
                elif order.lower() == "done":
                   # Showing the total bill for the order 
                    total_bill = 0 # by default
                    for item in Menu: # created a for loop to get the total bill
                        if item in Menu:
                            total_bill += Menu[item] * quantity # adds the price of each item to the total bill 
                    # to print it only one time
                    print(f"Total Bill: ${total_bill:.2f}$") 
                    confitmation = input("Confirm order?: ")
                    if confitmation.lower() == "yes":
                        print("Thank you for your order!")
                        print('\n') # For maintaining a gap
                        break
                    else:
                        print("Order cancelled.")
                        print('\n')
                        break
                else:
                    print("The item is not in the menu")
               
            
        elif user == 2:
            break
        else: 
            print("Invalid command")

take_order()