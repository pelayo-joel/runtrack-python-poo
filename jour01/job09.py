class Produit:
    def __init__(self, nom:str, prixHT:float, TVA:float):
        self.nom, self.prixHT = nom, prixHT
        self.TVA = max(min(TVA, 2.0), 1.0)


    #Returns the post-tax price
    def CalculerPrixTTC(self):
        return self.prixHT * self.TVA

    def Afficher(self):
        print(f"Produit: {self.nom}")
        print(f"TVA: {self.TVA}, PrixHT: {self.prixHT}, PrixTTC: {'%.2f' % self.CalculerPrixTTC()}")


#Demonstrates the class
produit1 = Produit("Pomme", 1.25, 1.2)
produit2 = Produit("Medoc", 4.25, 1.15)

produit1.Afficher()
produit2.Afficher()