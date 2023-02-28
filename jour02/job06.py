class Commande:
    def __init__(self):
        self.__order = {}

        """Did not understand what to do with these variables"""
        #self.__orderNumber = len(list(self.__order.keys()))
        #self.__orderStatus = ""


    '''Public methods'''
    def AddOrder(self, dish:str, pricePreTax:float):
        self.__order.update({dish:{"Price":float('%.2f' % pricePreTax), "Status":"In preparation"}})

    def CancelOrder(self, dishToCancel:str):
        if dishToCancel in self.__order:
            print(f"{dishToCancel} successfully canceled\n")
            del self.__order[dishToCancel]
        
        else:
            print(f"{dishToCancel} is not present in that order")

    def OrderInfo(self):
        print(f"\nDishes in preparation\n")
        for dish in self.__order:
            print(f"Dish: {dish}, Price (pre-tax): {self.__order[dish]['Price']}")
            
        print(f"\nTotal with tax: {self.__TVA()}")
        print(f"Total without tax: {self.__OrderTotal()}\n")



    '''Private methods'''
    def __OrderTotal(self):
        total = 0
        for dish in self.__order:
            total += self.__order[dish]["Price"]

        return total

    def __TVA(self):
        taxTotal = 0
        for dish in self.__order:
            taxTotal += float("%.2f" % (self.__order[dish]["Price"] * 1.2))

        return taxTotal
    

#Demonstrates the 'Commande' class
order = Commande()

order.AddOrder("Steak", 5.50)
order.AddOrder("Fries", 1.50)
order.AddOrder("PorkChop", 6.50)

order.OrderInfo()

order.CancelOrder("Burger")
order.CancelOrder("Steak")

order.OrderInfo()