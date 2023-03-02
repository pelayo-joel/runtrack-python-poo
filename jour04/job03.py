class Rectangle:
    def __init__(self):
        self._width, self._length = 0, 0


    '''Public methods'''

    def Perimeter(self):
        return self._length * 2 + self._width * 2
    

    def Surface(self):
        return self._length * self._width
    

    #Getters/Setters

    def GetWidth(self):
        return self._width
    
    def SetWidth(self, newWidth:int):
        self._width = newWidth

    def GetLength(self):
        return self._length
    
    def SetLength(self, newLength:int):
        self._length = newLength

    



class Parallelepipede(Rectangle):
    def __init__(self):
        super().__init__()

        self.__height = 0


    '''Public methods'''

    def Volume(self):
        return self.Surface() * self.__height
    

    #Getters/Setters

    def GetHeight(self):
        return self.__height
    
    def SetHeight(self, newHeight:int):
        self.__height = newHeight


#Demonstrates 'Rectangle' and 'Parallelepipede' class
rect = Rectangle()
parallel = Parallelepipede()

rect.SetWidth(4)
rect.SetLength(8)

print(f"Width: {rect.GetWidth()}, Length: {rect.GetLength()}")
print(f"Perimeter: {rect.Perimeter()}, Surface: {rect.Surface()}\n")


parallel.SetWidth(5)
parallel.SetLength(11)
parallel.SetHeight(3)

print(f"Width: {parallel.GetWidth()}, Length: {parallel.GetLength()}, Height: {parallel.GetHeight()}")
print(f"Volume: {parallel.Volume()}")