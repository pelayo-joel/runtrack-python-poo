class Rectangle:
    def __init__(self):
        self.__longueur, self.__largeur = None, None


    #Getters and Setters
    def SetLength(self, l:int):
        self.__longueur = l

    def SetWidth(self, w:int):
        self.__largeur = w

    def GetLength(self):
        return self.__longueur
    
    def GetWidth(self):
        return self.__largeur
    

#Demonstrates the 'Rectangle' class
rectangle1 = Rectangle()

rectangle1.SetLength(10)
rectangle1.SetWidth(5)
print(f"Longueur: {rectangle1.GetLength()}, Largeur: {rectangle1.GetWidth()}")

rectangle1.SetLength(8)
rectangle1.SetWidth(10)
print(f"Longueur: {rectangle1.GetLength()}, Largeur: {rectangle1.GetWidth()}")
