def StringLen(string:str):
    n = 0
    string = string[1:]

    if string != "":
        n = StringLen(string)

    return n + 1



def IdenticalString(string1:str, string2:str, i:int=0, j:int=0):
    char1, char2 = None, None

    try:
        char1, char2 = string1.lower()[i], string2.lower()[j]
        
    except:
        if string1.lower()[i - 1] == "*" or string2.lower()[j - 1] == "*":
            return 1
        
        return 0


    if char1 == "*":
        i = IdenticalString(string1, string2, i + 1, j)

    elif char2 == "*":
        i = IdenticalString(string1, string2, i, j + 1)
    
    elif char1 != char2:
        return 0

    elif i < StringLen(string1) - 1:
        i = IdenticalString(string1, string2, i + 1, j + 1) 


    if i == 0:
        return 0
    
    return 1




def Input():
    try:
        string1 = str(input("Enter a first string: "))
        string2 = str(input("Enter a second string: "))
        if isinstance(string1, str) and isinstance(string2, str):
            return string1, string2

    except KeyboardInterrupt:
        exit("\nExit program")

    except:
        print("Sorry invalid input, try again")
        Input()





if __name__ == "__main__":
    string1, string2 = Input()
    print("1 = identical string, 0 = different string:")
    print(IdenticalString(string1, string2))