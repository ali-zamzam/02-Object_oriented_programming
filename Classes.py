# """Objects and classes"""

"""
In Python and many other programming languages, object-oriented programming involves creating
classes of objects that contain specific information and tools suitable for manipulating them."""

"""class"""


class Vehicle:  # Vehicle class definition

    """init is the method of the class

    -The __init__ method takes as arguments the variables that will define the attributes
     of an instance when it is created.
    -The init method is automatically called when instantiating any class.
    -All methods defined within a class have the self argument as their first parameter.
    -This parameter is used to tell the method which instance called it."""

    # class attribute
    mark = "audi"

    def __init__(self, passengers, seats, colors, model, horsepower):
        """instance attributes"""
        self.passengers = passengers  # passengers list
        self.seats = seats  # number of seats
        self.color = colors
        self.model = model
        self.horsepower = horsepower

    def print_passengers(self):
        for i in range(len(self.passengers)):
            print(self.passengers[i])

    # Defining a method to change the color of a car
    def change_color(self, new_color):
        print(f"we change the color from {self.color} to {new_color}")

    # to add a new value to the list
    def add(self, name):  # new method for adding a new name
        self.passengers.append(name)


"""instance"""
voiture1 = Vehicle(["Pierre", "Adrian"], 4, "orange", "ford", "200")

"""seats and passengers are the attributes"""
print(voiture1.seats)
# 4

print(voiture1.passengers)
# ['Pierre', 'Adrian']

"""we use the class because mark is a class attribute we don't use class instance"""
print(Vehicle.mark)
# audi

voiture2 = Vehicle(["Dimitri", "Charles", "Yohan"], 4, "yellow", "ford", "200")

print(voiture2.seats)  # Affichage de l'attribut seats
voiture2.print_passengers()  # Execution de la méthode print_passengers

voiture1.change_color("blue")
# we change the color from Orange to blue

voiture1.add("ali")
voiture1.print_passengers()
# # ------------------------------------------------------------------------------------------------
# # Definition of the Car class
# class Cars:
#     # Definition of the constructor of the Car class
#     def __init__(self, color, model, horsepower):
#         # Initialization of class attributes with constructor arguments
#         self.color = color
#         self.model = model
#         self.horsepower = horsepower

#     # Defining a method to change the color of a car
#     def change_color(self, new_color):
#         print(f" we change the color from {self.color} to {new_color}")


# voiture = Cars("Orange", "audi", 250)
# voiture.change_color("blue")
# # we change the color from Orange to blue

# # ------------------------------------------------------------------------------------------------
# class Complexe:
#     def __init__(self, a, b):
#         self.partie_re = a
#         self.partie_im = b

#     def afficher(self):
#         if self.partie_im < 0:
#             print(f"{self.partie_re} - {-self.partie_im} i")

#         if self.partie_im == 0:
#             print(self.partie_re)

#         if self.partie_im > 0:
#             print(f"{self.partie_re}+ {self.partie_im} i")


# val1 = Complexe(4, 5)  # a = 4 , b = 5
# val2 = Complexe(3, -2)  # a = 3 , b = -2

# val1.afficher()
# val2.afficher()
# # ------------------------------------------------------------------------------------------------
# class Animal:
#     # When defining a class's attributes, if they are preceded by __, it means they are private
#     __name = ""
#     __height = 0
#     __weight = 0
#     __sound = 0

#     # Defining functions inside a class

#     # Constructor with parameters
#     def __init__(self, name, height, weight, sound):
#         self.__name = name
#         self.__height = height
#         self.__weight = weight
#         self.__sound = sound

#     # Encapsulation with set and get functions:
#     # Use the template 'props' in pyCharm to help writing them
#     def get_name(self):
#         return self.__name

#     def set_name(self, name):
#         self.__name = name

#     def get_height(self):
#         return self.__height

#     def set_height(self, height):
#         self.__height = height

#     def get_weight(self):
#         return self.__weight

#     def set_weight(self, weight):
#         self.__weight = weight

#     def get_sound(self):
#         return self.__sound

#     def set_sound(self, sound):
#         self.__sound = sound

#     # To use polymorphism, we will define a function, get_type, that will print the class name of the object
#     def get_type(self):
#         print("Animal")

#     # to print all properties of an object we will create a toSting method:
#     def toString(self):
#         # as this method exists inside the class, it is not necessary to call the getters to obtain the information
#         return "{} is {} cm tall and {} kilograms and says {}".format(
#             self.__name, self.__height, self.__weight, self.__sound
#         )


# # Declaring and initializing an Object based on the class we just created
# cat = Animal("Whiskers", 33, 10, "Meow")

# # Calling one of the methods from the Object
# print(cat.toString())

# # INHERITANCE

# # To inherit from a class, we write the superclass in parentheses after the name of the subclass
# class Dog(Animal):
#     # once the inheritance is declared, the subclass gets all the variables and functions from the superclass
#     __owner = ""

#     # Overriding the constructor of the animal class
#     def __init__(self, name, height, weight, sound, owner):
#         self.__owner = owner
#         # To determine that some of the objects variables will be handled by the superclass's constructor:
#         super(Dog, self).__init__(name, height, weight, sound)

#     # Writing getters and setters for variables that are not inherited:
#     def get_owner(self):
#         return self.__owner

#     def set_owner(self, owner):
#         self.__owner = owner

#     # Defining the get_type function:
#     def get_type(self):
#         print("Dog")

#     # Overriding the toString() function:
#     # It is necessary to use the getter methods to invoke the superclass's properties.
#     def toString(self):
#         return "{} is {} cm tall and {} kilograms and says {}. His owner is {}".format(
#             self.get_name(),
#             self.get_height(),
#             self.get_weight(),
#             self.get_sound,
#             self.__owner,
#         )

#     # Method overloading
#     def multiple_sounds(self, how_many=None):
#         if how_many is None:
#             print(self.get_sound)
#         else:
#             print(self.get_sound() * how_many)


# # Creating an object based on the subclass we just created

# spot = Dog("spot", 53, 27, "ruff", "rurtubiac")

# print(spot.toString())


# # POLYMORPHISM

# # allows us to refer to objects as their superclass and get their functions automatically
# class AnimalTesting:
#     def get_type(self, animal):
#         animal.get_type()


# test_animals = AnimalTesting()

# test_animals.get_type(cat)
# test_animals.get_type(spot)


# spot.multiple_sounds(4)
# print()
# spot.multiple_sounds()

# # -------------------------------------------------------------------------------------------------------------------------------
# class EpisodeDrWho:
#     """
#     Un épisode du Docteur Who
#     """


# ep = EpisodeDrWho()

# ep.saison = 7
# ep.episode = 5


# print(ep.saison)


# class SerieTele:
#     def diffuser(self):
#         print("désolé, je n'ai pas la télé !")


# class EpisodeDrWho(SerieTele):
#     """
#     Un épisode du Docteur Who
#     """

#     def __init__(self, saison, episode):
#         self.saison = saison
#         self.episode = episode

#     def attaque_dalek(self):

#         print("au secours ! Attaque de Dalek dans l'épisode", self.saison, self.episode)
#         self.dalek()

#     def dalek(self):
#         print(self)
#         print("au secours")


# p = EpisodeDrWho(saison=7, episode=5)
# d = EpisodeDrWho(saison=7, episode=5)

# p.attaque_dalek()

# d.attaque_dalek()
# # --------------------------------------------------------------------------------
"""attributes"""
# position, name, age, level,salary

class DataEngineer:

    # class attribute
    nick_name = "Keyboard Manager"

    def __init__(self, prenom, age, level, salary):
        # instance attributes
        self.name = prenom
        self.age = age
        self.level = level
        self.salary = salary

    def code(self):
        print(f"{self.name} is writing code")

    def code_language(self, language):
        print(f"{self.name} is writing in {language}language")

    def salary(age):
        if age < 25:
            return 2000
        if age < 30:
            return 3000
        return 4000  # else return 4000

    # def information(self):
    #     information = f"name = {self.name} , age = {self.age}, level = {self.level}"
    #     return information

    # with this method we can get information without use a function to have the information
    def __str__(self):
        information = f"name = {self.name} , age = {self.age}, level = {self.level}"
        return information

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def set_salaire(self, value):
        self._salaire = value

    def get_salaire(self):
        return self._salaire


# create instance of class DataEngineer
de1 = DataEngineer("ali", 30, "junior", 3000)

"""name not prenom because we use the value of self (self.name)
instead the value in __init(self, prenom)"""
print(de1.name, de1.level)
# ali junior
print(de1.nick_name)
# Keyboard Manager
# or
print(DataEngineer.nick_name)
# Keyboard Manager

de1.code()
# ali is writing code

de2 = DataEngineer("aliz", 30, "junior", 3000)
de2.code()
# aliz is writing code

"""because we have a (language) in def code_language so we need to put the language(python or c++..)"""
de1.code_language("python")
# ali is writing in python language


"""if we have a function we need to do this"""
# we use print because we had a return (return information)
# print(de1.information())
# name = ali , age = 30, level = junior

"""because we use def __str__ we can print the strings like that"""
print(de2)
# name = aliz , age = 30, level = junior

# if we had another de and it's equal to another de
de3 = DataEngineer("ali", 30, "junior", 3000)
# print(de1 == de3) #output false#
# the output is **false** because it's not the same memory adress

"""so we use __eq__ to check equality"""
# for example in __eq__ we will check age and name
print(de1 == de3)  # output True


"""here if we have an instance (def salary(age)
we need to use the class like the def __init__"""
print(DataEngineer.salary(27))
# 3000

de1.set_salaire(7000)
print(de1.get_salaire())
# -------------------------------------------------------------------------------------------


class car:
    def __init__(self, a, b=[]):
        self.seats = a
        self.passengers = b

    def print_passengers(self):
        for i in range(len(self.passengers)):
            print(self.passengers[i])

    def add(self, name):  # Nouvelle méthode
        self.passengers.append(name)


voiture1 = car(4, ["Charles", "Paul"])  # declaration de l'instance voiture1
voiture1.add("Raphaël")  # ajout de 'Raphaël' dans la liste des passagers
