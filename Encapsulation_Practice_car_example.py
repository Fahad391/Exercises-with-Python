class Car:
    def __init__(self, Brand, Model):
        self.brand = Brand
        self.model = Model
        self.__speed = 0 # used Encapsulation to make it private

    def accelerate(self, acc_value):
        if acc_value < 0:
            print("Acceleration cannot be a negative number")
        elif acc_value == 0:
                print("Acceleration Cannot be zero")
        else:
            self.__speed += acc_value # value adds with the current value, no override
            print(f"Acceleration set to {self.__speed} km/hr")


    def press_break(self):
        self.__speed  = 0
        print("Stopped")
# used getter and setter method to access the private variable
    def get_speed(self):
        print(f"Speed is set to {self.__speed} km/hr")

    def set_speed(self, set_value):
        if set_value <= 0:
            print("Speed cannot be negative nor Zero. Better Press Break")
        elif set_value == self.__speed:
                print(f"Speed is already at {self.__speed} km/hr")
        else:
            self.__speed = set_value # Input value is stored here. Also can store new value overriding the old one

car1 = Car("BYD", "Sealion")
car1.set_speed(30)
car1.get_speed()
car1.accelerate(5) # speed is increase by 5 
car1.set_speed(35)
car1.set_speed(10) # new value overrides the new value
car1.get_speed()
car1.accelerate(5)
