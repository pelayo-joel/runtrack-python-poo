def ListLen(lenList:list):
    n = 0
    lenList = lenList[1:]

    if lenList != []:
        n = ListLen(lenList)

    return n + 1



def ListMax(myList:list, i:int=0, maxi:int=0):
    if i < ListLen(myList):
        if myList[i] > maxi:
            maxi = myList[i]

        return ListMax(myList, i + 1, maxi)

    return maxi





aList = [3, 5, 1, 7, 8, 11, 7, 3, 9]
print(ListMax(aList))