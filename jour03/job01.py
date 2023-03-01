class Ville:
    def __init__(self, cityName:str, nCitizen:int):
        self.__name = cityName
        self.__nCitizen = nCitizen



    '''Public methods'''
    def AddCitizen(self):
        self.__nCitizen += 1

    def GetCitizen(self):
        return self.__nCitizen



class Personne:
    def __init__(self, name:str, age:int, city:Ville):
        self.__name, self.__age = name, age
        self.__city = city
        self.__AddToPopulation()


    '''Private methods'''
    #Add to population to city
    def __AddToPopulation(self):
        self.__city.AddCitizen()



#Demonstrates both 'Ville' and 'Personne' class
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Population de la ville de Paris: {paris.GetCitizen()} habitants.")
print(f"Population de la ville de Marseille: {marseille.GetCitizen()} habitants.")

jaune = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
cloche = Personne("Chloe", 18, marseille)

print(f"Mise a jour de la population de la ville de Paris: {paris.GetCitizen()} habitants.")
print(f"Mise a jour de la population de la ville de Marseille: {marseille.GetCitizen()} habitants.")