class Vehicle:
    """
    A base class for vehicles with a common 'move' action.
    """
    def __init__(self, name):
        """
        Initializes the vehicle with a name.
        """
        self.name = name

    def move(self):
        """
        A generic move action that can be overridden by subclasses.
        """
        print(f"{self.name} is moving.")

class Car(Vehicle):
    """
    Represents a car, a type of vehicle.
    """
    def move(self):
        """
        Defines the specific move action for a car.
        """
        print(f"{self.name} is Driving 🚗")

class Plane(Vehicle):
    """
    Represents a plane, a type of vehicle.
    """
    def move(self):
        """
        Defines the specific move action for a plane.
        """
        print(f"{self.name} is Flying ✈️")

class Boat(Vehicle):
    """
    Represents a boat, a type of vehicle.
    """
    def move(self):
        """
        Defines the specific move action for a boat.
        """
        print(f"{self.name} is Sailing ⛵")

class Bicycle(Vehicle):
    """
    Represents a bicycle, a type of vehicle.
    """
    def move(self):
        """
        Defines the specific move action for a bicycle.
        """
        print(f"{self.name} is Pedaling 🚴")

# Create instances of different vehicle types
my_car = Car("My Sedan")
my_plane = Plane("Boeing 747")
my_boat = Boat("Sailor's Delight")
my_bicycle = Bicycle("Mountain Rider")

# Call the move() method on each object
my_car.move()
my_plane.move()
my_boat.move()
my_bicycle.move()

# Demonstrate polymorphism by iterating through a list of vehicles
vehicles = [my_car, my_plane, my_boat, my_bicycle]

print("\nDemonstrating Polymorphism:")
for vehicle in vehicles:
    vehicle.move()