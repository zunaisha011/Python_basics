# Task-1. You are tasked with creating a Python program to represent vehicles using a class. Each car should have attributes for maximum speed and mileage
class car:
    def __init__(self,max_speed,mileage):
        self.max_peed=max_speed
        self.mileage=mileage


# Update the class with the default color for all vehicles," white".
class car:
    color='black'
    def __init__(self,max_speed,mileage):
        self.max_peed=max_speed
        self.mileage=mileage



# Additionally, you need to create methods in the Vehicle class to assign seating capacity to a vehicle.
class car:
    color='black'
    def __init__(self,max_speed,mileage):
        self.max_peed=max_speed
        self.mileage=mileage
    def capacity(self,seating_capacity):
        self.seating_capacity=seating_capacity
def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)




# Additionally, you need to create two objects of the Vehicle class object that should have a max speed of 200kmph and mileage of 20kmpl with five seating capacities, and another car object should have a max speed of 180kmph and mileage of 25kmpl with four seating capacities.
class Vehicle:
    color = "white"
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None
    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity
    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)
vehicle1 = Vehicle(200, 20)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()
