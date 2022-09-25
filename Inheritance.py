"""Inheritance"""

"""Inheritance consists of creating a subclass from an existing class. 
We say that this new class inherits from the first because it will automatically 
have the same attributes and methods."""

# ------------------------------------------------------------------------------------------------
"""We can define a Motorcycle class that inherits from the Vehicle class (from classes.py) in the following way:"""
from Classes import car

## the class moto inherits from the Vehicle class ##
""" we know that in the Vehicle class the seats = 4 but here we inherit so no need to but seats in( __init(self,..))"""
# what we use from the Vehicle class we need to put it as we want in class moto(color = red for example)
# and we can use the method to change the color from class vehicle
# we didn't use horsepower because we don't want to have it in class moto

"""question"""
# Define in the Moto class an add method which will add a name passed as an argument in the list of passengers
# by checking that there are still places available. If there are no spaces left on the Motorcycle,
# it will display The vehicle is full. If there are any left, the method will add the name to the list
# and display the number of places left.


class moto(Vehicle):
    def __init__(self, c, d):
        self.seats = 2
        self.color = "red"
        self.passengers = c
        self.type = d

    def add(self, name):  # new method for adding a new passenger
        if len(self.passengers) < self.seats:
            self.passengers.append(name)
            print(f"ther's more seats for you {name}")
        else:
            print("sorry we don't have seats left")


moto1 = moto(["ali"], "two wheels")
moto1.add("hasan")
moto1.change_color("black")
moto1.print_passengers()


moto2 = moto(["aliz"], "Three wheels")
moto2.add("ali")
# ther's more seats for you ali

moto2.print_passengers()
# aliz
# ali
moto2.add("hasan")
# sorry we don't have seats left

# # ------------------------------------------------------------------------------------------------------------
# To inherit from a class, we write the superclass in parentheses after the name of the subclass
class Dog(Animal):
    # once the inheritance is declared, the subclass gets all the variables and functions from the superclass
    __owner = ""

    # Overriding the constructor of the animal class
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        # To determine that some of the objects variables will be handled by the superclass's constructor:
        super(Dog, self).__init__(name, height, weight, sound)

    # Writing getters and setters for variables that are not inherited:
    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    # Defining the get_type function:
    def get_type(self):
        print("Dog")

    # Overriding the toString() function:
    # It is necessary to use the getter methods to invoke the superclass's properties.
    def toString(self):
        return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(
            self.get_name(),
            self.get_height(),
            self.get_weight(),
            self.get_sound,
            self.__owner,
        )

    # Method overloading
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound() * how_many)


# Creating an object based on the subclass we just created

spot = Dog("spot", 53, 27, "ruff", "rurtubiac")

print(spot.toString())


# -------------------------------------------------------------------------------------------
class Moto(car):
    def __init__(self, b, c):
        self.seats = 2
        self.passengers = b
        self.brand = c

    def add(self, name):
        if len(self.passengers) < self.seats:
            self.passengers.append(name)
            print("Il reste", self.seats - len(self.passengers), "places")
        else:
            print("Le véhicule est rempli")


Moto1 = Moto(["Pierre", "Dimitri"], "Yamaha")

Moto1 = Moto(["Pierre", "Dimitri"], "Yamaha")
Moto1.add("Yohann")
Moto1.print_passengers()


Moto2 = Moto(["ali"], "Honda")
Moto2.print_passengers()
Moto2.add("Dimitri")
Moto2.add("ali")
Moto2.add("ali")
Moto2.print_passengers()


# Create a Convoi class which will contain 2 attributes: The first, named vehicle_list is a list of Vehicle type instances
# and the second length is the total number of vehicles in the Convoy. A convoy will be automatically initialized with 1 4-seater vehicle without passengers.


class Convoi:
    def __init__(self):
        self.vehicule_list = []
        self.vehicule_list.append(car(4))
        self.length = 1

    # Define in the Convoy class a method add_vehicule which will add a Vehicle type object at the end of the list of vehicles in the convoy.
    # Do not forget to update the length of the convoi.
    def add_vehicule(self, vehicule):
        self.vehicule_list.append(vehicule)
        self.length = self.length + 1


# Initialize a convoi1 instance of the Convoy class.
# Add the passenger "Albert" in the first vehicle of the convoy1 instance.
# Add a "Honda" motorbike to convoy1 which will be driven by "Raphael".

convoi2 = Convoi()

convoi2.vehicule_list[0].add("Albert")

convoi2.add_vehicule(Moto(["Raphael"], "Honda"))


# Write a small script that will display all passengers in convoy1.
for vehicule in convoi2.vehicule_list:
    vehicule.print_passengers()
