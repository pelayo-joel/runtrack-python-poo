import math

class Cercle:
    def __init__(self, r:int):
        self.rayon = r


    #Changes the radius of the circle
    def ChangerRayon(self, newR:int):
        self.rayon = newR

    """Self explanatory method names"""
    def AfficherInfos(self):
        return f"Rayon: {self.rayon}, Circonference: {self.Circonference()}, Aire: {self.Aire()}, Diametre: {self.Diametre()}"

    def Circonference(self):
        return  math.pi * (self.rayon * 2)
    
    def Aire(self):
        return math.pi * self.rayon**2
    
    def Diametre(self):
        return self.rayon * 2
    

#Demonstrates the class
cercle1 = Cercle(4)
cercle2 = Cercle(7)

print(f"Cercle 1: \n{cercle1.AfficherInfos()}")
print(f"Cercle 2: \n{cercle2.AfficherInfos()}")