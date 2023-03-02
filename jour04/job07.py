import random
import time
import os

class Carte:
    def __init__(self, value:str, color:str):
        self.__value, self.__color = value, color

    def __str__(self):
        return f"{self.__value}, {self.__color}"




    '''Public methods'''

    #Getters
    def GetColor(self):
        return self.__color
    
    def GetValue(self):
        return self.__value





class Jeu:
    def __init__(self):
        self.__specialValues = {
            "Valet":10,
            "Dame":10,
            "Roi":10,
            "As":None
        }

        self.__deck = self.__NewDeck()
        self.__playerScore, self.__cpuScore = 0, 0
        self.__turn = 1
        self.__playerTurn = False




    '''Public methods'''

    def Run(self):
        self.__ClearScreen()

        while True:
            self.__DisplayUI()
            self.__playerTurn = True
            
            if self.__CheckGameEnd():
                input("\nPress enter to continue...")
                self.__ClearScreen()
                return None

            playerDraw = input("yes/y to draw or other to hold ")

            if playerDraw.lower() == "yes" or playerDraw.lower() == "y":
                cardDrawed = random.choice(self.__deck)
                value = cardDrawed.GetValue()

                if cardDrawed.GetValue() in list(self.__specialValues.keys()):
                    if cardDrawed.GetValue() == "As":
                        value = self.__AsChoice()
                    else:
                        value = self.__specialValues[cardDrawed.GetValue()]

                self.__playerScore += int(value)
                self.__deck.remove(cardDrawed)
                print(f"You drawed {cardDrawed.GetValue()} {cardDrawed.GetColor()}\n")

            else:
                print("You kept your score\n")

            self.__playerTurn = False

            print("The Dealer's thinking...")
            time.sleep(random.randint(1, 2))

            if self.__cpuScore < 17:
                cardDrawed = random.choice(self.__deck)
                value = cardDrawed.GetValue()

                if cardDrawed.GetValue() in list(self.__specialValues.keys()):
                    if cardDrawed.GetValue() == "As":

                        if self.__cpuScore < 11:
                            value = self.__AsChoice()
                            time.sleep(1)

                        else:
                            value = 1
                            time.sleep(1)

                    else:
                        value = self.__specialValues[cardDrawed.GetValue()]

                self.__cpuScore += int(value)
                self.__deck.remove(cardDrawed)
                print(f"Dealer drawed {cardDrawed.GetValue()} {cardDrawed.GetColor()}\n")

            else:
                print("Dealer keeps his score\n")

            input("\nPress enter to continue...")
            self.__turn += 1
            self.__ClearScreen()
    


    '''Private methods'''

    def __DisplayUI(self):
        print("\n", "-" * 100)
        print("-" * 100)
        print(f"||| Turn {self.__turn} |||\n")
        print(f"\n|| Your score ||")
        print(f"\nYour current score: {self.__playerScore}\n")

        print(f"\n|| Dealer's Score ||")
        print(f"\nDealer's current score: {self.__cpuScore}")
        print("\n", "-" * 100)
        print("-" * 100, "\n")


    def __AsChoice(self):
        print("Draws the 'As' card")
        if self.__playerTurn:
            while True:
                try:
                    valueChoice = int(input("Tap 0 to give +1, Tap 1 to give +11: "))

                    if valueChoice == 0:
                        print("+1")
                        return 1
                    elif valueChoice == 1:
                        print("+11")
                        return 11

                except:
                    print("Chose betweem 0 or 1")

        else:
            cpuValueChoice = random.choice([1, 11])
            print(f"Dealer chose +{cpuValueChoice}")
            return cpuValueChoice


    def __CheckGameEnd(self):
        if self.__turn == 5:
            self.__EndByTurn()
            return True

        elif self.__playerScore == 21:
            print("Blackjack !")
            return True
        
        elif self.__cpuScore == 21:
            print("You lost, Blackjack for the Dealer...")
            return True
        
        elif self.__playerScore > 21:
            print("You lost, you're above 21...")
            return True
        
        elif self.__cpuScore > 21:
            print("You won ! The Dealer's above 21")
            return True


    def __EndByTurn(self):
        if self.__cpuScore < self.__playerScore < 21:
            print("You won ! game ended with you being closer to 21")
        
        elif self.__playerScore < self.__cpuScore < 21:
            print("You lost, game ended with the Dealer closer to 21...")


    def __ClearScreen(self):
        osName = os.name
        if osName == "posix":
            os.system('clear')
        elif osName == "nt":
            os.system("cls")


    def __NewDeck(self):
        deck = []
        colors = ["Pique", "Carre", "Coeur", "Carreau"]

        for color in colors:
            for i in range(2, 10):
                newCard = Carte(f"{i}", color)
                deck.append(newCard)

            for value in self.__specialValues:
                newCard = Carte(f"{value}", color)
                deck.append(newCard)

        return deck










if __name__ == "__main__":
    GAMING = True

    while GAMING:
        Game = Jeu()
        Game.Run()

        print("Would you like to play again ?")
        replay = str(input("0 - Quit, 'Other keys' - Play again: "))
        
        if replay == '0':
            GAMING = False