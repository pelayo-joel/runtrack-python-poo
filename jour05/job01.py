def Factorial(n:int):
    if n >= 2:
        return n * Factorial(n - 1)
    
    return n
        
    

print(Factorial(5))