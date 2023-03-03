import random

def ListLen(lenList:list):
    n = 0
    lenList = lenList[1:]

    if lenList != []:
        n = ListLen(lenList)

    return n + 1



def GameLadies(rows:int, row:int=0, colPosTaken:list=[]):
    
    def RandomColPos(posTaken:list=colPosTaken):
        colPos = random.randint(1, rows) - 1

        if colPos in posTaken:
            return RandomColPos(posTaken)
        
        posTaken += [colPos - 1, colPos + 1]
        return colPos, posTaken


    if row < rows:
        boardRow = [" "] * rows
        rndColPos, colPosTaken = RandomColPos()

        boardRow[rndColPos] = "X"

        print(boardRow)
        row = GameLadies(rows, row + 1, colPosTaken)




def Input():
    try:
        size = int(input("Choose the board size: "))
        if isinstance(size, int):
            return size

    except KeyboardInterrupt:
        exit("\nExit program")

    except:
        print("Input must be an integer")
        Input()





if __name__ == "__main__":
    GameLadies(Input())