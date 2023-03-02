class Forme:
    def __init__(self):
        pass


    '''Public methods'''

    def Area(self):
        return 0
    




class Rectangle(Forme):
    def __init__(self, width:int, height:int):
        super().__init__()
        self.__width, self.__height = width, height


    '''Public methods'''

    def Area(self):
        return self.__width * self.__height
    

#Demonstrates 'Rectangle' class
rect = Rectangle(4, 6)

print(f"Aire: {rect.Area()}")