class Point:
    def __init__(self, x:int, y:int):
        self.x, self.y = x, y


    #Prints the coordinates of the instantiated point
    def AfficherLesPoints(self):
        print((self.x, self.y)) 
    
    #Prints the x coordinates
    def AfficherX(self):
        print(self.x)

    #Prints the y coordinates
    def AfficherY(self):
        print(self.y)

    #Allow you to change the x coordinates
    def ChangerX(self, newX:int):
        self.x = newX

    #Allow you to change the y coordinates
    def ChangerY(self, newY:int):
        self.y = newY


#Makes use of all the different methods of the 'Cercle' class 
point = Point(5, 9)

point.AfficherLesPoints()
point.AfficherX()
point.AfficherY()

point.ChangerX(2)
point.ChangerY(16)
point.AfficherLesPoints()