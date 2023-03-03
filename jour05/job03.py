def StrLength(string:str):
    n = 0
    string = string[1:]

    if string != "":
        n = StrLength(string)
    
    return n + 1


print(StrLength("Hello man"))