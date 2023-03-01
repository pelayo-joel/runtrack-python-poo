import random

class Player:
    def __init__(self, name:str, pos:int, goals:int, nAssists:int):
        self.__name = name
        self.__pos = pos

        self.__goals, self.__nAssists = goals, nAssists
        self.__yellowFouls, self.__redFouls = 0, 0
        #yellowFool:int, redFool:int


    '''Public methods'''
    def Goal(self):
        self.__goals += 1
    

    def Assist(self):
        self.__nAssists
    

    def YellowFool(self):
        self.__yellowFouls += 1
    

    def RedFool(self):
        self.__redFouls += 1
    

    def Player(self):
        return self.__name, self.__pos


    def Stats(self):
        return self.__goals, self.__nAssists, self.__yellowFouls, self.__redFouls




class SoccerTeam:
    def __init__(self, teamName:str) -> None:
        self.__team = teamName
        self.__playerList = []



    '''Public methods'''
    def AddPlayer(self, newPlayer:Player):
        self.__playerList.append(newPlayer)


    def PlayersStats(self):
        print(f"Players Stats:")
        for player in self.__playerList:
            playerGoals, playerAssists, playerMinorFouls, playerMajorFouls = player.Stats()
            print(f" - {player.Player()}:")
            print(f"    - Goals: {playerGoals}")
            print(f"    - Assists: {playerAssists}")
            print(f"    - Fools: Yellow: {playerMinorFouls}, Red: {playerMajorFouls}\n")


    #Not used because of how 'PlayerStats' works    
    def UpdatePlayerStats(self):
        self.PlayersStats()

    
    def GetTeam(self):
        return self.__playerList


#Demonstrates both 'Player' and 'SoccerTeam' class
names = ["Bro", "Bro2", "Bro3", "BrosCaptain"]
team = SoccerTeam("BroTeam")

for i in range(len(names)):
    name = names[i]
    names[i] = Player(name, random.randint(1, 4), random.randint(0, 9), random.randint(5, 19))
    team.AddPlayer(names[i])


team.PlayersStats()

names[0].RedFool()
names[0].RedFool()
names[2].RedFool()
names[1].Goal()
names[3].Assist()
team.PlayersStats()