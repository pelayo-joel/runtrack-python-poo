class Personne:
    def __init__(self, firstname:str, name:str):
        self.__firstname, self.__name = firstname, name

    #Returns a presentation of the 'Personne'
    def SePresenter(self):
        return f"Je suis {self.__name} {self.__firstname}"
    

personne1 = Personne("Pelayo", "Joel")
personne2 = Personne("FirstName", "Name")

#Prints both person's presentation
print(personne1.SePresenter())
print(personne2.SePresenter())