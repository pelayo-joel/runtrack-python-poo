"""Class 'Operation'"""
class Operation:
    def __init__(self, n1:int=0, n2:int=0):
        self.nombre1, self.nombre2 = n1, n2


    #Sum both attributes of this class (for Job03)
    def addition(self):
        return self.nombre1 + self.nombre2


print(Operation(0, 0)) 