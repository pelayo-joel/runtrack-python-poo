class Vehicle:
    def __init__(self, brand:str, model:str, year:int, price:float):
        self._brand, self._model = brand, model
        self._year, self._price = year, price


    '''Public methods'''

    def VehicleInfos(self):
        print(f"\nMarque: {self._brand}, Modele: {self._model}")
        print(f"Annee: {self._year}")
        print(f"Prix: {self._price}")


    def Start(self):
        print(f"Attention, je roule")




class Voiture(Vehicle):
    def __init__(self, *args, nDoors:int=4):
        super().__init__(*args)
        self.__doors = nDoors


    '''Public methods'''

    def CarInfos(self):
        self.VehicleInfos()
        print(f"Portes: {self.__doors}")


    def Start(self):
        print(f"La voiture roule")





class Moto(Vehicle):
    def __init__(self, *args, wheels:int=2):
        super().__init__(*args)
        self.__wheels = wheels


    '''Public methods'''

    def BikeInfos(self):
        self.VehicleInfos()
        print(f"Roues: {self.__wheels}")


    def Start(self):
        print(f"La moto roule")


#Demonstrates all classes
car = Voiture("Mercedes", "Classe A", 2020, 18500)
bike = Moto("Yamaha", "1200 Vmax", 1987, 4500)

car.CarInfos()
bike.BikeInfos()