def Power(x:int, n:int):
    if n >= 2:
        return x * Power(x, n - 1)
    
    return x


print(Power(2, 5))