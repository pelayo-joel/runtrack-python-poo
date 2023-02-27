class Animal:
    def __init__(self, age:int=0, name:str=None):
        self.age, self.name = age, name


    #Makes the animal older by incrementing its 'age' attribute
    def Vieillir(self):
        self.age += 1

    #Names (or renames) the animal
    def Nommer(self, name:str):
        self.name = name


#Demonstrates the class and its methods
animal = Animal()

print(f"L'age de l'animal {animal.age}")
animal.Vieillir()
print(f"L'age de l'animal {animal.age}")

animal.Nommer("Luna")
print(f"L'animal se nomme {animal.name}")