class Livre:
    def __init__(self):
        self.__title, self.__author, self.__nPages = None, None, None
        self.__availablility = True
        

    '''Public methods'''
    #Defines methods managing the availability of the book
    def Emprunter(self):
        if self.__Verification():
            self.__availablility = False
            print(f"This book is available ! Enjoy your reading.")
        
        else:
            print(f"This book is not available.")

    def Rendre(self):
        if not self.__Verification():
            self.__availablility = True
            print(f"Thanks for your reading, hope you had a good time !")

        else:
            print(f"This book has already been brought back.")


    #Defines getters/setters of the class
    def SetTitle(self, title:str):
        self.__title = title

    def SetAuthor(self, author:str):
        self.__author = author

    def SetPages(self, pages:int):
        try:
            if pages >= 0:
                self.__nPages = pages

            else:
                print(f"Variable 'pages' must be a positive integer")

        except:
            print(f"Variable 'pages' must be an integer")

    def GetTitle(self):
        return self.__title

    def GetAuthor(self):
        return self.__author

    def GetPages(self):
        return self.__nPages
    

    '''Private methods'''
    def __Verification(self):
        return self.__availablility

#Demonstrates the class and its getter/setters
book = Livre()

book.SetTitle("My Book")
book.SetAuthor("The books author")

#Demonstrates the catch of the type error or negative integer error
book.SetPages("44")
print(f"Title: {book.GetTitle()}, Author: {book.GetAuthor()}, Number of pages: {book.GetPages()}\n")

book.SetPages(-44)
print(f"Title: {book.GetTitle()}, Author: {book.GetAuthor()}, Number of pages: {book.GetPages()}\n")


book.SetPages(44)
print(f"Title: {book.GetTitle()}, Author: {book.GetAuthor()}, Number of pages: {book.GetPages()}")