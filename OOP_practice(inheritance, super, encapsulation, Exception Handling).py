from abc import ABC, abstractmethod

#Parent or Root Class
class Vehicle(ABC):
    total_vehicles = 0 # Class variable

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

        Vehicle.total_vehicles += 1

    @abstractmethod
    def Engine_type(self):
        pass

    def vehicle_info(self):
            print(f"Brand: {self.brand} | Model: {self.model} | Color: {self.color}")

    @classmethod
    def Total_Vehicle(cls):
            print(f"Total Vehicle Owned: {cls.total_vehicles}")


class Car(Vehicle):
    def __init__(self, brand, model, color, seat, engineType):
        if not isinstance(seat, int): #raises an error if goes otherway
            raise ValueError("Seats must contain integer")
        super().__init__(brand, model, color)
        self.seat = seat
        self.__enginetype = engineType

    def Engine_type(self):
        return self.__enginetype
    
    # used super to inherit method from parent class
    def vehicle_info(self):
        super().vehicle_info()
        print(f"Seat: {self.seat}")

class Sports_Car(Car):
    def __init__(self, brand, model, color, seat, engineType, horse_power):
          if not isinstance(horse_power, (float, int)): # with this technique both float and int can be made accepted by the rule(takes 2 argument)
               raise ValueError("Horse Power must be a float number")
          super().__init__(brand, model, color, seat, engineType)
          self.horse_power = horse_power
    def Engine_type(self):
         return super().Engine_type()

    def vehicle_info(self):
        super().vehicle_info()
        print(f"Seat: {self.seat} | Horse Power: {self.horse_power}")
    

class Bike(Vehicle):
    def __init__(self, brand, model, color, engineType):
          super().__init__(brand, model, color)
          self.__enginetype = engineType

    def Engine_type(self):
            return self.__enginetype

    def vehicle_info(self):
         return super().vehicle_info()

class Sports_Bike(Bike):
    def __init__(self, brand, model, color, engineType, horse_power):
        if not isinstance(horse_power, (float, int)): 
            raise ValueError("Horse Power must be a float number")
        super().__init__(brand, model, color, engineType)
        self.horse_power = horse_power

    def Engine_type(self):
         return super().Engine_type()

    def vehicle_info(self):
        super().vehicle_info()
        print(f"Horse Power: {self.horse_power}")


          
# Using exception handling
try:
    #Objects of the classes

    car1 = Car("Toyota", "Camry", "Black", 5, "Hybrid")
    car2 = Car("BYD", "Sealion", "White", 7, "Electric")
    bike1 = Bike("Honda", "Shine", "Black", "Hybrid")
    sports_car1 = Sports_Car("Ferrari", "SF90 Stradale", "Red", 2, "Oil", 986)
    sports_bike1 = Sports_Bike("MV Augusta", "F4CC", "Red-White mix", "Gas", 147)

except ValueError as error:
     print(error) # Prints the message written in raise ValueError

Vehicle.Total_Vehicle() # Updates Class variable's value

#sports_car1.vehicle_info()
