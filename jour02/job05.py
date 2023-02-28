import time

class Voiture:
    def __init__(self, brand:str, model:str, year:int, kilometers:int):
        self.__brand, self.__model = brand, model
        self.__year, self.__kilometers = year, kilometers
        self.__isStarted = False
        self.__tank = 50


    '''Public methods'''
    def Demarrer(self):
        if self.__isStarted:
            print(f"Already started")
            return None
        
        print("Starting up...")
        time.sleep(2)

        if self.__VerifierPlein() > 5:
            self.__isStarted = True
            self.__tank -= 45
            print(f"Let's roll")
            time.sleep(2)

        else:
            print(f"Not enough fuel. Tank level: {self.__tank}\n")

    def Arreter(self):
        if not self.__isStarted:
            print(f"Already stopped")
            return None
        
        self.__isStarted = False
        print(f"Successfully stopped")

    #Getter methods
    def GetBrand(self):
        return self.__brand
    
    def GetModel(self):
        return self.__model
    
    def GetYear(self):
        return self.__year
    
    def GetKilometers(self):
        return self.__kilometers
    
    def GetIfWorking(self):
        return self.__isStarted
    

    '''Private methods'''
    def __VerifierPlein(self):
        return self.__tank
    

#Demonstrates the 'Voiture' class
myCar = Voiture("Fiat", "Panda I", 1980, 24567)
print(f"\nBrand: {myCar.GetBrand()}, Model: {myCar.GetModel()}")
print(f"Year: {myCar.GetYear()}, Kilometers travelled: {myCar.GetKilometers()}\n")

myCar.Demarrer()
myCar.Demarrer()

myCar.Arreter()

myCar.Demarrer()

