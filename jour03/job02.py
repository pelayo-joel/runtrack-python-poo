import random

class CompteBancaire:
    def __init__(self, firstName:str, name:str, sold:float):
        self.__accountNumber = random.randint(1000000, 1999999)
        self.__sold = sold
        self.__firstName, self.__name = firstName, name

        if self.__sold < 0:
            self.__overdraft = True

        else:
            self.__overdraft = False




    '''Public methods'''
    def Afficher(self):
        print(f"\nAccount N.: {self.__accountNumber}")
        print(f"First Name: {self.__firstName}, Name: {self.__name}")


    def AfficherSolde(self):
        print(f"Account sold: {self.__sold}")


    def Agios(self):
        if self.__sold < 0:
            self.__sold += (self.__sold * -1)


    def Virement(self, accountTarget, amount:float):
        try:
            self.__Retrait(amount)
            accountTarget.Versement(amount)
        except:
            print(f"'AccountTarget' must a be of type 'CompteBancaire'")



    '''Private methods'''
    def __Versement(self, transfer:float):
        self.__sold += float('%.2f' % transfer)

        if self.__sold >= 0:
            self.__overdraft = False


    def __Retrait(self, withdraw:int):
        if self.__sold < withdraw:
            print(f"\nNot enough sold to withdraw")
            self.__overdraft = True
        
        self.__sold -= withdraw


#Demonstrates the CompteBancaire
compte1 = CompteBancaire("Bezos", "Jeff", 99999999999.04)
compte2 = CompteBancaire("Bruh", "Poverty", -23.00)
print(compte1)

compte1.Afficher()
compte1.AfficherSolde()

compte2.Afficher()
compte2.AfficherSolde()


compte1.Virement(compte2, 32)

compte2.Afficher()
compte2.AfficherSolde()

compte2.Virement(compte1, 12)

compte2.Afficher()
compte2.AfficherSolde()