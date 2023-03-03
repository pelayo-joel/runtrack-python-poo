def Fibonacci(i:int, n:int=1, n2:int=0):
    if i > 2:
        return Fibonacci(i - 1, n + n2, n)
    
    return n



def Input():
    try:
        fibPos = int(input("Choose a Fibonacci position: "))
        if isinstance(fibPos, int):
            return fibPos

    except KeyboardInterrupt:
        exit("\nExit program")

    except:
        print("Input must be an integer")
        Input()





if __name__ == "__main__":
    fibPos = Input()
    print(f"Value at position {fibPos} in the Fibonacci sequence is: {Fibonacci(fibPos)}")