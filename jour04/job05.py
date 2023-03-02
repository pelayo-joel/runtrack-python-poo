import math
from job04 import *



class Cercle(Forme):
    def __init__(self, radius:int):
        super().__init__()
        self.__radius = radius


    '''Public methods'''

    def Area(self):
        return math.pi * self.__radius**2
    

#Demonstrates 'Rectangle' and 'Cercle'
rect = Rectangle(3, 7)
circle = Cercle(4)

print(f"Rectangle area: {rect.Area()}, Circle area: {circle.Area()}")