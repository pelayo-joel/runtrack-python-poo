import random
import time
import os
#from colorama import Fore, Back, Style

class Personnage:
    def __init__(self, name:str, initHP:int, initStamina:int, initMP:int):
        self.__name = name
        self.__maxHP, self.__maxStamina, self.__maxMP = initHP, initStamina, initMP
        self.__hp, self.__stamina, self.__mp = self.__maxHP, self.__maxStamina, self.__maxMP

        self.__strength = 7
        self.__magic = 4
        self.__defense = 2

        self.__guard = False

        self.__afflicted = False
        self.__afflictionReduction = 2
        self.__actualState = ""
        self.__stateDuration = 0

        self.__states = {
            "Burn":{
                "Effect":4,
                "Duration":2
            }, 
            "Poison":{
                "Effect":2,
                "Duration":4
            }, 
            "Freeze":{
                "Effect":2,
                "Duration":2
            }, 
            "Charmed":{
                #"Effect":True,
                "Duration":2
            }
        }




    '''Public methods'''


    '''Actions Selection system'''

    def TakeAction(self, action:int, target:'Personnage'):
        print("\n")
        healingTarget = self

        if self.__actualState == "Charmed":
            target = self
            healingTarget = target
            action = random.randint(1, 6)
            self.__stateDuration += 1

            if self.__stateDuration == self.__states[self.__actualState]["Duration"]:
                self.__ClearAffliction()
                print(f"{self.__name} is now back to his senses")
        
        elif self.__actualState == "Burn":
            self.__Damage(self.__states[self.__actualState]["Effect"])
            print(f"{self.__name} took {self.__states[self.__actualState]['Effect']} damage from burning")
            self.__stateDuration += 1

            if self.__stateDuration == self.__states[self.__actualState]["Duration"]:
                self.__ClearAffliction()
                print(f"{self.__name} is not burning anymore")

        elif self.__actualState == "Poison":
            self.__Damage(self.__states[self.__actualState]["Effect"])
            print(f"{self.__name} took {self.__states[self.__actualState]['Effect']} damage from poison")
            self.__stateDuration += 1

            if self.__stateDuration == self.__states[self.__actualState]["Duration"]:
                self.__ClearAffliction()
                print(f"{self.__name} is not poisoned anymore")

        elif self.__actualState == "Freeze":
            print(f"{self.__name} is freezed")
            self.__stateDuration += 1

            if self.__stateDuration == self.__states[self.__actualState]["Duration"]:
                self.__ClearAffliction()
                print(f"{self.__name} is now unfreezed")

            return None


        if self.__IsGuarding():
            self.__guard = False

        if "Enemy" in self.__name and (self.__stamina < 5 or self.__mp < 10):
                action = random.choice([8, 9])
             

        match action:
            case 1:
                self.__NormalAttack(target)
            case 2:
                self.__HeavyAttack(target)
            case 3:
                self.__FireBall(target)
            case 4:
                self.__IceAge(target)
            case 5:
                self.__PoisonKnife(target)
            case 6:
                self.__Healing(healingTarget)
            case 7:
                self.__Dance(target)
            case 8:
                self.__Rest()
            case 9:
                self.__Concentrate()
            case 10:
                self.__Guard()



    '''Get/Display info'''

    def GetName(self):
        return self.__name

    def GetHP(self):
        return self.__hp
    
    def GetState(self):
        return self.__actualState
    

    def HPBar(self):
        print(f"{self.__name} HP: [{'#' * self.__hp}{'-' * (self.__maxHP - self.__hp)}]")
    
    def StaminaBar(self):
        print(f"{self.__name} Stamina: [{'#' * self.__stamina}{'-' * (self.__maxStamina - self.__stamina)}]")

    def MPBar(self):
        print(f"{self.__name} MP: [{'#' * self.__mp}{'-' * (self.__maxMP - self.__mp)}]")




    '''Private methods'''


    '''Actions'''

    def __NormalAttack(self, target:'Personnage'):
        print(f"{self.__name} is trying a normal attack...")
        time.sleep(random.randint(2, 4))

        damageInflicted = int(self.__strength * random.uniform(1.0, 1.2))
        if self.__afflicted:
            damageInflicted -= self.__afflictionReduction

        if self.__stamina >= 5:
            self.__stamina -= 5
            self.__stamina = max(self.__stamina, 0)

            if random.randint(0, 100) < 95:
                if target.__IsGuarding():
                    mitigatedDamage = damageInflicted - 3
                    target.__Damage(mitigatedDamage)
                    print(f"{self.__name} inflicted {mitigatedDamage} damage to {target.__name}")
                
                else:
                    target.__Damage(damageInflicted)
                    print(f"{self.__name} inflicted {damageInflicted} damage to {target.__name}")

            else:
                print(f"{self.__name} missed !\n")

        else:
            print(f"{self.__name} has not enough stamina\n")


    def __HeavyAttack(self, target:'Personnage'):
        print(f"{self.__name} is trying a heavy attack...")
        time.sleep(random.randint(2, 4))

        damageInflicted = int(self.__strength * random.uniform(1.5, 1.7))
        if self.__afflicted:
            damageInflicted -= self.__afflictionReduction

        if self.__stamina >= 8:
            self.__stamina -= 8
            self.__stamina = max(self.__stamina, 0)

            if random.randint(0, 100) < 75:
                if target.__IsGuarding():
                    mitigatedDamage = damageInflicted - 3
                    target.__Damage(mitigatedDamage)
                    print(f"{self.__name} inflicted {mitigatedDamage} damage to {target.__name}")
                
                else:
                    target.__Damage(damageInflicted)
                    print(f"{self.__name} inflicted {damageInflicted} damage to {target.__name}")

            else:
                print(f"{self.__name} missed !\n")

        else:
            print(f"{self.__name} has not enough stamina\n")


    def __FireBall(self, target:'Personnage'):
        print(f"{self.__name} is trying to cast a FireBall...")
        time.sleep(random.randint(2, 4))

        initialDamageInflicted = int(self.__magic * random.uniform(2.0, 2.5))
        if self.__afflicted:
            initialDamageInflicted -= self.__afflictionReduction

        if self.__mp >= 10:
            self.__mp -= 10
            self.__mp = max(self.__mp, 0)

            if random.randint(0, 100) < 60: 
                target.__Damage(initialDamageInflicted)

                if not target.__IsGuarding():
                    target.__Affliction("Burn")
                    print(f"{target.__name} got burned and inflicted {initialDamageInflicted} damage to {target.__name}\n")
                else:
                    print(f"{target.__name} inflicted {initialDamageInflicted} damage to {target.__name}\n")
            
            else:
                print(f"{self.__name} missed !\n")

        else:
            print(f"{self.__name} has not enough MP\n")


    def __IceAge(self, target:'Personnage'):
        print(f"{self.__name} is trying to cast the IceAge spell...")
        time.sleep(random.randint(2, 4))

        initialDamageInflicted = int(self.__magic * random.uniform(1.2, 1.5))
        if self.__afflicted:
            initialDamageInflicted -= self.__afflictionReduction

        if self.__mp >= 10:
            self.__mp -= 10
            self.__mp = max(self.__mp, 0)

            if random.randint(0, 100) < 65:
                target.__Damage(initialDamageInflicted)

                if not target.__IsGuarding():
                    target.__Affliction("Freeze")
                    print(f"{target.__name} got freezed and inflicted {initialDamageInflicted} damage to {target.__name}\n")

                else:
                    print(f"{target.__name} inflicted {initialDamageInflicted} damage to {target.__name}\n")

            else:
                print(f"{self.__name} missed !\n")

        else:
            print(f"{self.__name} has not enough MP\n")


    def __PoisonKnife(self, target:'Personnage'):
        print(f"{self.__name} is trying to throw poisoned knife to his opponent...")
        time.sleep(random.randint(2, 4))

        initialDamageInflicted = int(self.__strength * random.uniform(1.4, 1.8))
        if self.__afflicted:
            initialDamageInflicted -= self.__afflictionReduction

        if self.__stamina >= 9:
            self.__stamina -= 9
            self.__stamina = max(self.__stamina, 0)

            if random.randint(0, 100) < 75: 
                target.__Damage(initialDamageInflicted)

                if not target.__IsGuarding():
                    target.__Affliction("Poison")
                    print(f"{target.__name} has been poisoned and inflicted {initialDamageInflicted} damage to {target.__name}\n")

                else:
                    print(f"{target.__name} inflicted {initialDamageInflicted} damage to {target.__name}\n")
            
            else:
                print(f"{self.__name} missed !\n")

        else:
            print(f"{self.__name} has not enough stamina\n")


    def __Dance(self, target:'Personnage'):
        print(f"{self.__name} is trying to charm his opponent...")
        time.sleep(random.randint(2, 4))

        if self.__stamina >= 8 and self.__mp >= 3:
            self.__stamina -= 8
            self.__mp -= 3
            self.__stamina = max(self.__stamina, 0)
            self.__mp = max(self.__mp, 0)

            if random.randint(0, 100) < 40: 
                target.__Affliction("Charmed")
                print(f"{target.__name} got charmed by {self.__name} dance\n")

            else:
                print(f"{target.__name} was not charmed by {self.__name} dance !\n")

        else:
            print(f"{self.__name} has not enough stamina or MP\n")


    def __Healing(self, target:'Personnage'):
        print(f"{self.__name} is healing himself...")
        time.sleep(random.randint(2, 4))

        if self.__mp >= 5:
            self.__mp -= 5
            self.__mp = max(self.__mp, 0)
            target.__Heal()

        else:
            print(f"{self.__name} has not enough MP\n")


    def __Guard(self):
        print(f"{self.__name} is preparing himself for the next move...")
        self.__guard = True


    def __Rest(self):
        print(f"{self.__name} rests...")
        time.sleep(random.randint(1, 2))

        self.__stamina += 8
        self.__stamina = min(self.__stamina, self.__maxStamina)

        print(f"{self.__name} has recovered 5 stamina points")
        if self.__stamina >= self.__maxStamina:
            print(f"{self.__name} is fully rested\n")


    def __Concentrate(self):
        print(f"{self.__name} concentrates...")
        time.sleep(random.randint(1, 2))

        self.__mp += random.randint(5, 9)
        self.__mp = min(self.__mp, self.__maxMP)

        print(f"{self.__name} has recovered 5 MP")
        if self.__mp >= self.__maxMP:
            print(f"{self.__name} is full of MP\n")


    '''Character status manager'''

    def __IsGuarding(self):
        return self.__guard


    def __Affliction(self, newState:str):
        self.__afflicted = True
        self.__stateDuration = 0
        self.__actualState = newState


    def __ClearAffliction(self):
        self.__actualState = 0
        self.__stateDuration = 0
        self.__afflicted = False


    def __Heal(self):
        recoveredHP = int(self.__magic * random.uniform(1.5, 2.0))
        self.__hp += recoveredHP
        self.__hp = min(self.__hp, self.__maxHP)
        self.__afflicted = False
        self.__actualState = ""

        print(f"{self.__name} has recovered {recoveredHP} HP")
        if self.__stamina >= self.__maxStamina:
            print(f"{self.__name} is fully recovered")


    def __Damage(self, damage:int):
        self.__hp -= (damage - self.__defense)
        self.__hp = max(self.__hp, 0)










class Jeu:
    def __init__(self, difficulty:int):
        playerName = str(input("Choose your name: "))
        enemyName = str(input("Choose enemy name: "))

        if difficulty == 1:
            self.__enemy = Personnage(f"Easy {enemyName} Enemy", 50, 30, 20)

        elif difficulty == 2:
            self.__enemy = Personnage(f"Intermediate {enemyName} Enemy", 75, 40, 30)

        elif difficulty == 3:
            self.__enemy = Personnage(f"Hard {enemyName} Enemy", 100, 50, 40)


        self.__player = Personnage(playerName, 50, 30, 20)

        self.__charList = [self.__player, self.__enemy]



    '''Public methods'''


    def Run(self):
        self.__ClearScreen()
        while True:
            self.__DisplayUI()


            while True:
                try:
                    playerAction = int(input("Choose among the 10 actions\n"))

                    if 1 <= playerAction <= 10:
                        break

                except KeyboardInterrupt:
                    exit("Game exit")

                except:
                    print("Invalid input, choose between 1 to 9")


            print("Enemy is choosing...\n")
            time.sleep(random.randint(1, 5))
            enemyAction = random.randint(1, 10)

            self.__player.TakeAction(playerAction, self.__enemy)
            if self.__CheckDeath():
                self.__ClearScreen()
                return None
            
            self.__enemy.TakeAction(enemyAction, self.__player)
            if self.__CheckDeath():
                self.__ClearScreen()
                return None

            print("\nActions during this turn...")
            input("Press enter to continue")
            self.__ClearScreen()

        



    '''Private methods'''


    def __DisplayUI(self):
        print("\n\n", "-" * 150)
        print("-" * 150, "\n")

        for i in range(len(self.__charList) - 1, -1, -1):
            print(f"\n|| {self.__charList[i].GetName()} Info ||\n")
            self.__charList[i].HPBar()
            self.__charList[i].StaminaBar()
            self.__charList[i].MPBar()

        print(" " * 64, "-" *20, " " * 64)
        print(" " * 71, "Actions", " " * 71)
        print(f"\n{' ' * 52} 1 - Normal atk   2 - Heavy atk   3 - FireBall")
        print(f"\n{' ' * 52} 4 - Ice Age   5 - Poison Knife   6 - Healing")
        print(f"\n{' ' * 52} 7 - Dance   8 - Rest   9 - Concentrate")
        print(f"\n{' ' * 65} 10 - Guard")
        print("-" * 150)
        print("-" * 150, "\n")

    
    def __CheckDeath(self):
        for i in range(len(self.__charList)):
            if self.__charList[i].GetHP() <= 0:
                print(f"{self.__charList[i].GetName()} has died !")
                
                i += 1
                i = (i % len(self.__charList))
                print(f"{self.__charList[i].GetName()} is victorious !")

                return True
            

    def __ClearScreen(self):
        osName = os.name
        if osName == "posix":
            os.system("clear")
        elif osName == "nt":
            os.system("cls")
        











if __name__ == "__main__":
    GAMING = True

    while GAMING:
        while True:
            try:
                difficulty = int(input("Choose a difficulty: "))

                if 1 <= difficulty <= 3: 
                    Game = Jeu(difficulty)
                    break

            except KeyboardInterrupt:
                exit("Game exit")

            except:
                print("Invalid input, choose between 1 to 3")

        Game.Run()

        print("Would you like to play again ?")
        replay = str(input("0 - Quit, 'Other keys' - Play again: "))
        
        if replay == '0':
            GAMING = False