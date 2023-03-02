class Personne:
    def __init__(self):
        self._age = 14


    '''Public methods'''

    def PrintAge(self):
        print(self._age)


    def Hello(self):
        print("Hello")


    def ChangeAge(self, newAge:int):
        self._age = newAge





class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)


    '''Public methods'''

    def GoToClass(self):
        print("Je vais en cours")


    def PrintAge(self):
        print(f"J'ai {self._age} ans")





class Professeur(Personne):
    def __init__(self):
        Personne.__init__(self)
        self.__teachedCourse = "Math"


    '''Public methods'''

    def Teach(self):
        print("Le cours va commencer")



#Demonstrates 'Personne' and 'Eleve' class as per the assignement
person = Personne()
pupil = Eleve()

pupil.PrintAge()
