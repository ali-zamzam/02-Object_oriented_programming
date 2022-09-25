"""built in methods"""

# Thanks to the dir(object) command, we can get an overview of some predefined methods common to all Python objects.

print(dir(object))

"""__str__ method"""

# - One of the most practical methods is the __str__ method which is called automatically when the user issues
# the print command on an object. This method returns a string that represents the object that called it.
# - All classes in Python on which we can apply the print function have this method in their definition.

i = 10
print(i.__str__())  # '10'

tab = [1, 2, 3, 4, 5, 6]
print(tab.__str__())  # "[1, 2 , 3, 4, 5, 6]"


"""When we define our own class, it is preferable to define an __str__ method to it 
rather than a display type method as we did previously."""


class Complexe:
    def __init__(self, a=0, b=0):
        self.partie_re = a
        self.partie_im = b

    def __str__(self):
        if self.partie_im < 0:
            return (
                self.partie_re.__str__() + self.partie_im.__str__() + "i"
            )  # renvoie 'a' '-b' 'i'

        if self.partie_im == 0:
            return self.partie_re.__str__()  # renvoie 'a'

        if self.partie_im > 0:
            return (
                self.partie_re.__str__() + "+" + self.partie_im.__str__() + "i"
            )  # renvoie 'a' '+' 'b' + 'i'


z = Complexe(6, -3)
print(z)

# -------------------------------------------------------------------------------------------
"""comparison methods"""
# __le__ / __ge__: lesser or equal / greater or equal
# __lt__ / __gt__: lesser than / greater than
# __eq__ / __ne__ : equals / not equal

x = 5
y = 3

print(x > y)  # True
# or
print(x.__gt__(y))  # True

print(x < y)  # False
# or
print(x.__lt__(y))  # False


import numpy as np


class Complexe:
    def __init__(self, a=0, b=0):
        self.partie_re = a
        self.partie_im = b

    def __str__(self):
        if self.partie_im < 0:
            return self.partie_re.__str__() + self.partie_im.__str__() + "i"

        if self.partie_im == 0:
            return self.partie_re.__str__()

        if self.partie_im > 0:
            return self.partie_re.__str__() + "+" + self.partie_im.__str__() + "i"

    def mod(self):
        return np.sqrt(
            self.partie_re**2 + self.partie_im**2
        )  # renvoie (sqrt(a² + b²))

    def __lt__(self, other):
        if self.mod() < other.mod():  # renvoie True si |self| < |other|
            return True
        else:
            return False

    def __gt__(self, other):
        if self.mod() > other.mod():  # renvoie True si |self| > |other|
            return True
        else:
            return False


z1 = Complexe(3, 4)
z2 = Complexe(2, 5)
print(z1 > z2)
print(z1 < z2)
print(z1.__str__())  # 3+4i
